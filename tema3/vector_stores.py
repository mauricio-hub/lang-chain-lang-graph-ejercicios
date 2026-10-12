# Vector store (base de datos vectorial)
from langchain_community.vectorstores import Chroma

# Modelo de embeddings de OpenAI
from langchain_openai import OpenAIEmbeddings

# Loader para leer PDFs desde una carpeta
from langchain_community.document_loaders import PyPDFDirectoryLoader

# Divide textos grandes en partes más pequeñas (chunks)
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv

# Carga variables de entorno (.env), por ejemplo OPENAI_API_KEY
load_dotenv()

# Carga todos los PDFs que estén dentro de esta carpeta
loader = PyPDFDirectoryLoader(
    "C:\\Users\\mgdev\\Desktop\\projects\\curso_langchain\\tema3\\contratos"
)

# Lee los PDFs y los convierte en documentos de LangChain
documentos = loader.load()

print(f"cantidad de documentos {len(documentos)}")

# Configura cómo se va a partir el texto
# chunk_size: tamaño máximo de cada fragmento
# chunk_overlap: texto que se repite entre chunks para no perder contexto
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=5000,
    chunk_overlap=1000
)

# Divide los documentos en chunks de texto
docs_split = text_splitter.split_documents(documentos)

print(f"Se crearon {len(docs_split)} chunks de texto.")

# Crea la base de datos vectorial Chroma
# - Convierte cada chunk en un vector (embedding)
# - Guarda la base en disco (persist_directory)
vectorstore = Chroma.from_documents(
    docs_split,
    embedding=OpenAIEmbeddings(model="text-embedding-3-large"),
    persist_directory="C:\\Users\\mgdev\\Desktop\\projects\\curso_langchain\\tema3\\chroma_db"
)

# Pregunta que se quiere buscar dentro de los documentos
consulta = "¿Dónde se encuentra el local del contrato en el que participa María Jiménez Campos"

# Busca los documentos más similares a la consulta
# k=2 → devuelve los 2 más relevantes
resultados = vectorstore.similarity_search(consulta, k=2)

print("Top 3 documentos mas similares a la consulta:\n")

# Imprime el contenido y metadatos de cada resultado
for i, doc in enumerate(resultados, start=1):
    print(f"Contenido: {doc.page_content}")
    print(f"Metadatos: {doc.metadata}")
