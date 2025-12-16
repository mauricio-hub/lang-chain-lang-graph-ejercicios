from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

chat = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

#prompt template para traduccion

translator_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un traductor experto que traduce textos al idioma ingles."),
    ("human", "{texto}")
])


#cadena 

translator_chain = translator_prompt | chat

def traducir(texto: str) -> str:
    resp = translator_chain.invoke({"texto": texto})
    return resp.content.strip()


if __name__ == "__main__":
    resultado = traducir("los zapatos de  Sra. Smith son rojos")
    print(resultado)