from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from apps.fiestas.business import FiestaService


def home(request):
    """Vista principal del frontend de localización de fiestas."""
    fiestas = FiestaService.listar_todas()
    fiestas_con_coords = [f for f in fiestas if f.latitud and f.longitud]
    fiestas_sin_coords = [f for f in fiestas if not f.latitud or not f.longitud]
    return render(request, 'localizacion/home.html', {
        'fiestas': fiestas,
        'fiestas_con_coords': fiestas_con_coords,
        'fiestas_sin_coords': fiestas_sin_coords,
    })


@require_http_methods(["GET"])
def detalle(request, fiesta_id):
    try:
        fiesta = FiestaService.obtener_fiesta(fiesta_id)
    except ValueError as e:
        return render(request, 'localizacion/error.html', {'mensaje': str(e)}, status=404)
    return render(request, 'localizacion/detalle.html', {'fiesta': fiesta})
