from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.clienteList,name='cliente-list'),
    path('cliente/<int:id>', views.clienteView,name='cliente-view'),
    path('newcliente/', views.newCliente,name='cliente-new'),
    path('edit/<int:id>', views.editCliente,name='cliente-edit'),
    # path('changestatus/<int:id>', views.changeStatus,name='cliente-changestatus'),
    path('delete/<int:id>', views.deleteCliente,name='delete-edit'),
    
    

   
]
