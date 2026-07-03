# Convenciones del sistema de diseño

> Tokens, componentes y reglas de UI de TechWorld Learning Platform.
> Para el diseño técnico/UX del producto ver
> [`../architecture/design.md`](../architecture/design.md).
> **Última actualización**: 2026-07-02

## Stack

- **Librería de componentes**: Bootstrap.
- **Solución de estilos**: Bootstrap + Django Templates (más `static/css/styles.css`).
- **Página de referencia viva** (si aplica): No aplica en la versión actual.

## Tokens

| Token          | Uso                             |
| -------------- | ------------------------------- |
| Colores        | primario, secundario y estados de Bootstrap |
| Tipografía     | familias y escalas de Bootstrap             |
| Espaciado      | escala de espaciado de Bootstrap            |
| Bordes/sombras | radios y elevaciones de Bootstrap           |

> Usa **tokens semánticos** (p. ej. `color-primario`), no valores crudos, en los componentes.

## Componentes permitidos

- Usa los componentes de la librería; evita crear variantes ad-hoc.
- Cada componente debe contemplar sus **estados**: normal, hover, foco, deshabilitado, carga, error.

## Accesibilidad (baseline)

- Contraste mínimo objetivo: WCAG AA.
- Foco visible y navegación por teclado.
- Roles/atributos ARIA donde corresponda.

## Anti-patrones

- Valores de color/espaciado hardcodeados fuera de los tokens.
- Componentes duplicados que reimplementan algo existente.

## Referencias

- Documentación oficial de Bootstrap.
