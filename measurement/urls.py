from django.urls import path
from .views import SensorView, SensorsView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorsView.as_view())
]
