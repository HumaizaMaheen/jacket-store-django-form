from django.urls import path
from . import views

urlpatterns = [
    path('', views.addJacket),
    path('show/', views.showAll),
    path('delete', views.delete),
    path('update', views.update),
]