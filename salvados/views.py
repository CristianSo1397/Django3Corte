from django.shortcuts import render
from salvados.models import Salvado
from django.views import generic
from salvados.forms import SalvadoForm
from django.urls import reverse_lazy

class ListarSalvados(generic.ListView):
    model=Salvado
    template_name="salvados/listar_salvados.html"
    context_object_name="obj"
class InsertarSalvado(generic.CreateView):
    model=Salvado
    template_name="salvados/insertar_salvado.html"
    context_object_name="obj"
    form_class=SalvadoForm
    success_url=reverse_lazy("salvados:salvados_list")
class EditarSalvado(generic.UpdateView):
    model=Salvado
    template_name="salvados/insertar_salvado.html"
    context_object_name="obj"
    form_class=SalvadoForm
    success_url=reverse_lazy("salvados:salvados_list")
class BorrarSalvado(generic.DeleteView):
    model=Salvado
    template_name="salvados/borrar_salvado.html"
    context_object_name="obj"
    form_class=SalvadoForm
    success_url=reverse_lazy("salvados:salvados_list")