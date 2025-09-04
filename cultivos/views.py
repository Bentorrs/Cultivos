from django.shortcuts import render

def listar_cultivos(request):
    cultivos_originales = [
        {'nombre': 'Tomate', 'tipo': 'fruto'},
        {'nombre': 'Lechuga', 'tipo': 'hoja'},
        {'nombre': 'Albahaca', 'tipo': 'hoja'},
        {'nombre': 'Zanahoria', 'tipo': 'raiz'},
        {'nombre': 'Cilantro', 'tipo': 'hoja'},
        {'nombre': 'Pimiento', 'tipo': 'fruto'},
    ]

    termino = request.GET.get('buscar', '')
    tipo = request.GET.get('tipo', '')
    cultivo_filtrados = cultivos_originales
    if termino:
        cultivo_filtrados = [c for c in cultivo_filtrados if termino.lower() in c['nombre'].lower()]
    if tipo:
        cultivo_filtrados = [c for c in cultivo_filtrados if c['tipo'] == tipo]

    contexto = {
        'titulo':'Mi huerto',
        'mensaje':'Filtra los cultivos por nombre y tipo',
        'cultivos': cultivo_filtrados,
    }
    return render(request, 'cultivos/lista_cultivos.html', contexto)

def detalle_cultivo(request, nombre):
    cultivos = {
        'Tomate': {
            'tipo':'fruto',
            'descripcion':'Requiere sol directo y riego moderado, muy sensible al frío',
            'siembra':'Agosto - Octubre',
            'cosecha':'Noviembre - Enero'
        },
        'Lechuga': {
            'tipo':'hoja',
            'descripcion':'Preferentemente sombra y suelo humedo',
            'siembra':'Marzo - Mayo',
            'cosecha':'60 días depués de sembrado'
        },
        'Albahaca': {
            'tipo':'hoja',
            'descripcion':'Prefiere climas cálidos, no tolerancia a las heladas',
            'siembra':'Septiembre - Noviembre',
            'cosecha':'40 días después de la siembra'
        },
        'Zanahoria': {
            'tipo':'raiz',
            'descripcion':'Requiere sol directo y riego moderado, muy sensible al frío',
            'siembra':'Agosto - Octubre',
            'cosecha':'Noviembre - Enero'
        },
        'Cilantro': {
            'tipo':'hoja',
            'descripcion':'Requiere sol directo y riego moderado, muy sensible al frío',
            'siembra':'Agosto - Octubre',
            'cosecha':'Noviembre - Enero'
        },
        'Pimiento': {
            'tipo':'fruto',
            'descripcion':'Requiere sol directo y riego moderado, muy sensible al frío',
            'siembra':'Agosto - Octubre',
            'cosecha':'Noviembre - Enero'
        },
    }
    cultivos = cultivos.get(nombre)
    if not cultivos:
        return render(request, 'cultivos/no_encontrado.html', {'nombre':nombre})
    contexto = {
        'nombre':nombre,
        'tipo':cultivos['tipo'],
        'descripcion':cultivos['descripcion'],
        'siembra':cultivos['siembra'],
        'cosecha':cultivos['cosecha'],
    }
    return render(request, 'cultivos/detalle.html', contexto)

def recomendar_cultivos(request, estacion):
    estaciones = {
        'Verano': {
            'cultivo': 'Albahaca',
            'recomendacion': 'ejemplo'
        },
        'Otonno': {
            'cultivo': 'Zanahora',
            'recomendacion': 'ejemplo'
        },
        'Invierno': {
            'cultivo': 'Pimiento',
            'recomendacion': 'ejemplo'
        },
        'Primavera': {
            'cultivo': 'Tomate',
            'recomendacion': 'ejemplo'
        },
    }

    
    estaciones = estaciones.get(estacion)
    if not estaciones:
        return render(request, 'cultivos/no_encontrado.html', {'estaciones':estacion})
    contexto = {
        'estacion':estacion,
        'cultivo':estaciones['cultivo'],
        'recomendacion':estaciones['recomendacion']
    }
    return render(request, 'cultivos/recomendar.html', contexto)

def consejo_diario():
    pass

def evaluar_riego():
    pass

def calculadora_espacio():
    pass