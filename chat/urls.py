from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('chat/' , views.chatpage, name='chatpage'),
	path('login/' , views.login , name='login'),
	path('create_user/', views.CreateUser , name='createUser'),
	path('username/' , views.Home ,name='userhome'),
	path('chat_create/', views.CreateChat , name='CreateChat'),
]
