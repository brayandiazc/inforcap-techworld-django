# Convenciones de calidad y tooling

> Linters, formato, análisis estático y git hooks de TechWorld Learning Platform.
> **Última actualización**: 2026-07-02

## Stack

- **Linter**: ruff (o flake8).
- **Formateador**: black (longitud de línea 88).
- **Análisis estático / seguridad**: No aplica en la versión actual.
- **Auditoría de dependencias**: No aplica en la versión actual.
- **Orquestador de git hooks**: pre-commit (opcional; No aplica en la versión actual).

## Git hooks

Estrategia sugerida: hooks baratos y rápidos en `pre-commit`, los más costosos en
`pre-push`. CI ejecuta todo de nuevo en el servidor.

### pre-commit (en cada commit)

- Linter sobre archivos cambiados.
- Formato automático.
- Verificación de trailing whitespace, fin de archivo, conflictos sin resolver.

### pre-push (al subir)

- Linter completo.
- Tests (o un subconjunto rápido).
- Auditoría de dependencias.

## Reglas

- El código debe pasar linter y formato antes del merge.
- Los checks de calidad son **bloqueantes** en CI.

## Comandos útiles

```bash
ruff check .    # lint
black .         # formato
# Auditoría de dependencias: No aplica en la versión actual.
```

## Referencias

- Documentación oficial de black y ruff.
