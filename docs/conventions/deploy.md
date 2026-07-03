# Convenciones de despliegue

> Operaciones de producción de TechWorld Learning Platform. Fuente de verdad de cómo se
> despliega, se hace rollback y se opera el sistema.
> **Última actualización**: 2026-07-02

> **Estado**: no hay pipeline de despliegue configurado aún. Este documento describe el
> esquema típico previsto (gunicorn + `collectstatic` + `migrate`) y queda pendiente de
> definir en detalle.

## Stack de infraestructura

- **Hosting / cómputo**: pendiente de definir.
- **DNS / TLS**: pendiente de definir.
- **Contenedores / orquestación**: No aplica en la versión actual.
- **CI/CD**: GitHub Actions (ver `.github/workflows/`, aún de ejemplo).

## Ambientes

| Ambiente   | URL              | Rama      | Deploy     |
| ---------- | ---------------- | --------- | ---------- |
| Desarrollo | http://127.0.0.1:8000 | `develop` | Automático |
| Staging    | pendiente de definir  | `staging` | Automático |
| Producción | pendiente de definir  | `main`    | Manual     |

## Reglas

- Solo se despliega a producción desde `main`.
- Cada deploy debe ser reproducible y reversible.
- Las variables de entorno y secretos se gestionan según [`secrets.md`](secrets.md).
- Verificar health checks tras cada deploy.

## Procedimiento de deploy

```bash
# Esquema típico previsto (pipeline pendiente de definir)

# 1. Preparar estáticos
python manage.py collectstatic --noinput

# 2. Aplicar migraciones y servir con gunicorn
python manage.py migrate
gunicorn techworld.wsgi

# 3. Verificar
# Comando de deploy: pendiente de definir.
```

## Rollback

```bash
# Pendiente de definir (a nivel de infraestructura).
# A nivel de datos, revertir migraciones:
python manage.py migrate <app> <migracion_anterior>
```

## Health checks y monitoreo

- Endpoint de salud: No aplica en la versión actual.
- Monitoreo de errores: No aplica en la versión actual.
- Alertas: No aplica en la versión actual.

## Referencias

- Documentación oficial de despliegue de Django (gunicorn, `collectstatic`, `migrate`).
