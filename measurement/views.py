# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.viewsets import ModelViewSet

from measurement.models import Sensor, Measurement
from .serializers import SensorSerializers, MeasurementSerializer,SensorsSerializers
from django.forms import model_to_dict

class MeasurementView(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    http_method_names = ['get', 'post']

class SensorView(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

class SensorsView(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializers







