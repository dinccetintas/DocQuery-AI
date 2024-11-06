from retriever.retriever import Retriever
from models.llm_model import LLMModel
from langchain.chains import RetrievalQA

class RAGChatbot:
    def __init__(self, model_id):
        self.llm = LLMModel.initialize()
    
    def answer_query(self, file, query):
        retriever_obj = Retriever.retrieve(file)
        qa = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever_obj,
            return_source_documents=False
        )
        response = qa.invoke(query)
        return response['result']