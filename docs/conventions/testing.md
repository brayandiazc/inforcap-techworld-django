# Convenciones de testing

> Cómo escribimos y ejecutamos tests en TechWorld Learning Platform.
> **Última actualización**: 2026-07-02

## Stack

- **Framework de tests**: Django `TestCase` (opcionalmente pytest-django).
- **Cobertura**: coverage.py (opcional; No aplica en la versión actual).
- **Tests de sistema/E2E**: No aplica en la versión actual.

## Tipos de test

| Tipo          | Qué cubre                     | Carpeta              |
| ------------- | ----------------------------- | -------------------- |
| Unitarios     | Funciones/clases aisladas     | `<app>/tests.py`             |
| Integración   | Interacción entre componentes | `<app>/tests.py`             |
| E2E / sistema | Flujos completos de usuario   | No aplica en la versión actual |

## Reglas

- Todo cambio funcional se acompaña de tests.
- Estructura **Arrange-Act-Assert** (AAA): preparar, ejecutar, verificar.
- Un test verifica **una** cosa; nombres descriptivos del comportamiento esperado.
- Los tests deben ser deterministas (sin dependencia de red, reloj o orden).
- Cobertura mínima esperada: No aplica en la versión actual.

## Ejemplos

```python
class RecursoTests(TestCase):
    def test_comportamiento_esperado_cuando_condicion(self):
        # Arrange
        # Act
        # Assert
        ...
```

## Comandos útiles

```bash
python manage.py test                          # Ejecutar todos los tests
coverage run manage.py test && coverage report # Con reporte de cobertura (opcional)
# Modo watch: No aplica en la versión actual.
```

## Referencias

- Documentación oficial de testing de Django.
