from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('create/',views.create,name='create'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('update/<int:pk>',views.update,name='update'),
    path('liste/',views.liste,name='liste'),
    path('detail/<int:pk>',views.detail,name='detail'),
    path('connexion/',views.connexion,name='connexion'),
]
