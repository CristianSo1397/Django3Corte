from django.shortcuts import render
from aliados.models import Aliado
from django.views import generic
from aliados.forms import AliadoForm
from django.urls import reverse_lazy
# Create your views here.
class ListarAliados(generic.ListView):
    model=Aliado
    template_name="aliados/listar_aliados.html"
    context_object_name="obj"
class InsertarAliado(generic.CreateView):
    model=Aliado
    template_name="aliados/insertar_aliado.html"
    context_object_name="obj"
    form_class=AliadoForm
    success_url=reverse_lazy("aliados:aliados_list")
class EditarAliado(generic.UpdateView):
    model=Aliado
    template_name="aliados/insertar_aliado.html"
    context_object_name="obj"
    form_class=AliadoForm
    success_url=reverse_lazy("aliados:aliados_list")
class BorrarAliado(generic.DeleteView):
    model=Aliado
    template_name="aliados/borrar_aliado.html"
    context_object_name="obj"
    form_class=AliadoForm
    success_url=reverse_lazy("aliados:aliados_list")

