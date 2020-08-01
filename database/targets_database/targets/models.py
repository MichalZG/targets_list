from django.db import models

class Target(models.Model):
    name = models.CharField(max_length=54, unique=True)
    ra = models.DecimalField(max_digits=11, decimal_places=8)
    dec = models.DecimalField(max_digits=11, decimal_places=8)
    observations_number = models.IntegerField(default=0, null=True, blank=True)
    magnitude = models.DecimalField(max_digits=5, decimal_places=3)
    importance = models.IntegerField(default=0)
    days_from_last_observations = models.IntegerField(default=0, null=True, blank=True)
    cadence = models.IntegerField(default=1)
    priority = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        ordering = ('name',)