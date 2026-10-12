""" from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
#from langchain_community.retrievers import MultiQueryRetriever
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.retrievers import MultiQueryRetriever

# Carga variables de entorno (.env)
load_dotenv()

# Carga una base vectorial YA EXISTENTE desde disco
vectorstore = Chroma(
    persist_directory="C:\\Users\\mgdev\\Desktop\\projects\\curso_langchain\\tema3\\chroma_db",
    embedding_function=OpenAIEmbeddings(model="text-embedding-3-large")
)

# Crea un retriever desde el vectorstore
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
 """
 
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv

load_dotenv()

vectorstore = Chroma(
    persist_directory="C:\\Users\\mgdev\\Desktop\\projects\\curso_langchain\\tema3\\chroma_db",
    embedding_function=OpenAIEmbeddings(model="text-embedding-3-large"),
)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

base_retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2}
)

retriever = MultiQueryRetriever.from_llm(
    retriever=base_retriever,
    llm=llm
)

consulta = "¿Dónde se encuentra el local del contrato en el que participa María Jiménez Campos?"

resultados = retriever.invoke(consulta)

print(f"Número de documentos encontrados: {len(resultados)}")
print("Top documentos más similares a la consulta:\n")

if not resultados:
    print("No se encontraron documentos. Verificando base vectorial...")
    # Verificar que hay documentos en la base
    docs_count = vectorstore._collection.count()
    print(f"Total documentos en Chroma: {docs_count}")

for i, doc in enumerate(resultados, start=1):
    print(f"Documento {i}")
    print(doc.page_content)
    print(doc.metadata)
    print("-" * 40)
