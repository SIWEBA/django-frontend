from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "dashboard/inicio.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("panel")
    else:
        form = AuthenticationForm()
    return render(request, "dashboard/login.html", {"form": form})

def registro_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("panel")
    else:
        form = UserCreationForm()
    return render(request, "dashboard/registro.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("inicio")

@login_required(login_url="login")
def panel_usuario(request):
    return render(request, "dashboard/panel.html")