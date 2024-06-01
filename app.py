import streamlit as st

from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
import os

index_name = 'mvp'
embeddings = OpenAIEmbeddings(model = "text-embedding-3-large")
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)


# Criar uma caixa de entrada de texto
query = st.text_input("Write something here and press Enter:")

# Verificar se o texto foi digitado e enviar para a API
if query:
    # Enviar o texto para a API
    results = vectorstore.similarity_search(query)

    c = 1
    for x in results:
        st.write(f"Empresa {c}")
        st.write(x.page_content)
        c += 1

