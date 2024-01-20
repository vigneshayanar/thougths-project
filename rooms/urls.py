from django.urls import path

from . import views

urlpatterns=[
    path('',views.rooms,name='rooms'),
    path('join/<str:pk>',views.join,name='join')
]