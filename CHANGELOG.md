# Changelog

Todos los cambios notables de este proyecto se documentan en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [1.0.0] - 2026-07-02

### Added

- Gestión de usuarios (app `users`): registro con contraseña hasheada e inicio de sesión.
- Gestión de cursos (app `courses`): listado, creación e inscripción de estudiantes con control de duplicados (`unique_together`).
- Modelo de datos con las entidades `User`, `Course` e `Inscription` (con progreso).
- Panel de administración de Django para usuarios, cursos e inscripciones.
- Datos iniciales cargables mediante fixtures (`loaddata`).
- Plantillas con Django Templates + Bootstrap (herencia de `base.html` y `navbar.html`).
- Configuración por variables de entorno con `python-dotenv` (`.env.example`).
- Documentación del proyecto y de gobernanza a partir de la plantilla
  [`project-starter-template-es`](https://github.com/brayandiazc/project-starter-template-es):
  `docs/` (arquitectura, producto, convenciones y decisiones), `CONTRIBUTING`,
  `CODE_OF_CONDUCT`, `SECURITY`, `LICENSE` (MIT), `.editorconfig` y plantillas de
  issues/PR en `.github/`.

<!--
Enlaces de comparación entre versiones:
[Unreleased]: https://github.com/brayandiazc/inforcap-techworld-django/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/brayandiazc/inforcap-techworld-django/releases/tag/v1.0.0
-->
