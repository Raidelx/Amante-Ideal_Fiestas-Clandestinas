from django.urls import path
from . import views

app_name = 'fiestas'

urlpatterns = [
    path('', views.fiestas_list, name='lista'),
    path('<int:fiesta_id>/', views.fiesta_detail, name='detalle'),
]
