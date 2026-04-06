from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fiestas/', include('apps.fiestas.urls')),
    path('invitados/', include('apps.invitados.urls')),
    path('localizacion/', include('apps.localizacion.urls')),
    path('', RedirectView.as_view(url='/fiestas/', permanent=False)),
]
