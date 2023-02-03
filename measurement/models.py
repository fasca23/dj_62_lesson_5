from django.db import models

from django.forms.fields import ImageField

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.description}'

class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor,on_delete=models.CASCADE, related_name='measurements')
    temperature= models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    # image = ImageField(max_length=100, allow_empty_file=False)
    photo = models.ImageField(upload_to='image', null=True)

    def __str__(self):
        return f'{self.id_sensor} - {self.temperature} - {self.created_at}'