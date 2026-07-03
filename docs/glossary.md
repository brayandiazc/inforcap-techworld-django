# Glosario

Vocabulario compartido del dominio y del proyecto. Mantén las definiciones cortas
y sin ambigüedad para que todo el equipo use los términos de la misma forma.

| Término        | Definición                                                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Curso          | Contenido formativo que ofrece la plataforma. Modelo `Course` con título, descripción y duración en horas.                            |
| Django ORM     | Capa de mapeo objeto-relacional de Django que traduce clases de modelo a tablas y permite consultar la base de datos con Python.      |
| Estudiante     | Rol de usuario (`role="student"`) que se inscribe en cursos y sigue su progreso. Es el valor por defecto al registrarse.              |
| Fixture        | Archivo JSON con datos iniciales que se carga con `python manage.py loaddata` para poblar la base de datos.                           |
| Inscripción    | Relación entre un usuario y un curso. Modelo `Inscription` (tabla intermedia) con `progress` y `unique_together` para evitar duplicados. |
| Instructor     | Rol de usuario (`role="instructor"`) asociado a la creación de cursos.                                                                |
| Migración      | Archivo generado por Django que versiona los cambios del esquema de la base de datos (`makemigrations` / `migrate`).                 |
| MTV            | Patrón Modelo-Template-Vista de Django: separa datos (Modelo), presentación (Template) y lógica de la petición (Vista).              |
| PostgreSQL     | Sistema de base de datos relacional usado por el proyecto (motor `django.db.backends.postgresql`).                                   |
| Progreso       | Porcentaje de avance de un estudiante en un curso. Campo `progress` (entero, por defecto 0) del modelo `Inscription`.                |
| Usuario        | Persona registrada en la plataforma. Modelo propio `User` (no extiende `AbstractUser`) con username, email, contraseña y rol.        |

> Convención: ordena los términos alfabéticamente y enlaza al documento donde se
> detalla cada concepto cuando aplique.
