from langchain_core.prompts import PromptTemplate


template = "Eres un experto en marketing. Sugiere un eslogan creativo para un producto {producto}."

prompt = PromptTemplate(
    input_variables=["producto"],
    template=template
)

prompt_lleno = prompt.format(producto="zapatos deportivos")
print(prompt_lleno)
