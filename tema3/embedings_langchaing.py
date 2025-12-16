from langchain_openai import OpenAIEmbeddings
import numpy as np
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

texto1 ="plomo a Maduro"
texto2 ="Buenos Aires es la capital de Argentina"


vec1 = embeddings.embed_query(texto1)
vec2 = embeddings.embed_query(texto2)

print(f"Dimension de los vectores 1: {len(vec1)}")
print(f"Dimension de los vectores 2: {len(vec2)}")


cos_sim = np.dot(vec1 , vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

print(f"Similitud de conesno entre vectores 1 y 2 {cos_sim:.3f}")

