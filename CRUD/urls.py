from django.urls import path
from . import views

app_name = 'CRUD'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout_view, name='logout_view'),
    path('', views.index, name='index'),
    path('guardar_contacto', views.guardar_contacto, name='guardar'),
    path('eliminar_contacto/<id>', views.eliminar_contacto, name='eliminar'),
    path('editar_contacto/<id>', views.editar_contacto, name='editar'),
    path('actualizar_contacto', views.actualizar_contacto, name='actualizar'),
]