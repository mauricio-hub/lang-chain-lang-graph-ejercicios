from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
load_dotenv()

chat = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

pltantilla_sistema = SystemMessagePromptTemplate.from_template("" \
    "Eres un {rol} que responde de manera {tono} a las preguntas del usuario." ""
    )


plantilla_humana = HumanMessagePromptTemplate.from_template("Mi pregunta sobre {tema} es: {pregunta}")


chat_prompt = ChatPromptTemplate.from_messages([
    pltantilla_sistema,
    plantilla_humana
])

mensaje = chat_prompt.format_messages(
    rol="nutricionista",
    especialidad="alimentacion saludable",
    tono="profesional y hostil",
    tema="nutricion",
    pregunta="¿Cuales son los beneficios de una dieta balanceada?"
) 


for msg in mensaje:
    print(f"{msg.type}: {msg.content}")
    
