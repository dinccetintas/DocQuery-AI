import gradio as gr
from app.chatbot import RAGChatbot
from config.config import config

class ChatInterface:
    def __init__(self):
        self.chatbot = RAGChatbot()
    
    def launch(self):
        interface = gr.Interface(
            fn=self.chatbot.answer_query,
            inputs=[
                gr.File(label="Upload PDF File", file_count="single", file_types=['.pdf'], type="filepath"),
                gr.Textbox(label="Input Query", lines=2, placeholder="Type your question here...")
            ],
            outputs=gr.Textbox(label="Output"),
            title="RAG Chatbot",
            description="Upload a PDF document and ask any question. The chatbot will answer from the provided document",
            allow_flagging="never"
        )
        interface.launch(server_name="0.0.0.0", server_port=7860)