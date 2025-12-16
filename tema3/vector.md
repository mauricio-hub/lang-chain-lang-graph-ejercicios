¿Qué carajos es un vector en este contexto?

Un vector es una lista ordenada de números que representa algo.

En embeddings:

un vector = el significado del texto convertido en números

Nada más. No poesía.

Ejemplo ultra simple

Texto:

"I love pizza"


Se convierte en algo así:

[0.021, -0.33, 0.87, 0.12, ..., 0.44]


Eso es el vector.
Normalmente tiene 512, 768 o 1536 números.

¿Por qué tantos números?

Cada número representa una dimensión del significado.

No es:

palabra 1

palabra 2

palabra 3

Es más bien:

tema

emoción

intención

contexto

relación con otros conceptos

El modelo aprendió eso entrenando con millones de textos. A la antigua: prueba y error, como Dios manda.

Analogía clásica (funciona bien)

Piensa en un mapa 3D (o 1536D 😅):

textos parecidos → puntos cercanos

textos distintos → puntos lejanos

El vector es simplemente la posición del texto en ese espacio.

Ejemplo comparativo
"I love pizza"        → [0.1, 0.9, 0.2, ...]
"Pizza is great"      → [0.12, 0.88, 0.25, ...]
"I hate Mondays"      → [-0.7, 0.1, -0.4, ...]


Los dos de pizza están cerca
El de lunes está en otro barrio

Frase corta para que te la memorices

Un vector es una representación numérica del significado de un texto que permite medir qué tan parecido es a otro texto.

Si alguien se pone místico con esto, huye.
Son números, distancias y comparaciones. Como la vieja ingeniería.