from django.db import models


class Pi(models.Model):
    mac_address = models.CharField(max_length=255)