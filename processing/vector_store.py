from langchain_community.vectorstores import Chroma
from models.embedding_model import EmbeddingModel

class VectorStore:
    @staticmethod
    def initialize(chunks):
        embedding_model = EmbeddingModel.initialize()
        return Chroma.from_documents(chunks, embedding_model)