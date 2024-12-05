from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),  
    path('nuevo/', views.crear_cliente, name='crear_cliente'), 
    path('<int:pk>/editar/', views.actualizar_cliente, name='actualizar_cliente'),  
    path('<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),  
]
