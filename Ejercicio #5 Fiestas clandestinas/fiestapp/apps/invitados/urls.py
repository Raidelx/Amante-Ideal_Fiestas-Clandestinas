from django.urls import path
from . import views

app_name = 'invitados'

urlpatterns = [
    path('', views.home, name='home'),
    path('solicitar/<int:fiesta_id>/', views.solicitar_ingreso, name='solicitar'),
    path('gestionar/<int:fiesta_id>/', views.gestionar_invitados, name='gestionar'),
    path('confirmar/<int:invitado_id>/', views.confirmar_invitado, name='confirmar'),
    path('rechazar/<int:invitado_id>/', views.rechazar_invitado, name='rechazar'),
]
