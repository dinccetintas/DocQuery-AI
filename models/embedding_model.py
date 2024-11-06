from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames
from config.config import Config
from langchain_ibm import WatsonxEmbeddings
import os

os.environ["WATSONX_APIKEY"] = Config.API_KEY

class EmbeddingModel:
    @staticmethod
    def initialize():
        embed_params = {
            EmbedTextParamsMetaNames.TRUNCATE_INPUT_TOKENS: 3,
            EmbedTextParamsMetaNames.RETURN_OPTIONS: {"input_text": True}
        }

        return WatsonxEmbeddings(
            model_id=Config.EMBEDDING_MODEL,
            url=Config.URL,
            project_id=Config.PROJECT_ID,
            params=embed_params,
        )