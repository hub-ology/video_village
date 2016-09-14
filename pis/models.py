# DAS added Pi.__str__()
import json

import requests
from django.db import models


class Pi(models.Model):
    mac_address = models.CharField(max_length=255)
    status = models.TextField(null=False, blank=True)
    notes = models.CharField(max_length=255, null=False, blank=True)
    tunnel = models.CharField(max_length=255, null=False, blank=True)
    projector_connected = models.BooleanField(default=False)
    projector_on = models.BooleanField(default=False)
    playlist_active = models.BooleanField(default=False)

    def __str__(self):
        return "Pi {}: {}".format(self.id, self.mac_address)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        super(Pi, self).save()
        self.parse_status()

    def parse_status(self):
        if self.status:
            status_data = json.loads(self.status)
            projector = status_data.get('projector')
            if projector:
                self.projector_connected = projector.get('connected')
                self.projector_on = projector.get('on')

            tunnels = status_data.get('tunnels')
            if tunnels:
                self.tunnel = tunnels.get('pivideo')

    def turn_projector_on(self):
        if self.tunnel:
            r = requests.get(self.tunnel + '/projector/on')
            return r.json()

    def turn_projector_off(self):
        if self.tunnel:
            r = requests.get(self.tunnel + '/projector/off')
            return r.json()

