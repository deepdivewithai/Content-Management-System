from . import views
from django.urls import path

app_name = 'product'

urlpatterns = [
    path('', views.home, name='home')
]