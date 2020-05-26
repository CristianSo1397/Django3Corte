from django.urls import path
from aliados.views import ListarAliados, InsertarAliado, EditarAliado, BorrarAliado

urlpatterns=[
    path('aliados', ListarAliados.as_view(), name='aliados_list'),
    path('aliados/new', InsertarAliado.as_view(), name='insertar_aliado'),
    path('aliados/edit<int:pk>', EditarAliado.as_view(), name='editar_aliado'),
    path('aliados/delete<int:pk>', BorrarAliado.as_view(), name='borrar_aliado'),
]