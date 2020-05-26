from django.urls import path
from salvados.views import ListarSalvados, InsertarSalvado, EditarSalvado, BorrarSalvado

urlpatterns=[
    path('salvados', ListarSalvados.as_view(), name='salvados_list'),
    path('salvados/new', InsertarSalvado.as_view(), name='insertar_salvado'),
    path('salvados/edit<int:pk>', EditarSalvado.as_view(), name='editar_salvado'),
    path('salvados/delete<int:pk>', BorrarSalvado.as_view(), name='borrar_salvado'),

]