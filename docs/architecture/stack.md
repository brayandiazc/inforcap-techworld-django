# Stack Tecnológico

> Fuente de verdad de las tecnologías y versiones del proyecto.
> **Última actualización**: 2026-07-02

## Frontend

| Categoría | Tecnología                    | Versión | Por qué |
| --------- | ----------------------------- | ------- | ------- |
| Framework | Django Templates (renderizado en servidor, patrón MTV) | 5.1.3 | El proyecto no usa una SPA ni framework JS; las vistas devuelven HTML renderizado en el servidor. |
| Estado    | No aplica en la versión actual | —      | Al ser renderizado en servidor, no hay una capa de estado en el cliente. |
| Estilos   | Bootstrap + CSS propio (`static/css/styles.css`) | — | Bootstrap acelera el maquetado responsivo del MVP; el CSS propio ajusta detalles. |
| Build     | No aplica en la versión actual | —      | No hay bundler; los estáticos se sirven directamente con el sistema de archivos estáticos de Django. |

## Backend

| Categoría           | Tecnología                         | Versión | Por qué |
| ------------------- | ---------------------------------- | ------- | ------- |
| Runtime             | Python                             | 3.10+   | Versión mínima requerida por Django 5.1.x. |
| Framework           | Django                             | 5.1.3   | Framework backend full-stack que provee el patrón MTV, ORM, admin y enrutamiento. |
| ORM / capa de datos | Django ORM                         | 5.1.3   | Incluido en Django; mapea los modelos (`User`, `Course`, `Inscription`) a tablas de PostgreSQL. |
| Validación          | Validación integrada de modelos y formularios de Django | 5.1.3 | Se usan las restricciones y validaciones que ofrece el propio framework (campos, `unique`, `choices`). |

## Base de Datos

| Categoría | Tecnología                       | Versión | Por qué |
| --------- | -------------------------------- | ------- | ------- |
| Principal | PostgreSQL (motor `django.db.backends.postgresql` vía `psycopg2-binary`) | psycopg2-binary 2.9.10 | Base de datos relacional robusta y estándar en producción con Django. |
| Cache     | No aplica en la versión actual   | —       | El MVP no configura una capa de cache. |
| Cola      | No aplica en la versión actual   | —       | No hay procesamiento asíncrono ni tareas en segundo plano. |

## DevOps & Herramientas

| Categoría    | Tecnología                                    |
| ------------ | --------------------------------------------- |
| CI/CD        | No aplica en la versión actual                |
| Contenedores | No aplica en la versión actual                |
| Orquestación | No aplica en la versión actual                |
| Monitoreo    | No aplica en la versión actual                |
| Testing      | No aplica en la versión actual (los archivos `tests.py` están vacíos) |

## Servicios externos

| Servicio     | Uso              | Credenciales necesarias |
| ------------ | ---------------- | ----------------------- |
| No aplica en la versión actual | El proyecto no integra servicios externos de terceros. | — |

> Configuración por variables de entorno (`.env`, leídas en `techworld/settings.py` con `python-dotenv==1.0.1`): `DB_HOST`, `DB_PORT` (5432), `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `SECRET_KEY`, `DEBUG`.

## Justificación de elecciones

| Tecnología elegida            | Alternativa descartada       | Razón                                                            |
| ----------------------------- | ---------------------------- | ---------------------------------------------------------------- |
| Django Templates (MTV)        | SPA (React/Vue) + API REST   | Es un proyecto educativo/MVP; el renderizado en servidor mantiene el foco en aprender Django sin complejidad de frontend. |
| PostgreSQL                    | SQLite                       | Se prefiere una base de datos de nivel producción para acercar el ejercicio a un escenario real. |
| pip + `requirements.txt`      | Poetry / Pipenv              | Gestor de paquetes estándar y suficiente para el alcance del MVP. |

## Dependencias (requirements.txt)

- `asgiref==3.8.1`
- `Django==5.1.3`
- `psycopg2-binary==2.9.10`
- `python-dotenv==1.0.1`
- `sqlparse==0.5.2`

Instalación: `pip install -r requirements.txt`. Servidor de desarrollo: `python manage.py runserver` (http://127.0.0.1:8000). Datos iniciales: fixtures JSON cargados con `python manage.py loaddata`.

## Versiones mínimas soportadas

- Python >= 3.10
- Django == 5.1.3
- PostgreSQL con driver `psycopg2-binary` >= 2.9.10
