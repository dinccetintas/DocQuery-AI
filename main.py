from utils.suppress_warnings import suppress_warnings
from app.interface import ChatInterface
from config.config import Config
import os

if __name__ == "__main__":
    suppress_warnings()
    os.environ["WATSONX_APIKEY"] = Config.API_KEY
    chat_interface = ChatInterface()
    chat_interface.launch()