# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView 
from rest_framework.generics import RetrieveAPIView

from measurement.models import Sensor, Measurement
from .serializers import SensorSerializers
from django.forms import model_to_dict

# @api_view(['GET'])
# def measurement(request):
#     sensors = Sensor.objects.all()
#     ser = SensorSerializers(sensors, many=True)
#     return Response(ser.data)

# class MeasurementView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         ser = SensorSerializers(sensors, many=True)
#         return Response(ser.data)

#     def post(self, request):
#         return Response({'status': 'ok'})

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

    # def post(self, request):
    #     post_new = Sensor.objects.create(
    #         name=request.data['name'],
    #         description=request.data['description']
    #     )
    #     return Response({'post': model_to_dict(post_new)})

    # def patch(self, request):
    #     patch_new = Sensor.objects.update(
    #         name=request.data['name'],
    #         description=request.data['description']
    #     )
    #     return Response({'patch': model_to_dict(patch_new)})

# class SensorView(UpdateAPIView):


class SensorsView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers







