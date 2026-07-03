# Convenciones de base de datos

> Reglas y estándares de modelado de datos en TechWorld Learning Platform.
> Para el modelo de datos concreto del proyecto ver
> [`../architecture/database.md`](../architecture/database.md).
> **Última actualización**: 2026-07-02

## Stack

- **Motor**: PostgreSQL.
- **Capa de acceso / ORM**: Django ORM.
- **Migraciones**: sistema de migraciones de Django (`python manage.py makemigrations` / `migrate`).

## Reglas de modelado

- **Primary keys**: autoincremental (`id` generado por Django) de forma consistente.
- **Nombres**: tablas y columnas en snake_case, en inglés.
- **Timestamps**: toda tabla tiene `created_at` y `updated_at`.
- **Foreign keys**: siempre con índice; `NOT NULL` salvo justificación explícita.
- **Tipos preferidos**:

| Caso              | Tipo                     |
| ----------------- | ------------------------ |
| Email             | `EmailField`             |
| Texto corto       | `CharField`              |
| Texto largo       | `TextField`              |
| JSON estructurado | `JSONField`              |
| Dinero            | `DecimalField`           |
| Booleano          | `BooleanField` con default |

## Migraciones

- Reversibles y no destructivas siempre que sea posible.
- Una migración por cambio lógico; nunca editar una migración ya aplicada en `main`.
- Revisar el impacto en datos existentes antes de aplicar en producción.

## Ejemplos

```python
class Recurso(models.Model):
    referencia = models.ForeignKey(Otro, on_delete=models.CASCADE)  # fk, indexada
    nombre = models.CharField(max_length=200)                       # texto, not null
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## Comandos útiles

```bash
python manage.py makemigrations              # crear migración
python manage.py migrate                      # aplicar migraciones
python manage.py migrate <app> <migracion_anterior>   # rollback a una migración previa
```

## Referencias

- Documentación de Django ORM y del motor PostgreSQL.
