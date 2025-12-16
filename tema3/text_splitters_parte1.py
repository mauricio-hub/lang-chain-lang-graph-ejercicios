from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Cargar el documento PDF
loader = PyPDFLoader("C:\\Users\\mgdev\\Desktop\\projects\\curso_langchain\\tema3\\text_splitters_parte1.py")
pages = loader.load()

#dividir texto en chunkcs

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size =10000,
    chunk_overlap = 200
)

chunks = text_splitter.split_documents(pages)


# 2. Combinar todas las páginas en un texto único
""" full_text = ""
for page in pages:
    full_text += page.page_content + "\n"
 """
 
# 3. Pasar el texto al LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

summaries = []

for chunk in chunks:
    response = llm.invoke(f"Haz un resumen de los puntos mas importantes del siguiente text: {chunk.page_content}")
    summaries.append(response.content)
    
final_summary = llm.invoke(f"Combina y sintetiza estos resumenes en un resumen coherente y completo : {" ".join(summaries)}")

    
    
print(final_summary.content)