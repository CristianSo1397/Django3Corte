from django.shortcuts import render
from patrocinadores.models import Patrocinador
from django.views import generic 
from patrocinadores.forms import PatrocinadorForm
from django.urls import reverse_lazy
# Create your views here.
class ListarPatrocinadores(generic.ListView):
    model=Patrocinador
    template_name="patrocinadores/listar_patrocinadores.html"
    context_object_name="obj"
class InsertarPatrocinador(generic.CreateView):
    model=Patrocinador
    template_name="patrocinadores/insertar_patrocinador.html"
    context_object_name="obj"
    form_class=PatrocinadorForm
    success_url=reverse_lazy("patrocinadores:patrocinadores_list")
class EditarPatrocinador(generic.UpdateView):
    model=Patrocinador
    template_name="patrocinadores/insertar_patrocinador.html"
    context_object_name="obj"
    form_class=PatrocinadorForm
    success_url=reverse_lazy("patrocinadores:patrocinadores_list")
class BorrarPatrocinador(generic.DeleteView):
    model=Patrocinador
    template_name="patrocinadores/borrar_patrocinador.html"
    context_object_name="obj"
    form_class=PatrocinadorForm
    success_url=reverse_lazy("patrocinadores:patrocinadores_list")
    
