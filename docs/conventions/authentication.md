# Convenciones de autenticación y autorización

> Reglas transversales de autenticación y autorización en TechWorld Learning Platform.
> Para cómo funciona la auth en este proyecto ver
> [`../architecture/auth.md`](../architecture/auth.md).
> **Última actualización**: 2026-07-02

## Stack

- **Autenticación**: login manual (verificación de `username` + `check_password`). Deuda técnica: migrar al sistema de auth de Django.
- **Autorización**: validación en las vistas de Django según el campo `role` del usuario.
- **Hashing de contraseñas**: `make_password` / `check_password` de `django.contrib.auth.hashers`.

## Reglas

- La autorización se valida **siempre en el servidor**, en cada request.
- Nunca confiar en checks de cliente para decisiones de seguridad.
- Las contraseñas se almacenan hasheadas con un algoritmo robusto y salt.
- Los tokens/sesiones se rotan en cada login y tienen expiración.
- Los flujos OAuth/SSO se validan server-side (email y UID).

## Modelo

- **Usuario**: `users.User` con `username`, `email`, `password` (hasheado) y `role`.
- **Sesión / token**: no hay sesión persistente real todavía; depende del middleware de auth de Django (deuda técnica).
- **Roles / permisos**: RBAC simple por el campo `role` (`student` / `instructor`).

## Ejemplos

```text
# Pseudocódigo de verificación de autorización
if not current_user.can?(:accion, recurso)
  rechazar(403)
```

## Comandos útiles

```bash
python manage.py createsuperuser   # crear usuario administrador del admin de Django
```

## Referencias

- [`../architecture/auth.md`](../architecture/auth.md)
- [SECURITY.md](../../SECURITY.md)
