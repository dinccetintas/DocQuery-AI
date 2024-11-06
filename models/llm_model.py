from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from config.config import Config
from langchain_ibm import WatsonxLLM

class LLMModel:
    @staticmethod
    def initialize():
        paramaters = {
            GenParams.MAX_NEW_TOKENS: 256,
            GenParams.MIN_NEW_TOKENS: 1,
            GenParams.TEMPERATURE: 0.5
        }
        credentials = Credentials(url=Config.URL, api_key=Config.API_KEY)

        model = ModelInference(
            model_id= Config.LLM_MODEL,
            params= paramaters,
            project_id=Config.PROJECT_ID,
            credentials= credentials
        )

        return WatsonxLLM(watsonx_model = model)