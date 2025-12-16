          ┌───────────────────────────────────────────────┐
          │                 (1) Preprocesamiento           │
Input →──→│   Limpia texto: strip() y corta a 500 chars    │
          └───────────────────────────────────────────────┘
                               │
                               ▼
       ┌───────────────────────────────────────────────────────────┐
       │            (2) ANÁLISIS EN PARALELO (RunnableParallel)    │
       │   Aquí se ejecutan DOS cosas al MISMO tiempo:             │
       │                                                           │
       │   A) Resumen:        B) Sentimiento:                      │
       │   "Resume este       "Dime si es positivo, negativo,      │
       │    texto..."          o neutro en JSON"                   │
       │                                                           │
       └───────────────────────────────────────────────────────────┘
                               │
                               ▼
        Resultado trabajado por ambas ramas:
        {
          "resumen": "texto resumido...",
          "sentimiento_data": {"sentimiento": "...", "razon": "..."}
        }
                               │
                               ▼
     ┌────────────────────────────────────────────────────────────┐
     │                (3) MERGE FINAL                             │
     │ Combina todo en un solo diccionario limpio:                │
     │ {"resumen": ..., "sentimiento": ..., "razon": ... }        │
     └────────────────────────────────────────────────────────────┘
                               │
                               ▼
                           OUTPUT FINAL
