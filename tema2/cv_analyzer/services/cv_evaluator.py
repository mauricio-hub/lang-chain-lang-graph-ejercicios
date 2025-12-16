from langchain_openai import ChatOpenAI
from models.cv_model  import AnalisisCV
from prompts.cv_prompts import crear_sistema_prompts
from dotenv import load_dotenv
load_dotenv()


def crear_evaluador_cv():
    model_base  = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    
    modelo_estructurado = model_base.with_structured_output(AnalisisCV)

    chat_prompt = crear_sistema_prompts()
    
    cadena_evaluacion = chat_prompt | modelo_estructurado
    
    return cadena_evaluacion

   
def evaluar_candidato(texto_cv:str,descripcion_puesto:str) -> AnalisisCV:
    
    try:
        cadena_evaluacion = crear_evaluador_cv()
        
        resultado = cadena_evaluacion.invoke({
            "texto_cv":texto_cv,
            "descripcion_puesto":descripcion_puesto
        })
        
        return resultado
    
    except Exception as e:
        return AnalisisCV(
            nombre_candidato="No identificado",
            habilidades_clave=["Requiere revisión manual del CV"],
            experiencia_relevante=0,
            education="No identificada",
            fortalezas_principales=["Requiere revisión manual del CV"],
            areas_mejora=["No se pudieron identificar áreas de mejora automáticamente"]
        )
        