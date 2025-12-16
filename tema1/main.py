from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Cargar variables de entorno desde el archivo .env
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


pregunta = "¿En que año llego el hombre a la luna?"
print("pregunta:", pregunta)

respuesta = llm.invoke(pregunta)

print("respuesta:", respuesta.content)
