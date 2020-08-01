from rest_framework import serializers
from .models import Target

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['name', 'ra', 'dec', 'observations_number', 'magnitude', 'importance',
                  'days_from_last_observations', 'cadence', 'priority']





# class Target(serializers.Serializer):
#     name = models.CharField(max_length=54)
#     ra = models.DecimalField(max_digits=11, decimal_places=8)
#     dec = models.DecimalField(max_digits=11, decimal_places=8)
#     obervations_number = models.IntegerField(default=0, null=True, blank=True)
#     magnitude = models.DecimalField(max_digits=5, decimal_places=3)
#     importance = models.IntegerField(default=0)
#     days_from_last_observations = models.IntegerField(default=0, null=True, blank=True)
#     cadence = models.IntegerField(default=1)
#     priority = models.DecimalField(max_digits=5, decimal_places=1)

#     def create(self, validated_data):
#         return Target.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         name = validated_data.get('name', instance.name)
#         ra = validated_data.get('ra', instance.ra)
#         dec = validated_data.get('dec', instance.dec)
#         obervations_number = validated_data.get('observations_number', instance.obervations_number)
#         magnitude = validated_data.get('magnitude', instance.magnitude)
#         importance = validated_data.get('importance', instance.importance)
#         days_from_last_observations = validated_data.get(
#             'days_from_last_observations', instance.days_from_last_observations
#             )
#         cadence = validated_data.get('cadence', instance.cadence)
#         priority = validated_data.get('priority', instance.priority)

#         instance.save()
#         return instance