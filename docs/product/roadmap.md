# Roadmap — TechWorld Learning Platform

> Estado y dirección del proyecto. Documento vivo.
> **Última actualización**: 2026-07-02

## Leyenda

- ✅ Hecho
- 🚧 En curso
- 📋 Planificado
- ⏸️ Diferido

## Visión

TechWorld Learning Platform aspira a ser un proyecto de referencia para aprender Django con el patrón MTV: un MVP claro, honesto y completo que evoluciona de forma incremental, incorporando buenas prácticas (autenticación estándar, pruebas, integración continua y despliegue) sin perder su valor didáctico para los estudiantes de Inforcap.

## Estado actual

Versión **1.0.0**: MVP funcional. Permite registrar usuarios (contraseña hasheada con `make_password`), iniciar sesión de forma manual (`check_password`), listar cursos, crear cursos e inscribirse en ellos con control de inscripción duplicada (`unique_together`) y campo de progreso. Stack: Python 3.10+, Django 5.1.3, PostgreSQL vía `psycopg2-binary`, plantillas Django + Bootstrap y configuración por variables de entorno con `python-dotenv`. Aún **no** hay pruebas reales, integración continua ni despliegue configurado, y la autenticación no usa todavía el sistema de sesiones de Django.

## Por versión / fase

### ✅ Fase 1 — v1.0.0: MVP funcional (Hecho)

- [x] Modelo propio `User` con roles (estudiante / instructor).
- [x] Registro de usuarios con contraseña hasheada.
- [x] Inicio de sesión manual verificando el hash.
- [x] Modelos `Course` e `Inscription` con relación usuario–curso y progreso.
- [x] Listado y creación de cursos.
- [x] Inscripción a cursos con control de duplicados (`unique_together`).
- [x] Configuración por variables de entorno y carga de datos iniciales con fixtures.
- [x] Django Admin para usuarios, cursos e inscripciones.

### 🚧 Fase 2 — Consolidación y calidad (En curso)

- [ ] 🚧 Unificar la autenticación con el sistema de Django (migrar a `AbstractUser` o al auth estándar, con sesiones persistentes) para resolver la deuda técnica del login/registro manual.
- [ ] 📋 Agregar pruebas automatizadas (los archivos `tests.py` están vacíos hoy).
- [ ] 📋 Asignar el instructor al crear un curso (hoy `create_course` no asocia instructor).

### 📋 Fase 3 — Funcionalidades para el estudiante y el instructor (Planificado)

- [ ] 📋 Vista de progreso del estudiante (avance por curso a partir del campo `progress` de `Inscription`).
- [ ] 📋 Panel de analítica de cursos (inscripciones, progreso agregado) para instructores.

### 📋 Fase 4 — Operación (Planificado)

- [ ] 📋 Configurar integración continua (CI) para ejecutar las pruebas automáticamente.
- [ ] 📋 Configurar el despliegue del proyecto.

## Backlog / ideas sin agendar

- Recuperación de contraseña y validaciones de formulario más completas.
- Internacionalización (i18n) del proyecto.
- Posible API REST para exponer cursos e inscripciones.

## Fuera de alcance

- Monetización, planes de pago o pasarelas de cobro: el proyecto es educativo y sin ánimo de lucro (licencia MIT).
- Convertirlo en una SPA o añadir un framework JavaScript: se mantiene deliberadamente en el patrón MTV server-rendered por su valor didáctico.

## Cómo se actualiza este documento

- Revisar al cerrar cada versión/fase.
- Las decisiones que cambian el rumbo se registran como ADRs en [`../decisions/`](../decisions/README.md).
