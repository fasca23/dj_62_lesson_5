from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor,on_delete=models.CASCADE)
    temperature= models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.temperature