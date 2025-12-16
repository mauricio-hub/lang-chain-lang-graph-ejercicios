from langchain_community.document_loaders import GoogleDriveLoader

credential_path = ""
token_path = ""


loader = GoogleDriveLoader(
    folder_id="",
    credentials_path=credential_path,
    token_path=token_path,
    recursive=True
)

documents = loader.load() 

#print(documents)

print(f"Metadatos: {documents[0].metadata}")
print(f"Contenidos: {documents[0].page_content}")