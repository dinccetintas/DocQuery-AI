from langchain_community.document_loaders import PyPDFLoader

class DocumentLoader:
    @staticmethod
    def load(file):
        loader = PyPDFLoader(file.name)
        return loader.load()