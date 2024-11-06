from processing.document_loader import DocumentLoader
from processing.text_splitter import TextSplitter
from processing.vector_store import VectorStore

class Retriever:
    @staticmethod
    def retrieve(file):
        documents = DocumentLoader.load(file)
        chunks = TextSplitter.split(documents)
        vectordb = VectorStore.initialize(chunks)
        return vectordb.as_retriever(search_type="mmr", search_kwargs={"k": 5})