from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Cargar variables de entorno desde el archivo .env
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)


pregunta = "¿hola gemini ,En que año llego el hombre a la luna?"
print("pregunta:", pregunta)

respuesta = llm.invoke(pregunta)

print("respuesta:", respuesta.content)
