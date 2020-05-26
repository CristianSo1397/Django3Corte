from django.urls import path
from patrocinadores.views import ListarPatrocinadores, InsertarPatrocinador, EditarPatrocinador, BorrarPatrocinador

urlpatterns =[
    path('patrocinadores', ListarPatrocinadores.as_view(), name='patrocinadores_list'),
    path('patrocinadores/new', InsertarPatrocinador.as_view(), name='insertar_patrocinador'),
    path('patrocinadores/edit<int:pk>', EditarPatrocinador.as_view(), name='editar_patrocinador'),
    path('patrocinadores/delete<int:pk>', BorrarPatrocinador.as_view(), name='borrar_patrocinador'),
]  