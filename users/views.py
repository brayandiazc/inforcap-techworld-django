from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        date_of_birth = request.POST.get("date_of_birth", None)
        city = request.POST.get("city", None)
        role = request.POST.get("role", "student")

        User.objects.create(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            city=city,
            role=role,
        )
        return redirect("login")

    return render(request, "users/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # Guardamos el usuario autenticado en la sesión.
                request.session["user_id"] = user.id
                return redirect("home")  # Página de inicio
            else:
                return render(
                    request, "users/login.html", {"error": "Contraseña incorrecta"}
                )
        except User.DoesNotExist:
            return render(
                request, "users/login.html", {"error": "Usuario no encontrado"}
            )

    return render(request, "users/login.html")
