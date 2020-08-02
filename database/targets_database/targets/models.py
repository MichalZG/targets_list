from django.db import models

class Target(models.Model):
    group = models.ForeignKey('TargetGroup', on_delete=models.SET_DEFAULT, default='common')
    name = models.CharField(max_length=54, unique=True)
    ra = models.DecimalField(max_digits=11, decimal_places=8)
    dec = models.DecimalField(max_digits=11, decimal_places=8)
    observations_number = models.IntegerField(default=0, null=True, blank=True)
    magnitude = models.DecimalField(max_digits=5, decimal_places=3)
    days_from_last_observations = models.IntegerField(default=0, null=True, blank=True)
    cadence = models.IntegerField(default=1)
    priority = models.DecimalField(max_digits=5, decimal_places=1)
    note = models.CharField(max_length=34, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class TargetGroup(models.Model):
    name = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.name