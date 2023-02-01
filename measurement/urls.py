from django.urls import path
from .views import SensorsView, MeasurementView, SensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
