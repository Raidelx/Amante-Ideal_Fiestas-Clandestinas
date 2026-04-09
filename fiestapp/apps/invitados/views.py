from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from apps.fiestas.business import FiestaService, InvitadoService


def home(request):
    """Vista principal del frontend de invitados."""
    fiestas = FiestaService.listar_fiestas_disponibles()
    return render(request, 'invitados/home.html', {'fiestas': fiestas})


@require_http_methods(["GET", "POST"])
def solicitar_ingreso(request, fiesta_id):
    """Formulario para solicitar ingreso a una fiesta."""
    try:
        fiesta = FiestaService.obtener_fiesta(fiesta_id)
    except ValueError as e:
        return render(request, 'invitados/error.html', {'mensaje': str(e)}, status=404)

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        alias = request.POST.get('alias', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        try:
            invitado, mensaje = InvitadoService.solicitar_ingreso(fiesta_id, nombre, alias, telefono)
            return render(request, 'invitados/confirmacion.html', {
                'invitado': invitado,
                'fiesta': fiesta,
                'mensaje': mensaje,
            })
        except ValueError as e:
            return render(request, 'invitados/solicitar.html', {
                'fiesta': fiesta,
                'error': str(e),
                'form_data': {'nombre': nombre, 'alias': alias, 'telefono': telefono},
            })

    return render(request, 'invitados/solicitar.html', {'fiesta': fiesta})


@require_http_methods(["GET"])
def gestionar_invitados(request, fiesta_id):
    """Vista para el organizador: ver y gestionar lista de invitados."""
    try:
        invitados, fiesta = InvitadoService.listar_invitados(fiesta_id)
    except ValueError as e:
        return render(request, 'invitados/error.html', {'mensaje': str(e)}, status=404)
    return render(request, 'invitados/gestionar.html', {
        'fiesta': fiesta,
        'invitados': invitados,
    })


@require_http_methods(["POST"])
def confirmar_invitado(request, invitado_id):
    try:
        InvitadoService.confirmar_invitado(invitado_id)
    except ValueError as e:
        return render(request, 'invitados/error.html', {'mensaje': str(e)}, status=400)
    fiesta_id = request.POST.get('fiesta_id')
    return redirect(f'/invitados/gestionar/{fiesta_id}/')


@require_http_methods(["POST"])
def rechazar_invitado(request, invitado_id):
    try:
        InvitadoService.rechazar_invitado(invitado_id)
    except ValueError as e:
        return render(request, 'invitados/error.html', {'mensaje': str(e)}, status=400)
    fiesta_id = request.POST.get('fiesta_id')
    return redirect(f'/invitados/gestionar/{fiesta_id}/')
