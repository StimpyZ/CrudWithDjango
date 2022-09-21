import re
from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.
def home(request):
    empleadosListados = Empleado.objects.all()
    return render(request, "gestionEmpleado.html", {"empleados": empleadosListados} )

def registrarEmpleados(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    telefono = request.POST['txtTelefono']
    correo = request.POST['txtCorreo']
    
    empleado = Empleado.objects.create(codigo=codigo, nombre=nombre, telefono=telefono, correo=correo)
    return redirect('/')

def eliminarEmpleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    empleado.delete()
    return redirect('/')
    
def edicionEmpleados(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    telefono = request.POST['txtTelefono']
    correo = request.POST['txtCorreo']
    
    empleado = Empleado.objects.get(codigo=codigo)
    empleado.nombre = nombre
    empleado.telefono = telefono
    empleado.correo = correo
    empleado.save()
    return redirect('/')

def editarEmpleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    return render(request, "editarEmpleado.html", {"empleado": empleado})