from django.shortcuts import render
from  enemigos.models import Enemigo
from django.views import generic
from enemigos.forms import EnemigoForm
from django.urls import reverse_lazy

# Create your views here.
class ListarEnemigos(generic.ListView):
    model=Enemigo
    template_name="enemigos/listar_enemigos.html"
    context_object_name="obj"
class InsertarEnemigo(generic.CreateView):
    model=Enemigo
    template_name="enemigos/insertar_enemigo.html"
    context_object_name="obj"
    form_class=EnemigoForm
    success_url=reverse_lazy("enemigos:enemigos_list")
class EditarEnemigo(generic.UpdateView):
    model=Enemigo
    template_name="enemigos/editar_enemigo.html"
    context_object_name="obj"
    form_class=EnemigoForm
    success_url=reverse_lazy("enemigos:enemigos_list")
class BorrarEnemigo(generic.DeleteView):
    model=Enemigo
    template_name="enemigos/borrar_enemigo.html"
    context_object_name="obj"
    form_class=EnemigoForm
    success_url=reverse_lazy("enemigos:enemigos_list")


