"""Load html from files, clean up, split, ingest into Weaviate."""
import pickle

from langchain.document_loaders import ReadTheDocsLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS

class SimpleDocument:
    def __init__(self, page_content, metadata=None):
        self.page_content = page_content
        self.metadata = metadata if metadata else {}



def ingest_docs():
    """Get documents from web pages."""
    with open('langchain_docs.html', 'r') as file:
        html_content = file.read()
    raw_documents = [SimpleDocument(html_content)]

    # raw_documents = loader.load()
    print("number of raw documents:", len(raw_documents))
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    
    documents = text_splitter.split_documents(raw_documents)
    documents = documents[:1]
    print("Number of split documents:", len(documents))

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Save vectorstore
    with open("vectorstore.pkl", "wb") as f:
        pickle.dump(vectorstore, f)


if __name__ == "__main__":
    ingest_docs()
