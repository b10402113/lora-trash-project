
from django.urls import path
from lora_garbage_app import views
urlpatterns = [
    path('', views.index),
]
