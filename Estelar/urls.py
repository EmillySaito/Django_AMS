from django.urls import path
from Estelar.views import index

urlpatterns = [
path('', index, name='index')
]