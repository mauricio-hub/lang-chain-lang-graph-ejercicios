from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
import streamlit as st

from config import *

from dotenv import load_dotenv

from tema3.asistente_legal_rag.prompts import MULTI_QUERY_PROMPT, RAG_TEMPLATE
# Carga variables de entorno (.env)
load_dotenv()


def initialize_rag_system():
   
   #vector store a consultar
   
   vectorestore = Chroma(
       persist_directory=CHROMA_DB_PATH,
         embedding_function=OpenAIEmbeddings(model=EMBEDDING_MODEL)
    )
   
   # modelos para diferentes tareas en RAG
   llm_query = ChatOpenAI(model=QUERY_MODEL, temperature=0)
   
   llm_generation = ChatOpenAI(model=GENERATION_MODEL, temperature=0)
   
   #retriever mmr (maximal marginal relevance
   # utiliza múltiples queries para mejorar la recuperación
   # y reducir la redundancia en los resultados)
   
   base_retriever = vectorestore.as_retriever(
         search_type=SEARCH_TYPE,
            search_kwargs={
                "k": SEARCH_K,
                "lambda_mult": MMR_DIVERSITY_LAMBDA,
                "fetch_k": MMR_FETCH_K
            }
   )
   

    # prompt personalizado para multiquery retriever
   multi_query_prompt = PromptTemplate.from_template(MULTI_QUERY_PROMPT)
   # multiquery retriever con prompt personalizado
   mmr_multiquery_retriever = MultiQueryRetriever(
         base_retriever=base_retriever,
         llm=llm_query,
         prompt=multi_query_prompt,
        # output_parser=StrOutputParser(),
        # return_all_queries=True
        )
        
   prompt = PromptTemplate.from_template(RAG_TEMPLATE)
   
   rag_chain = (
       {
              "context": mmr_multiquery_retriever,
              "question": RunnablePassthrough()
       }
         | prompt
         | llm_generation
         | StrOutputParser()
   )     
   
   return rag_chain , mmr_multiquery_retriever