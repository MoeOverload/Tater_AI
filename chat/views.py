from django.shortcuts import render,redirect
from .models import ChatMessage  # If you plan to save chat history to a model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os

def index(request):
    return render(request, 'chat/index.html')

def login_View(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('userhome', username=user.username)  # Redirect to the logged-in user's home page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'chat/loginPage.html')


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect('index')



def CreateUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'chat/createUser.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'chat/createUser.html', {'error': 'Username already taken'})

        if User.objects.filter(email=email).exists():
            return render(request, 'chat/createUser.html', {'error': 'Email already used'})

        user = User.objects.create_user(username=username, password=password1, email=email)
        login(request, user)  # Auto login after registration
        return redirect('userhome', username=user.username)

    return render(request, 'chat/createUser.html')

    
@login_required
def Home(request, username):
    user = get_object_or_404(User, username=username)
    if request.user != user:
        messages.error(request, "You can't view someone else's home page.")

    
    return render(request, 'chat/userHome.html')


def CreateChat(request):
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


