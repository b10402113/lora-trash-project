
from django.urls import path
from lora_garbage_app import views
urlpatterns = [
    path('', views.index),
    path('/<str:location>', views.index),
    path('overview', views.overview),
    path('event', views.event),
    path('trash_detail/<int:trash_id>', views.trash_detail),
    path('api/post_trash_data/',views.post_trash_data,name='api-data'),
    path('trash_ajax_data/<int:trash_id>',views.trash_ajax_data,name='trash_ajax_data'),
    path('api/path_generate/', views.path_generate),
    path('profile', views.profile),
    # 產生的圖片
    path('display_image/', views.display_image),

]
