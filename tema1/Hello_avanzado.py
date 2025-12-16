from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
#from langchain.chains import LLMChain

load_dotenv()

chat = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


plantilla = PromptTemplate(
    input_variables=["nombre"],
    template="Escribe un saludo personalizado para {nombre}\nAsistente:"
)

chain = plantilla | chat


resultado = chain.invoke({"nombre": "Mauricio"})
print(resultado.content)