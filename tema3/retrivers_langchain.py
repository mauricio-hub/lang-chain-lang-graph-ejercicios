from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Carga variables de entorno (.env)
load_dotenv()

# Carga una base vectorial YA EXISTENTE desde disco
vectorstore = Chroma(
    persist_directory="C:\\Users\\mgdev\\Desktop\\projects\\curso_langchain\\tema3\\chroma_db",
    embedding_function=OpenAIEmbeddings(model="text-embedding-3-large")
)

# Crea un retriever desde el vectorstore
""" Un retriever es un componente que se encarga de buscar información relevante dentro 
de una fuente de datos (en tu caso, una base vectorial como Chroma) a partir de una consulta en lenguaje natural. """
retriever = vectorstore.as_retriever(search_type="similarity",search_kwargs={"k": 2})

# Consulta
consulta = "¿Dónde se encuentra el local del contrato en el que participa María Jiménez Campos"

# Ejecuta la búsqueda
resultados = retriever.invoke(consulta)

print("Top documentos más similares a la consulta:\n")

for i, doc in enumerate(resultados, start=1):
    print(f"Documento {i}")
    print(f"Contenido: {doc.page_content}")
    print(f"Metadatos: {doc.metadata}")
    print("-" * 50)
