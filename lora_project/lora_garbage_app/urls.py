
from django.urls import path
from lora_garbage_app import views
urlpatterns = [
    path('', views.index),
    path('overview', views.overview),
    path('trash_detail/<int:trash_id>', views.trash_detail),
]
