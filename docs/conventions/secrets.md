# Convenciones de secretos y credenciales

> Cómo gestionamos secretos en TechWorld Learning Platform.
> **Última actualización**: 2026-07-02

## Filosofía

- Los secretos **nunca** se commitean en texto plano.
- Separación clara entre **configuración** (no sensible) y **secretos** (sensible).

## Dónde vive cada cosa

| Tipo                         | Dónde                                         |
| ---------------------------- | --------------------------------------------- |
| Secretos de aplicación       | `.env` local (python-dotenv)                  |
| Variables de infraestructura | Variables de entorno del entorno              |
| Secretos de CI/CD            | Secrets del proveedor (p. ej. GitHub Actions) |

## Reglas

- El archivo `.env` está en `.gitignore`; solo se versiona `.env.example` (sin valores).
- Comparte secretos con nuevos colaboradores **fuera de banda** (nunca por git, email plano ni chat público).
- Rota credenciales periódicamente (sugerido cada 90 días) y de inmediato ante sospecha de fuga.
- Si un secreto se commitea por error: **rota el secreto primero**, luego limpia la historia.

## Ejemplos

```bash
# Copiar la plantilla de variables
cp .env.example .env
# Completar valores reales (que nunca se suben):
# DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, SECRET_KEY, DEBUG
```

## Comandos útiles

```bash
# Gestor de secretos dedicado: No aplica en la versión actual.
# Los secretos se cargan desde .env con python-dotenv (load_dotenv en settings).
```

## Referencias

- [SECURITY.md](../../SECURITY.md) — política de seguridad.
- Documentación de python-dotenv.
