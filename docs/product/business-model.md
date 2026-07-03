# TechWorld Learning Platform — Modelo de Negocio

> Marco: **Lean Canvas** (adaptado a un contexto educativo). Describe por qué existe el proyecto y cómo genera valor.
> **Nota importante**: TechWorld Learning Platform es un **proyecto educativo de reforzamiento** para estudiantes de Inforcap, **no un producto comercial**. Es de uso formativo, **sin ánimo de lucro**, publicado bajo **licencia MIT**. Donde este marco pide precios, ingresos o rentabilidad, se indica que **no aplica** por tratarse de un proyecto educativo.
> **Última actualización**: 2026-07-02

## 1. Problema

- **Problema principal**: quienes aprenden Django necesitan un ejemplo completo y realista que muestre, de principio a fin, cómo se construye un MVP web con el patrón MTV (Modelo-Template-Vista), y no solo fragmentos aislados de código.
- **Problema secundario**: la teoría de modelos, relaciones (uno a muchos, tablas intermedias), migraciones, plantillas y formularios se entiende mejor con un dominio concreto que la conecta con un caso práctico (gestión de cursos e inscripciones).
- **Alternativas actuales**: tutoriales sueltos, documentación oficial y ejercicios "de juguete" que rara vez integran usuarios, cursos, inscripciones y progreso en un mismo proyecto coherente.

## 2. Segmentos de cliente

> En este proyecto, "clientes" se entiende como **audiencia formativa**. No hay clientes de pago.

| Segmento                    | Descripción                                                                                     | Notas                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Estudiantes de Inforcap     | Aprendices de Django que refuerzan sus conocimientos siguiendo el proyecto paso a paso.         | Audiencia principal / "early adopter" del material.       |
| Instructores y docentes     | Personas que enseñan Django y usan el proyecto como material de apoyo o base para sus clases.   | Adaptan y extienden el ejemplo para sus grupos.           |

- **Audiencia ideal**: estudiante de Inforcap con bases de Python que quiere construir su primer proyecto web full-stack con Django y entender el patrón MTV en un caso real.
- **Primeros usuarios**: los propios grupos de reforzamiento de Inforcap guiados por el instructor.

## 3. Propuesta de valor única

- Un MVP educativo **completo y honesto**: muestra un flujo real (registro, inicio de sesión, listado de cursos, inscripción con control de duplicados y seguimiento de progreso) usando exclusivamente Django y el patrón MTV, sin capas innecesarias.
- **Concepto de alto nivel**: "un proyecto guía tipo plataforma de cursos, para aprender Django MTV construyéndolo de verdad".

## 4. Solución (el producto)

| Módulo / Capacidad          | Qué resuelve                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------- |
| App `users`                 | Registro de usuarios con contraseña hasheada (`make_password`) e inicio de sesión manual; enseña modelos propios y roles (estudiante / instructor). |
| App `courses`               | Creación y listado de cursos; enseña modelos, migraciones y renderizado con plantillas.              |
| Inscripciones y progreso    | Relación usuario–curso mediante el modelo `Inscription` (tabla intermedia con progreso y `unique_together`); enseña relaciones N–N con datos extra y validación de duplicados. |
| Django Admin                | Panel de administración para gestionar usuarios, cursos e inscripciones sin escribir vistas propias. |

## 5. Canales

- Repositorio público en GitHub (`brayandiazc/inforcap-techworld-django`) con guía paso a paso.
- Sesiones y material de reforzamiento de Inforcap.
- Boca a boca entre estudiantes e instructores de la comunidad.

## 6. Modelo de ingresos

> **No aplica.** El proyecto es educativo y **sin ánimo de lucro**; se distribuye gratuitamente bajo **licencia MIT**. No existen planes, precios, suscripciones ni monetización de ningún tipo.

## 7. Estructura de costos y rentabilidad

> **No aplica como negocio.** Al ser un proyecto formativo y de código abierto, no hay estructura de ingresos ni objetivo de rentabilidad.

- **Costos del proyecto**: se limitan al tiempo de desarrollo y mantenimiento voluntario del autor. Para ejecutarlo basta un entorno local con Python y PostgreSQL; no requiere infraestructura de pago.

## 8. Métricas clave

> Al ser educativo, las métricas relevantes son de **aprendizaje y adopción del material**, no comerciales.

- **De aprendizaje**: estudiantes que completan la guía y logran levantar el proyecto localmente; comprensión del patrón MTV y de las relaciones entre modelos.
- **De adopción**: estrellas / forks del repositorio, uso del proyecto como base en cursos y aportes de la comunidad.

## 9. Ventaja competitiva

- Proyecto real, coherente y mantenido por un instructor de Inforcap, pensado explícitamente para enseñar y con el código honesto sobre su propio estado (incluyendo su deuda técnica documentada, como la autenticación).

## Decisiones pendientes

- [ ] Definir hasta qué punto extender el proyecto como material sin perder su claridad didáctica.
- [ ] Decidir si se documenta la migración de la autenticación propia al sistema de auth de Django como ejercicio guiado.
