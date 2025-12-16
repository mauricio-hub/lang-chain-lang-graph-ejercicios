from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_openai import ChatOpenAI
import json
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------
# CONFIGURACIÓN DEL MODELO LLM
# ---------------------------------------
# Instanciamos el modelo "gpt-4o-mini".
# temperature=0 garantiza respuestas más consistentes y menos creativas
# (ideal para análisis, resúmenes y JSON).
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# ---------------------------------------
# PREPROCESAMIENTO DEL TEXTO
# ---------------------------------------
def preprocess_text(text):
    """
    Limpia el texto eliminando espacios al inicio/final
    y recorta el texto a un máximo de 500 caracteres.
    
    Este paso evita enviar contenido sucio o demasiado largo al modelo.
    Es un "primer filtro" antes del pipeline real.
    """
    return text.strip()[:500]

# Convertimos la función a un objeto Runnable para integrarla en el pipeline.
preprocessor = RunnableLambda(preprocess_text)


# ---------------------------------------
# FUNCIÓN: GENERAR RESUMEN
# ---------------------------------------
def generate_summary(text):
    """
    Toma el texto preprocesado y genera un resumen en una sola oración.
    Construye un prompt simple y envía la solicitud al modelo LLM.
    Retorna SOLO el contenido del mensaje generado por el LLM.
    """
    prompt = f"Resume en una sola oración: {text}"
    response = llm.invoke(prompt)  # Ejecuta el modelo con el prompt
    return response.content        # Extraemos el texto generado por el LLM

# Convertimos la función a Runnable para usarla como rama del pipeline.
summary_brach = RunnableLambda(generate_summary)


# ---------------------------------------
# FUNCIÓN: ANÁLISIS DE SENTIMIENTO
# ---------------------------------------
def analyze_sentiment(text):
    """
    Analiza el sentimiento del texto.
    
    - Crea un prompt que obliga al modelo a responder solo en JSON.
    - Llama al modelo y trata de parsear el JSON devuelto.
    - Si el modelo devuelve algo inválido, se captura la excepción
      y se responde con un JSON seguro.
    """
    
    prompt = f"""Analiza el sentimiento del siguiente texto.
    Responde ÚNICAMENTE en formato JSON válido:
    {{"sentimiento": "positivo|negativo|neutro", "razon": "justificación breve"}}
    
    Texto: {text}"""
    
    response = llm.invoke(prompt)

    # Intentamos convertir la respuesta del LLLM a JSON real.
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        # Si algo falla (lo cual pasa a veces con los LLMs),
        # devolvemos un JSON controlado para no romper el pipeline.
        return {"sentimiento": "neutro", "razon": "Error en análisis"}

# Convertimos esta función en Runnable para usarla en paralelo.
sentiment_branch = RunnableLambda(analyze_sentiment)


# ---------------------------------------
# FUNCIÓN: FUSIÓN DE RESULTADOS
# ---------------------------------------
def merge_results(data):
    """
    Combina los resultados provenientes de las dos ramas paralelas.

    `data` llega con esta estructura:
    {
        "resumen": <texto>,
        "sentimiento_data": {
            "sentimiento": <positivo|negativo|neutro>,
            "razon": <explicación>
        }
    }

    Aquí simplemente rearmamos un diccionario final más limpio.
    """
    return {
        "resumen": data["resumen"],
        "sentimiento": data["sentimiento_data"]["sentimiento"],
        "razon": data["sentimiento_data"]["razon"]
    }

# Se convierte la función en Runnable para cerrar la cadena.
merger = RunnableLambda(merge_results)


# ---------------------------------------
# ANÁLISIS EN PARALELO
# ---------------------------------------
# Ejecuta summary_brach y sentiment_branch al mismo tiempo.
# Cada una recibe el mismo input (el texto preprocesado).
#
# El resultado será un diccionario con ambas salidas:
# {
#   "resumen": <resultado de summary_branch>,
#   "sentimiento_data": <resultado de sentiment_branch>
# }
parallel_analysis = RunnableParallel({
    "resumen": summary_brach,
    "sentimiento_data": sentiment_branch
})


# ---------------------------------------
# CADENA COMPLETA (PIPELINE FINAL)
# ---------------------------------------
# Flujo completo:
# 1. preprocessor → limpia el texto
# 2. parallel_analysis → genera resumen + sentimiento al mismo tiempo
# 3. merger → junta todo en un formato de salida claro
chain = preprocessor | parallel_analysis | merger

#analizando solo un resultado no recomendodo
#review = "este producto es una mierda asquesosa es lo peor que he comprado"

#form simple
#resultado = chain.invoke(review)

## analizando varios resultados en paralelo 

review_batch = [
    "Excelente me encanta tus nalgas",
    "del asco las peores nalgas del mundo",
    "regula me ha parecido todo algo positivio es que termino rapido"
]

result_batch = chain.batch(review_batch)

print(result_batch)