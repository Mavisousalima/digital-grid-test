from django.urls import path
from .views import calculate_savings

urlpatterns = [
    path("", calculate_savings, name="calculate_savings"),
]
