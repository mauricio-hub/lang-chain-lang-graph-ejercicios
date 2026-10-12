# Importamos RunnableLambda: permite envolver funciones normales dentro de un pipeline.
from langchain_core.runnables import RunnableLambda

""" RunnableLambda son objetos que pueden invocarse mediante
el metodo invoke (langchain) , son Una pieza que se puede ejecutar.
 Recibe datos → los procesa → devuelve algo.
 Se puede encadenar con otros pasos usando |.
ejemplo recibe un texto de entrada y hace una salida

seupuede combinar objetos de langchain , funciones personalizadas en python .
. 
"""

# Paso 1: una función lambda que recibe un número y lo convierte en texto
paso1 = RunnableLambda(lambda x : f"Numero recibido: {x}")
# Esto significa:
# - Recibe un input (ej: 43)
# - Devuelve el string "Numero recibido: 43"


# Función normal que duplica el texto en una lista
def duplicar_text(texto):
    # Devuelve una lista con el texto repetido dos veces
    return [texto] * 2


# Paso 2: convertimos esa función normal en un Runnable
paso2 = RunnableLambda(duplicar_text)
# Ahora `paso2` puede conectarse dentro de un pipeline igual que paso1


# Creamos el pipeline usando el operador "|" (pipe)
cadena = paso1 | paso2
# Esto significa:
# - Primero se ejecuta paso1
# - La salida de paso1 se pasa automáticamente a paso2


# Ejecutamos toda la cadena de pasos con el valor 43
resultado = cadena.invoke(100)
# Flujo real:
#   43 → paso1 → "Numero recibido: 43" → paso2 → ["Numero recibido: 43", "Numero recibido: 43"]


print(resultado)  # Salida: ['Numero recibido: 43', 'Numero recibido: 43']
# Mostramos el resultado final del pipeline


def saludar(nombre):
    return nombre  # ← se conserva

step1 = RunnableLambda(saludar)

def nombre_final(nombre):
    return f"hola {nombre}"

step2 = RunnableLambda(nombre_final)

cadena = step1 | step2
print(cadena.invoke("Mauricio"))
