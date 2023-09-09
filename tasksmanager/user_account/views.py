from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from tasks.models import Task

# Create your views here.
def signin(request):
    error = False
    message = ""
    if request.method == "POST":
        print("=="*5, " new post ", "=="*5)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            data =username
            return redirect('tasks')
        else:
            error = True
            message = "Le nom d'utilisateur ou le mot de passe est incorrect!"
        print("username : ", username, "Password : ", password)
    context = {
            "error": error,
            "message": message
        }
    return render(request, 'user_account/login.html', context)

def signup(request):
    error = False
    message = ""
    if request.method == "POST":
        print("=="*5, " new post ", "=="*5)
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        repeat_password = request.POST.get("repeat_password", None)
        try: 
            validate_email(email)
        except:
            error = True
            message = "Email incorrecte !"
        if not error:
            if password != repeat_password :
                error = True
                message = "Les mots de passe ne correspondent pas"
        if error == False:
            user = User.objects.filter(Q(email=email) | Q(username=username)).first()
            if user:
                error = True
                message = f"Un utilisateur avec cet email {email} ou avec ce nom d'ulisateur {username} existe deja"
        if error == False:
            user = User(
                username= username,
                email = email
            )
            user.save()
            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('signin')

    context = {
            "error": error,
            "message": message
        }
    return render(request, 'user_account/register.html', context)
@login_required(login_url='signin')
def tasks(request):
    tasks = Task.objects.all()
    context = {"tasks":tasks}
    
    return render(request, 'tasks/tables.html', context)

def signout(request):
    return render(request, 'user_account/logout.html', {})