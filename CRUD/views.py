from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.utils.translation import gettext_lazy as _
from .models import Contacto

# Create your views here.

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'El nombre de usuario debe ser menor a 150 caracteres y no puede contener caracteres especiales'
        self.fields['password1'].help_text = 'La contraseña debe tener al menos 3 caracteres'
        self.fields['password2'].help_text = 'La contraseña debe tener al menos 3 caracteres'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CRUD:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'autenticacion/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'autenticacion/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('CRUD:login')


@login_required(login_url='CRUD:login')
def index(request):
    contactos = Contacto.objects.all()
    return render(request, 'index.html', {'contactos': contactos})

@login_required(login_url='CRUD:login')
def guardar_contacto(request):
    nombre = request.POST['txtnombre']
    apellido = request.POST['txtapellido']
    telefono = request.POST['txttelefono']
    correo = request.POST['txtcorreo']
    direccion = request.POST['txtdireccion']
    contacto = Contacto(nombre=nombre, apellido=apellido, telefono=telefono, correo=correo, direccion=direccion)
    contacto.save()
    return redirect('/')

@login_required(login_url='CRUD:login')
def eliminar_contacto(request, id):
    contacto = Contacto.objects.get(pk=id)
    contacto.delete()
    return redirect('/')

@login_required(login_url='CRUD:login')
def editar_contacto(request, id):
    contactoseleccionado = Contacto.objects.get(pk=id)
    contactos = Contacto.objects.all()
    context = {'contactos': contactos, 'contactoseleccionado': contactoseleccionado}
    return render(request, 'editar_contacto.html', context)

@login_required(login_url='CRUD:login')
def actualizar_contacto(request):
    nombre = request.POST['txtnombre']
    apellido = request.POST['txtapellido']
    telefono = request.POST['txttelefono']
    correo = request.POST['txtcorreo']
    direccion = request.POST['txtdireccion']

    contacto = Contacto.objects.get(pk=request.POST['id'])
    contacto.nombre = nombre
    contacto.apellido = apellido
    contacto.telefono = telefono
    contacto.correo = correo
    contacto.direccion = direccion
    contacto.save()
    return redirect('/')