from django.shortcuts import render
from .models import ChatMessage  # If you plan to save chat history to a model
import os
def index(request):
    if request.method == "GET":
        return render(request, 'chat/index.html')

def login(request):
    if request.method == "GET":
        return render(request, 'chat/loginPage.html')
    

def CreateUser(request):
    if request.method == "GET":
        return render(request, 'chat/createUser.html')
    

def Home(request):
    if request.method == "GET":
        return render(request, 'chat/userHome.html')


def CreateChat(request):
    if request.method == "GET":
        return render(request, 'chat/CreateChat.html')
def chatpage(request):
    
    chat_history = ChatMessage.objects.all().order_by("-timestamp")[:10]   # Get all previous chat messages from the DB
    if request.method == "POST":
        user_input = request.POST.get('prompt')
        
        # Placeholder for AI logic (replace with real backend call)
        ai_response = f"Potato AI says: You asked: {user_input}"

        # Optionally save the conversation to a DB
        ChatMessage.objects.create(user_input=user_input, ai_response=ai_response)

        return render(request, 'chat/chatPage.html', {'chat_history': chat_history, 'user_input': user_input, 'ai_response': ai_response})

    return render(request, 'chat/chatPage.html', {'chat_history': chat_history})


