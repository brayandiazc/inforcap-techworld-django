from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Inscription
from users.models import User


# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})


def create_course(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        duration = request.POST["duration"]

        Course.objects.create(title=title, description=description, duration=duration)
        return redirect("course_list")

    return render(request, "courses/create_course.html")


def enroll_course(request, course_id):
    if request.method == "POST":
        course = get_object_or_404(Course, id=course_id)

        # El usuario autenticado se obtiene de la sesión (modelo propio users.User).
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("login")
        user = get_object_or_404(User, id=user_id)

        # Verifica si ya está inscrito
        if Inscription.objects.filter(user=user, course=course).exists():
            return render(
                request,
                "courses/course_list.html",
                {
                    "courses": Course.objects.all(),
                    "error": "Ya estás inscrito en este curso.",
                },
            )

        Inscription.objects.create(user=user, course=course)
        return redirect("course_list")
