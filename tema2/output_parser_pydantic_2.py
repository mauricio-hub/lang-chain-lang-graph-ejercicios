from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# -------------------------------------------------------------
# 1. DEFINICIÓN DEL MODELO Pydantic
# -------------------------------------------------------------
# Este modelo define la estructura EXACTA que queremos recibir
# como salida del LLM. Es decir: la IA TIENE que responder
# con estos campos y en estos tipos.
class AnalisisTexto(BaseModel):
    resumen: str = Field(description="Resumen breve del texto.")
    sentimiento: str = Field(description="Sentimiento del texto (Positivo, neutro o negativo)") 


# -------------------------------------------------------------
# 2. INICIALIZAMOS EL LLM DE OPENAI VIA LANGCHAIN
# -------------------------------------------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# -------------------------------------------------------------
# 3. CONVERTIMOS EL LLM EN UN 'STRUCTURED LLM'
# -------------------------------------------------------------
# Aquí pasa lo clave:
#   - with_structured_output() le dice al LLM:
#         “Devuélveme la respuesta siguiendo ESTE modelo Pydantic”.
#   - LangChain genera automáticamente un SYSTEM PROMPT oculto
#     que obliga al modelo a responder SOLO en JSON válido
#     siguiendo AnalisisTexto.
#
# Esto reemplaza el uso manual de JSON y Validadores.
structured_llm = llm.with_structured_output(AnalisisTexto)

# -------------------------------------------------------------
# 4. TEXTO A ANALIZAR
# -------------------------------------------------------------
texto_prueba = "Me fastidió la película, lo más apestoso que vi en mi vida."

# -------------------------------------------------------------
# 5. INVOCAMOS AL MODELO
# -------------------------------------------------------------
# Aquí ocurre la magia:
#   - LangChain envía el prompt al modelo.
#   - El modelo responde con un JSON.
#   - LangChain lo valida automáticamente con Pydantic.
#   - Si falta un campo o rompe la estructura → error.
#   - Si es correcto → devuelve un objeto AnalisisTexto ya listo.
resultado = structured_llm.invoke(f"Analiza el siguiente texto: {texto_prueba}")

# -------------------------------------------------------------
# 6. IMPRIMIR RESULTADO COMO OBJETO Pydantic
# -------------------------------------------------------------
print(resultado)
