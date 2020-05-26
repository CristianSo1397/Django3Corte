from django.urls import path
from enemigos.views import ListarEnemigos, InsertarEnemigo, EditarEnemigo, BorrarEnemigo

urlpatterns=[
    path('enemigos', ListarEnemigos.as_view(), name='enemigos_list'),
    path('enemigos/new', InsertarEnemigo.as_view(), name='insertar_enemigo'),
    path('enemigos/edit<int:pk>', EditarEnemigo.as_view(), name='editar_enemigo'),
    path('enemigos/delete<int:pk>', BorrarEnemigo.as_view(), name='borrar_enemigo'),
]