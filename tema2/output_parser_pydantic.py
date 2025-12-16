from pydantic import BaseModel
# tecnica outputparcer
# Pydantic permite definir modelos de datos con validación automática.
# Al heredar de BaseModel, Usuario se convierte en un "modelo Pydantic"
# que valida tipos, convierte valores y aplica defaults automáticamente.
class Usuario(BaseModel):
    id: int           # Campo obligatorio. Pydantic intentará convertir el valor a int.
    nombre: str       # Campo obligatorio. Debe ser string.
    activo: bool = True  # Campo opcional. Si no se lo pasas, usa el valor por defecto: True.


# Diccionario con los datos de entrada.
# Ojo: "id" viene como string "123", pero Pydantic intentará convertirlo a int.
data = {"id": "123", "nombre": "Mafalda"}


# Aquí ocurre la magia:
# Usuario(**data) toma el dict, valida los tipos, convierte lo necesario
# y crea una instancia del modelo Usuario.
usuario = Usuario(**data)


# Cuando imprimes un modelo Pydantic, muestra los valores ya validados
# y convertidos a sus tipos reales.
print(usuario)
