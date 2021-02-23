from django.db import models
from django.apps import apps


class Target(models.Model):
    group = models.ForeignKey('TargetGroup', on_delete=models.CASCADE,
        blank=True, null=True)
    name = models.CharField(max_length=54, unique=True)
    ra = models.DecimalField(max_digits=11, decimal_places=8)
    dec = models.DecimalField(max_digits=11, decimal_places=8)
    p = models.DecimalField(max_digits=15, decimal_places=12, null=True, blank=True)
    m0 = models.DecimalField(max_digits=16, decimal_places=8, null=True, blank=True, default=1)
    eclipse_duration = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    magnitude = models.DecimalField(max_digits=5, decimal_places=3)
    cadence = models.IntegerField(default=1)
    priority = models.DecimalField(max_digits=5, decimal_places=1)
    note = models.CharField(max_length=34, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.group:
            group, _ = apps.get_model(
                'targets.targetgroup').objects.get_or_create(name='main')
            self.group = group
        
        return super().save(*args, **kwargs)
        

class TargetGroup(models.Model):
    name = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.name