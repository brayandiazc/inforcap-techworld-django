# Convenciones de vistas y layouts

> Cómo organizamos vistas, layouts y UI compartida en TechWorld Learning Platform.
> **Última actualización**: 2026-07-02

## Layouts

| Layout                                | Uso                                         |
| ------------------------------------- | ------------------------------------------- |
| `templates/base.html`                 | Páginas públicas (landing, listado de cursos) |
| `templates/base.html` (`users/`)      | Pantallas de autenticación (login/registro) |
| `templates/base.html` + `templates/navbar.html` | Producto autenticado (área de cursos) |

## Elementos compartidos

- **Head compartido**: metadatos y SEO (ver [`seo.md`](seo.md)).
- **Mensajes flash**: patrón único para notificaciones de éxito/error.
- **Navegación**: header/menú reutilizable.

## Reglas

- Reutiliza parciales/componentes; no dupliques marcado.
- Cada vista contempla sus estados: carga, vacío, error y éxito.
- La UI sigue el [sistema de diseño](design-system.md).
- Separa estructura (layout) de contenido (vista) de comportamiento.

## Estructura

```text
templates/
├── base.html                 # layout base (herencia de plantillas)
└── navbar.html               # navegación reutilizable

<app>/templates/<app>/        # vistas por recurso (p. ej. courses/, users/)
```

## Referencias

- [`design-system.md`](design-system.md)
- [`seo.md`](seo.md)
