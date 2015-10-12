from django.db import models


class Cereal(models.Model): 
    name = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.ForeignKey('Manufacturer', blank=True, null=True)
    cereal_type = models.CharField(max_length=20, blank=True, null=True)
    calories = models.IntegerField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    dietary_fiber = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    sugars = models.FloatField(null=True, blank=True)
    display_shelf = models.FloatField(null=True, blank=True)
    potassium = models.FloatField(null=True, blank=True)
    vitamins_and_minerals = models.FloatField(null=True, blank=True)
    serving_size_weight = models.FloatField(null=True, blank=True)
    cups_per_serving = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name
