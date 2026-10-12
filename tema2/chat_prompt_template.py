from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv(override=True)

chat = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

#prompt template para traduccion

translator_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente util que atiende a personas en preguntas general te llamas CULOBOT responde de manera chistosa e ironico y grosero muy grosero."),
    ("human", "{texto}")
])


#cadena 

translator_chain = translator_prompt | chat

def traducir(texto: str) -> str:
    resp = translator_chain.invoke({"texto": texto})
    return resp.content.strip()


if __name__ == "__main__":
    resultado = traducir("como te llamas y para que eres util?")
    print(resultado)