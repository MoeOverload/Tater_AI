from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('chat/' , views.chatpage, name='chatpage'),
	path('login/' , views.login_View , name='login'),
	path('Logout/' , views.logout_view, name='logout'),
	path('NewUser/', views.CreateUser , name='createUser'),
	path('chat_create/', views.CreateChat , name='CreateChat'),
    path('<str:username>/' , views.Home ,name='userhome'),
]
