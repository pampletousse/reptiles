from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('create/',views.create,name='create'),
    path('delete/<int:pk>',views.liste,name='delete'),
    path('liste/',views.liste,name='liste'),
    path('detail/<int:pk>',views.detail,name='detail'),
]
