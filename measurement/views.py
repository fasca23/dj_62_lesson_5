# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, CreateAPIView
# from rest_framework.generics import RetrieveAPIView

from measurement.models import Sensor, Measurement
from .serializers import SensorSerializers, MeasurementSerializer
from django.forms import model_to_dict


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class SensorView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers







