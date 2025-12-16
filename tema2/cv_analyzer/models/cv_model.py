from pydantic import BaseModel, Field
from typing import List

class AnalisisCV(BaseModel):
    """ Modelo para analisis de cv """
    nombre_candidato: str = Field(
        description="Nombre completo del candidato extraído del CV"
    )
    habilidades_clave: List[str] = Field(
        description="Habilidades técnicas o profesionales más relevantes"
    )
    experiencia_relevante: int = Field(
        description="Años de experiencia directamente relacionados con el rol"
    )
    education: str = Field(
        description="Educación más relevante para el perfil"
    )
    fortalezas_principales: List[str] = Field(
        description="3 a 5 fortalezas principales basadas en el perfil del candidato"
    )
    areas_mejora: List[str] = Field(
        description="4 áreas donde el candidato puede mejorar profesionalmente"
    )
    
    porcentaje_ajuste: int = Field(description="Porcentaje de ajuste al puesto entre (0-100) basado en la experiencia, habilidades y formacion",ge=0,le=100)