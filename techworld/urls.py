from django.contrib import admin
from django.urls import path, include
from courses import views as course_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # La raíz del sitio muestra el listado de cursos y actúa como "home".
    path("", course_views.course_list, name="home"),
    path("courses/", include("courses.urls")),
    path("users/", include("users.urls")),
]
