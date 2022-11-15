from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('test/', test),
    path('test_1/', first_test),
]