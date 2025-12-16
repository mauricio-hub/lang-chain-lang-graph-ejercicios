from langchain_core.messages import HumanMessage , AIMessage
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente útil que mantiene el contexto de la conversacion."),
    MessagesPlaceholder(variable_name="historial_conversacion"),
    ("human", "{input}"),
])



historial_conversacion = [
    HumanMessage(content="Hola, ¿cómo estás?"),
    AIMessage(content="¡Hola! Estoy bien, gracias. ¿En qué puedo ayudarte hoy?"),
    HumanMessage(content="¿Puedes contarme un chiste?"),
    AIMessage(content="Claro, aquí tienes uno: ¿Por qué los programadores confunden Halloween con Navidad? Porque OCT 31 es igual a DEC 25."),

]

mensaje = chat_prompt.format_messages(
    historial_conversacion=historial_conversacion,
    input="¿Cual es la capital de Francia?",  
)


for msg in mensaje:
    print(f"{msg.type}: {msg.content}")
# Salida esperada:
# system: Eres un asistente útil que mantiene el contexto de la conversacion.   
