import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from apps.fiestas.business import FiestaService


@require_http_methods(["GET", "POST"])
def fiestas_list(request):
    """
    GET  /fiestas/     → lista todas las fiestas (HTML o JSON)
    POST /fiestas/     → crea una nueva fiesta
    """
    if request.method == 'GET':
        accept = request.headers.get('Accept', '')
        fiestas = FiestaService.listar_todas()

        if 'application/json' in accept:
            data = [
                {
                    'id': f.id,
                    'nombre': f.nombre,
                    'descripcion': f.descripcion,
                    'direccion': f.direccion,
                    'latitud': float(f.latitud) if f.latitud else None,
                    'longitud': float(f.longitud) if f.longitud else None,
                    'capacidad': f.capacidad,
                    'invitados_confirmados': f.invitados_confirmados,
                    'cupos_disponibles': f.cupos_disponibles,
                    'fecha_hora': f.fecha_hora.isoformat(),
                    'estado': f.estado,
                    'codigo_acceso': f.codigo_acceso,
                }
                for f in fiestas
            ]
            return JsonResponse({'fiestas': data})

        return render(request, 'fiestas/lista.html', {'fiestas': fiestas})

    # POST — crear fiesta
    if request.content_type == 'application/json':
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)
    else:
        body = request.POST

    try:
        fiesta = FiestaService.crear_fiesta(
            nombre=body.get('nombre', ''),
            descripcion=body.get('descripcion', ''),
            direccion=body.get('direccion', ''),
            capacidad=body.get('capacidad', 0),
            fecha_hora_str=body.get('fecha_hora', ''),
            latitud=body.get('latitud') or None,
            longitud=body.get('longitud') or None,
        )
    except ValueError as e:
        if request.content_type == 'application/json':
            return JsonResponse({'error': str(e)}, status=400)
        fiestas = FiestaService.listar_todas()
        return render(request, 'fiestas/lista.html', {
            'fiestas': fiestas,
            'error': str(e),
            'form_data': body,
        }, status=400)

    if request.content_type == 'application/json':
        return JsonResponse({
            'id': fiesta.id,
            'nombre': fiesta.nombre,
            'codigo_acceso': fiesta.codigo_acceso,
            'mensaje': 'Fiesta creada exitosamente.',
        }, status=201)

    return redirect('/fiestas/')


def fiesta_detail(request, fiesta_id):
    try:
        fiesta = FiestaService.obtener_fiesta(fiesta_id)
    except ValueError as e:
        return render(request, 'fiestas/error.html', {'mensaje': str(e)}, status=404)
    return render(request, 'fiestas/detalle.html', {'fiesta': fiesta})
