¿Qué es RAG?

RAG = Retrieval + Augmented Generation

Traducido a humano:

buscar primero información correcta y luego usarla para responder

El problema SIN RAG

Le preguntas al modelo:

“¿Cómo se instala Docker en Windows?”

El modelo:

responde de memoria

puede alucinar

puede estar desactualizado

Como ese amigo que “cree recordar”.

Qué hace RAG (paso a paso, modo bebé 🍼)

El usuario pregunta algo

Buscas información relacionada (en tus documentos)

Le das esa info al modelo

El modelo responde usando SOLO eso

Listo. Eso es RAG.

Ejemplo infantil

Tienes estos documentos:

“Guía Docker Windows”

“Manual React”

“Recetas de pasta”

Pregunta:

“How do I install Docker on Windows?”

RAG:

busca el doc de Docker

se lo pasa al modelo

el modelo responde con eso

No inventa recetas 🍝.

Dónde entran embeddings y la DB vectorial

La parte Retrieval funciona así:

documentos → embeddings → DB vectorial

pregunta → embedding

buscas los más parecidos

los traes

Eso es el “buscar”.

Diagrama mental ultra simple
Pregunta
   ↓
Embedding
   ↓
Vector DB (busca parecido)
   ↓
Texto encontrado
   ↓
LLM responde con eso


Fin.

Frase corta para decir sin quedar como payaso

RAG is a technique where the model retrieves relevant information from external data sources and uses it to generate more accurate responses.

Regla de oro

Si una app de IA no usa RAG:

inventa

miente con confianza

parece lista… pero no lo es.