from django.shortcuts import render, redirect
from .models import ObjetoPerdido
from .forms import ObjetoForm
from .serializers import ObjetoPerdidoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def objetos(request):
    objetos = ObjetoPerdido.objects.all().order_by('-fecha_hallazgo')
    contexto = {
        'objetos': objetos,
        'cantidad_objetos': objetos.count(),
        'ultimo_objeto': objetos.first(),
    }
    return render(request, 'objetos/index.html', contexto)

def detalle(request, id):
    objeto = ObjetoPerdido.objects.get(id=id)
    return render(request, 'objetos/detalle.html', {'objeto': objeto})

def crear(request):
    formulario = ObjetoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('objetos')
    return render(request, 'objetos/crear.html', {'formulario': formulario})

def editar(request, id):
    objeto = ObjetoPerdido.objects.get(id=id)
    formulario = ObjetoForm(request.POST or None, request.FILES or None, instance=objeto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('objetos')
    return render(request, 'objetos/editar.html', {'formulario': formulario, 'objeto': objeto})

def eliminar(request, id):
    objeto = ObjetoPerdido.objects.get(id=id)
    if request.method == 'POST':
        objeto.delete()
        return redirect('objetos')
    return render(request, 'objetos/eliminar.html', {'objeto': objeto})

@api_view(['GET', 'POST'])
def objeto_list(request):
    if request.method == 'GET':
        objetos = ObjetoPerdido.objects.all()
        serializer = ObjetoPerdidoSerializer(objetos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ObjetoPerdidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def objeto_detail(request, pk):
    try:
        objeto = ObjetoPerdido.objects.get(pk=pk)
    except ObjetoPerdido.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ObjetoPerdidoSerializer(objeto)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ObjetoPerdidoSerializer(objeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        objeto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
