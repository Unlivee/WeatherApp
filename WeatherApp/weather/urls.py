from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('qwerty', views.about, name='about'),
    path('<int:pk>', views.delete, name='delete'),
]
