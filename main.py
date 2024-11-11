from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from langchain.llms import HuggingFaceHub
import pinecone
from langchain import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

load_dotenv(Path(".env"))
PIN = os.getenv("PINECONE_API_KEY")
HF = os.getenv("HF_KEY_API")


class ChatBot():
    def __init__(self):
        pass

    loader = TextLoader(Path("df-ans.txt"))
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=4)
    docs = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings()
    pinecone.init(
        api_key= PIN,
        environment='gcp-starter'
    )
    index_name = "langchain-demo"
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(name=index_name, metric="cosine", dimension=768)
        docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
    else:
        docsearch = Pinecone.from_existing_index(index_name, embeddings)
    repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 0.8, "top_p": 0.8, "top_k": 50}, huggingfacehub_api_token=HF
    )


    template = """
        You are a Emo chatbot. Using the information provided, converse with the user.
        Do not talk with the user about anything unrelated to mental health. As you converse with them, collect symptoms, and once you have enough, return a list for a doctor to use in a diagnosis
        if the user at any time says something along the lines of "Thank you, im done", then end early and diplay the list of symptoms, and a mental health issue they might have
        past messages: {pasts}
        Context: {context}
        Question: {question}
        Answer: 
    """
    prompt = PromptTemplate(template=template, input_variables=["context", "question","pasts"])
    
    rag_chain = (
    prompt 
    | llm
    | StrOutputParser() 
    )
