from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

class TextSplitter:
    @staticmethod
    def split(documents, chunk_size=500, chunk_overlap=100):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )
        
        chunks = []
        for doc in documents:
            split_texts = text_splitter.split_text(doc.page_content)
            for text in split_texts:
                chunks.append(Document(page_content=text, metadata=doc.metadata))
        
        return chunks