¿Qué son embeddings?

Los embeddings son números que representan el significado de un texto.
No palabras sueltas, significado.
Una frase → se convierte en un vector (una lista de números).

La gracia:
textos con significado parecido → números parecidos.

¿Para qué sirven?

Principalmente para:

Buscar texto por significado, no por palabras exactas

RAG (buscar info relevante antes de preguntar al LLM)

Clasificar, agrupar o comparar textos

Vieja escuela: LIKE '%perro%'
Nueva escuela: “¿esto se parece semánticamente?”

Ejemplo simple (conceptual)

Frases:

"I love pizza"

"Pizza is my favorite food"

"I hate waking up early"

Las dos primeras generan embeddings muy cercanos
La tercera queda lejos

Aunque no compartan exactamente las mismas palabras.

Ejemplo práctico (LangChain + OpenAI)
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector = embeddings.embed_query("I love pizza")

print(len(vector))   # ej: 1536 números


Ese vector es el significado de la frase en forma matemática.

¿Y luego qué haces con eso?

Generas embeddings de documentos

Los guardas en una vector DB (Chroma, FAISS, Pinecone)

Embedding de la pregunta del usuario

Comparas (cosine similarity)

Traes los textos más parecidos

Se los pasas al LLM
👉 RAG

Mini-ejemplo mental de RAG

Usuario pregunta:

“How do I install Docker on Windows?”

No buscas por palabras.
Buscas por significado → traes el doc correcto aunque diga:

“Steps to set up Docker on Windows 11”

Frase clave para entrevistas

Embeddings transform text into vectors that capture semantic meaning, allowing us to compare and retrieve information based on meaning rather than keywords.

Y ya está.
Nada místico: matemática + lenguaje. Como debe ser.