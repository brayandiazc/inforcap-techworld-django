# Diseño — TechWorld Learning Platform

> Decisiones de diseño técnico y de producto: cómo se resuelve el problema y
> cómo se ve y se siente el producto. Las decisiones relevantes se promueven a
> ADRs en [`../decisions/`](../decisions/README.md).
>
> **Última actualización**: 2026-07-02

## Contexto y objetivos

- **Problema**: los estudiantes de Inforcap necesitan un proyecto de referencia, sencillo y
  realista, para aprender a construir una aplicación web con Django siguiendo el patrón MTV. La
  plataforma modela un caso de uso reconocible: gestión de cursos e inscripciones.
- **Objetivos**: permitir registrar usuarios, listar cursos, crear cursos e inscribirse en ellos;
  mantener el código legible y didáctico; usar tecnologías estándar de Django sin capas de
  complejidad innecesarias.
- **No-objetivos**: no se busca una plataforma de producción. Quedan explícitamente fuera: API REST,
  SPA/JS framework, tests automatizados, CI/CD, despliegue, internacionalización, cache, colas,
  emails y un sistema de autenticación robusto (ver [`auth.md`](auth.md)).

## Requisitos

### Funcionales

- Registro de usuarios con contraseña hasheada (`make_password`).
- Inicio de sesión validando credenciales (`check_password`).
- Listado de todos los cursos disponibles.
- Creación de cursos (título, descripción, duración).
- Inscripción de un usuario en un curso, sin permitir duplicados (`unique_together`).
- Distinción semántica de roles `student` / `instructor` en el modelo de usuario.

### No funcionales

- **Simplicidad y legibilidad**: prioridad didáctica; código directo con vistas basadas en funciones.
- **Portabilidad de configuración**: parámetros sensibles (`SECRET_KEY`, credenciales de BD, `DEBUG`)
  vía variables de entorno con `python-dotenv`.
- **Seguridad básica**: contraseñas siempre hasheadas, nunca en texto plano.
- **Rendimiento/escalabilidad/accesibilidad**: no son objetivos de este MVP; se cubren solo por lo
  que aporta Bootstrap por defecto.

## Diseño propuesto

- **Enfoque general**: aplicación Django server-rendered con patrón **MTV**. Dos apps de dominio
  (`users`, `courses`) más el proyecto `techworld`. PostgreSQL como base de datos vía Django ORM.
  Las vistas son funciones simples que leen `request.POST` y renderizan plantillas o redirigen.
- **Componentes y flujos**:
  - `techworld/` — configuración, `urls` raíz (incluye `users/` y `courses/`), WSGI/ASGI.
  - `users/` — modelo `User` propio, vistas `register` y `login_view`, plantillas de auth.
  - `courses/` — modelos `Course` e `Inscription`, vistas `course_list`, `create_course` y
    `enroll_course`, plantillas de cursos.
  - Detalle de piezas y relaciones en [`architecture.md`](architecture.md); modelo de datos en
    [`database.md`](database.md).

## Alternativas consideradas

| Alternativa                                | Pros                                      | Contras                                                        | ¿Por qué se descartó?                                              |
| ------------------------------------------ | ----------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------ |
| SPA (React/Vue) + API REST (DRF)           | Frontend rico, separación clara           | Mayor complejidad, dos stacks, más difícil de enseñar          | El objetivo es enseñar el patrón MTV de Django de forma sencilla.  |
| Auth nativo de Django (`AbstractUser`)     | Sesiones reales, permisos, `@login_required` | Requiere entender más del framework desde el inicio            | Se pospuso para un MVP más simple; queda como deuda técnica.       |
| Frontend con CSS propio sin framework      | Control total del estilo                  | Más tiempo en CSS, menos foco en backend                       | Bootstrap acelera una UI decente con esfuerzo mínimo.              |

## Identidad visual y sistema de diseño

- **Principios de diseño**: claridad y funcionalidad por encima de la estética; consistencia
  mediante herencia de plantillas; UI mínima suficiente para un MVP educativo.
- **Motor de plantillas**: Django Templates con **herencia**. `templates/base.html` define el
  esqueleto HTML (bloques `title` y `content`) e **incluye** `templates/navbar.html` con
  `{% include 'navbar.html' %}`. Las plantillas de cada app extienden esta base.
- **Estilos**: **Bootstrap 5.3.3** cargado desde CDN (`cdn.jsdelivr.net`) en `base.html`, incluyendo
  su JS bundle. Se usan clases utilitarias y componentes de Bootstrap (`navbar`, `container`,
  `card`, `form-control`, etc.).
- **Hoja de estilos propia**: existe `static/css/styles.css` con ajustes menores (fondo claro
  `#f8f9fa`, márgenes de navbar/card/formularios). **Nota**: en la versión actual su `<link>` está
  **comentado** en `base.html`, por lo que estos estilos no se están aplicando; queda pendiente
  habilitarlo (requiere `{% load static %}`).
- **Tokens**: no hay un sistema formal de tokens; los colores y espaciados provienen de Bootstrap y
  de los pocos valores de `styles.css`.
- **Componentes / primitivas permitidas**: los de Bootstrap 5. No hay librería de componentes propia.

### Páginas / plantillas

| Plantilla                              | Ruta                          | Propósito                                        |
| -------------------------------------- | ----------------------------- | ------------------------------------------------ |
| `templates/base.html`                  | —                             | Esqueleto base (Bootstrap + bloques + navbar).   |
| `templates/navbar.html`                | —                             | Barra de navegación global (Cursos, Registrarse, Iniciar Sesión). |
| `users/templates/users/register.html`  | `/users/register/`            | Formulario de registro.                          |
| `users/templates/users/login.html`     | `/users/login/`               | Formulario de inicio de sesión.                  |
| `courses/templates/courses/course_list.html` | `/courses/`             | Listado de cursos y botón de inscripción.        |
| `courses/templates/courses/create_course.html` | `/courses/create/`    | Formulario de creación de curso.                 |

## Accesibilidad

- Se hereda lo que aporta Bootstrap por defecto (contraste y foco de sus componentes; `navbar` con
  atributos ARIA en el toggler).
- **No** hay un trabajo específico de accesibilidad (auditoría de contraste WCAG, gestión de foco
  personalizada ni roles/atributos ARIA adicionales). Queda como mejora futura.

## Estados de la interfaz

- **Éxito**: creación de usuario/curso e inscripción redirigen a la vista correspondiente
  (`login`, `course_list`).
- **Error**: se comunica re-renderizando la plantilla con una variable `error` en el contexto
  (login: "Usuario no encontrado" / "Contraseña incorrecta"; inscripción: "Ya estás inscrito en
  este curso.").
- **Vacío**: el listado de cursos depende de que existan registros; no hay un estado de "sin cursos"
  diseñado explícitamente (mejora pendiente).
- **Carga**: no aplica en la versión actual (renderizado síncrono en servidor, sin llamadas
  asíncronas desde el cliente).

## Modelo de datos afectado

El diseño se apoya en tres entidades: `users.User`, `courses.Course` y `courses.Inscription`
(tabla intermedia con `progress` y restricción `unique_together = (user, course)`). Ver el detalle
en [`database.md`](database.md).

## Riesgos y mitigaciones

| Riesgo                                                             | Impacto | Mitigación                                                                 |
| ----------------------------------------------------------------- | ------- | -------------------------------------------------------------------------- |
| Login sin sesión real e inconsistencia de `request.user`          | Alto    | Migrar al auth nativo de Django (ver deuda técnica en [`auth.md`](auth.md)). |
| Dependencia de CDN para Bootstrap (sin internet no hay estilos)   | Medio   | Servir Bootstrap localmente vía `static/` en una iteración futura.         |
| `styles.css` no se carga (link comentado en `base.html`)          | Bajo    | Habilitar el `<link>` con `{% load static %}` cuando se necesite.          |
| Ausencia de tests y validación de formularios                     | Medio   | Añadir Django Forms y una suite de tests como mejora planificada.          |

## Preguntas abiertas

- [ ] ¿Se migrará la autenticación a `AbstractUser` / auth nativo de Django?
- [ ] ¿Se habilitará `static/css/styles.css` o se consolidará todo en Bootstrap?
- [ ] ¿Debe `create_course` asignar el instructor (usuario) que crea el curso?
- [ ] ¿Se añadirá una vista de progreso y un panel de analítica (previstos en el README)?
- [ ] ¿Se definirá una página de inicio para el `redirect("home")` del login?
