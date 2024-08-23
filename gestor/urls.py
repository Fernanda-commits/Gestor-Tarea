from django.urls import path
from .views import *

urlpatterns = [
    path('',listar,name='listar'),
    path('crear',crear,name='crear')
]
