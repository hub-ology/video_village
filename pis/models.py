# DAS added Pi.__str__()
import json

import requests
from django.db import models
from django.conf import settings

NGROK_AUTH = (settings.NGROK_AUTH_USER, settings.NGROK_AUTH_TOKEN)

class Pi(models.Model):
    mac_address = models.CharField(max_length=255)
    status = models.TextField(null=False, blank=True)
    notes = models.CharField(max_length=255, null=False, blank=True)
    tunnel = models.CharField(max_length=255, null=False, blank=True)
    projector_connected = models.BooleanField(default=False)
    projector_on = models.BooleanField(default=False)
    playlist_active = models.BooleanField(default=False)
    cpu_temp = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    ssh_tunnel = models.CharField(max_length=255, null=False, blank=True)
    software_version = models.CharField(max_length=10, null=False, blank=True)
    file_cache_size = models.CharField(max_length=10, null=False, blank=True)
    sd_available_space = models.CharField(max_length=10, null=False, blank=True)
    local_ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return "Pi {}: {}".format(self.id, self.mac_address)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.parse_status()
        super(Pi, self).save()

    def parse_status(self):
        if self.status:
            status_data = json.loads(self.status)
            version = status_data.get('version')
            if version:
                self.software_version = version

            sd_card = status_data.get('sd_card')
            if sd_card:
                self.file_cache_size = sd_card.get('file_cache')
                self.sd_available_space = sd_card.get('available')
            self.local_ip_address = status_data.get('ip_address')
            projector = status_data.get('projector')
            if projector:
                self.projector_connected = projector.get('connected')
                projector_on = projector.get('on')
                if projector_on:
                    self.projector_on = True
                else:
                    self.projector_on = False

            tunnels = status_data.get('tunnels')
            if tunnels:
                self.tunnel = tunnels.get('pivideo')
                try:
                    if tunnels.get('ssh'):
                        self.ssh_tunnel = tunnels.get('ssh')
                except:
                    pass

            try:
                self.cpu_temp = status_data.get('cpu_temp')
            except:
                pass

            try:
                self.cachefile_set.all().delete()
                file_cache = status_data.get('file_cache')
                for f in file_cache:
                    file = CacheFile(pi=self, file_name=f)
                    file.save()
            except:
                pass


    def turn_projector_on(self):
        if self.tunnel:
            r = requests.post(self.tunnel + '/projector/on', auth=NGROK_AUTH)
            return r.json()

    def turn_projector_off(self):
        if self.tunnel:
            r = requests.post(self.tunnel + '/projector/off', auth=NGROK_AUTH)
            return r.json()

    def get_status(self):
        if self.tunnel:
            r = requests.get(self.tunnel + '/status', auth=NGROK_AUTH)
            return r.json()

    def play(self, video=None, playlist=None, loop=False, start_time=None, end_time=None):
        if self.tunnel:

            if video:
                data = {'video':video.url}
            else:
                videos = [{'video': v.url} for v in playlist]
                data = {'playlist': videos, 'start_time': start_time, 'end_time': end_time, 'loop': loop}

            r = requests.post(self.tunnel + '/play', auth=NGROK_AUTH, json=data)

            return r.json()


class CacheFile(models.Model):
    pi = models.ForeignKey(Pi)
    file_name = models.CharField(max_length=255)
