from langchain_community.document_loaders import PyPDFLoader , WebBaseLoader
from bs4 import BeautifulSoup
""" 
loader = PyPDFLoader("C:\\Users\\mgdev\\Desktop\\projects\\curso_langchain\\tema3\\React Inter.pdf")


pages = loader.load()


#print(dir(pages[0]))

for i , page in enumerate(pages):
    print(f"=== Pagina {i+1} ===")
    print(f"Contenidos: {page.page_content}")
    print(f"Metadatos: {page.metadata}") """
    
    
 
loader = WebBaseLoader("https://www.langchain.com/") 

docs = loader.load()

print(docs)  