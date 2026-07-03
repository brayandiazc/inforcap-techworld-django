# Referencia de rutas HTTP (vistas server-rendered)

> Contrato de rutas HTTP de **TechWorld Learning Platform**.
> Documentación interactiva: **No aplica en la versión actual** (no hay OpenAPI/Swagger/Postman).
>
> **Última actualización**: 2026-07-02

## ¿API REST? No en esta versión

TechWorld Learning Platform **no expone una API REST ni devuelve JSON**. Es una aplicación
**server-rendered** construida con el patrón **MTV** (Modelo–Template–Vista) de Django: cada
ruta ejecuta una vista que renderiza una plantilla HTML o realiza un `redirect`.

Este documento describe, por tanto, el **contrato de las vistas HTTP** (rutas, métodos y
comportamiento) en lugar de endpoints de una API JSON. La exposición de una API REST/JSON
pública se contempla únicamente como **evolución futura** (ver [Posible evolución futura](#posible-evolución-futura)).

## Convenciones generales

- **URL base (desarrollo)**: `http://127.0.0.1:8000`
- **Versionado**: No aplica en la versión actual (no hay prefijo de versión en las rutas).
- **Formato**: HTML renderizado con Django Templates. **No** se responde `application/json`.
- **Enrutamiento**: `techworld/urls.py` (ROOT_URLCONF) incluye `courses.urls` bajo `/courses/`
  y `users.urls` bajo `/users/`, además del panel de administración en `/admin/`.
- **Datos de formularios**: se envían como `application/x-www-form-urlencoded` (formularios HTML
  clásicos) y se leen desde `request.POST` en las vistas.

## Autenticación de las rutas

- **No aplica un esquema de API.** No hay Bearer token ni API key.
- El acceso a las vistas de `courses/` y `users/` **no está protegido** por autenticación en la
  versión actual (ver [`auth.md`](auth.md)).
- El único acceso autenticado es el panel `/admin/`, que usa el login nativo de Django.

## Manejo de errores

No hay un formato de error JSON estándar. El manejo de errores es el propio de una app HTML:

- Errores de validación de negocio se comunican **re-renderizando la plantilla** con una variable
  de contexto `error` (p. ej. login con "Contraseña incorrecta", inscripción con "Ya estás inscrito
  en este curso.").
- Recursos inexistentes: `enroll_course` usa `get_object_or_404(Course, id=course_id)`, que
  devuelve una página **404** estándar de Django si el curso no existe.
- Errores no controlados devuelven las páginas de error por defecto de Django (500 en producción,
  traza de depuración si `DEBUG=True`).

| Código HTTP | Cuándo ocurre en esta app                                              |
| ----------- | --------------------------------------------------------------------- |
| 200         | Renderizado normal de una plantilla (GET o POST que re-renderiza).    |
| 302         | Redirecciones tras POST (`redirect` a `login`, `course_list`, etc.).  |
| 404         | Curso inexistente en `enroll_course` (`get_object_or_404`).           |
| 500         | Error interno no controlado.                                          |

> No se emiten 401/403/422/429: no hay autenticación de API, validación estructurada ni rate limiting.

## Paginación, filtrado y ordenamiento

- **No aplica en la versión actual.** El listado de cursos (`course_list`) devuelve
  `Course.objects.all()` sin paginación ni filtros. El orden de los cursos viene dado por el
  `Meta.ordering = ["-created_at"]` del modelo `Course` (más recientes primero).

## Rutas (contrato de vistas HTTP)

### Administración

```http
GET/POST  /admin/            # Panel de administración de Django (auth nativa)
```

### Usuarios (`users/urls.py`, prefijo `/users/`)

```http
GET   /users/register/       # Muestra el formulario de registro (users/register.html)
POST  /users/register/       # Crea el usuario (hash con make_password) y redirige a login
GET   /users/login/          # Muestra el formulario de login (users/login.html)
POST  /users/login/          # Valida credenciales con check_password
```

**`POST /users/register/`** — vista `register`

- Campos del formulario: `username`, `email`, `password`, `first_name`, `last_name`,
  `date_of_birth` (opcional), `city` (opcional), `role` (opcional, por defecto `student`).
- Comportamiento: hashea la contraseña con `make_password`, crea el `users.User` y responde con
  `redirect("login")` (302).

**`POST /users/login/`** — vista `login_view`

- Campos del formulario: `username`, `password`.
- Comportamiento: busca el usuario por `username`; si `check_password` es correcto responde
  `redirect("home")` (302); si no, re-renderiza `users/login.html` (200) con el mensaje de error.
- **No** crea sesión de usuario (ver [`auth.md`](auth.md)). La ruta con nombre `home` no está
  definida en la versión actual.

### Cursos (`courses/urls.py`, prefijo `/courses/`)

```http
GET   /courses/                        # Lista todos los cursos (courses/course_list.html)
GET   /courses/create/                 # Muestra el formulario de creación (create_course.html)
POST  /courses/create/                 # Crea un curso y redirige al listado
POST  /courses/<int:course_id>/enroll/ # Inscribe al request.user en el curso
```

**`GET /courses/`** — vista `course_list`

- Comportamiento: renderiza `courses/course_list.html` con `Course.objects.all()` en el contexto.

**`POST /courses/create/`** — vista `create_course`

- Campos del formulario: `title`, `description`, `duration` (horas).
- Comportamiento: crea el `Course` y responde `redirect("course_list")` (302). Un `GET` muestra
  el formulario. **No** asigna instructor al curso.

**`POST /courses/<int:course_id>/enroll/`** — vista `enroll_course`

- Comportamiento: obtiene el curso con `get_object_or_404` (404 si no existe); si el par
  `(request.user, course)` ya tiene una `Inscription`, re-renderiza `course_list.html` (200) con
  `error = "Ya estás inscrito en este curso."`; en caso contrario crea la `Inscription` y responde
  `redirect("course_list")` (302).
- La restricción `unique_together = (user, course)` del modelo impide inscripciones duplicadas a
  nivel de base de datos.
- **Limitación conocida**: usa `request.user`, que no coincide con el modelo propio `users.User`
  porque el login no autentica sesiones (ver deuda técnica en [`auth.md`](auth.md)).

## Rate limiting

- **No aplica en la versión actual.** No hay límites de tasa ni headers `X-RateLimit-*`.

## Webhooks

- **No aplica en la versión actual.** No se reciben ni emiten webhooks.

## Posible evolución futura

Exponer una API REST/JSON (por ejemplo con **Django REST Framework**) es una evolución posible pero
**fuera del alcance de la versión 1.0.0**. Si se aborda, convendría:

- Definir un prefijo de versión (`/api/v1/`) y respuestas JSON con `Content-Type: application/json`.
- Reutilizar los modelos existentes (`User`, `Course`, `Inscription`) mediante serializadores.
- Resolver antes la autenticación (ver [`auth.md`](auth.md)) para poder aplicar tokens y permisos.

## Changelog

- **1.0.0 (2026-07-02)**: primera versión documentada. App server-rendered (MTV) sin API JSON.
