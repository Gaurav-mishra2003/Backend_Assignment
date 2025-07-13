# forms/urls.py
from django.urls import path
from .views import WheelSpecificationCreateView

urlpatterns = [
    path('api/wheel-specifications', WheelSpecificationCreateView.as_view()),

]
