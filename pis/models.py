from django.db import models

class Pi(models.Model):
    mac_address = models.CharField(max_length=255)

class Window(models.Model):
    building = models.PositiveIntegerField()
    pi = models.ForeignKey(Pi, null=True, blank=True)