import os
from dotenv import load_dotenv
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()

class ConfigLoader:
    def __init__(self):
        print("Loaded config...")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]

class ModelLoader:
    def __init__(self, model_provider: str = "groq"):
        self.config = ConfigLoader()
        self.model_provider = model_provider

    def load_llm(self):
        if self.model_provider.lower() == "groq":
            print("Loading LLM from Groq...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            if not groq_api_key:
                raise ValueError("GROQ_API_KEY environment variable is required")
            
            model_name = self.config["llm"]["groq"]["model_name"]
            return ChatGroq(model=model_name, api_key=groq_api_key)
        
        elif self.model_provider.lower() == "openai":
            print("Loading LLM from OpenAI...")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("OPENAI_API_KEY environment variable is required")
            
            model_name = self.config["llm"]["openai"]["model_name"]
            return ChatOpenAI(model=model_name, api_key=openai_api_key)
        
        else:
            raise ValueError(f"Unsupported model provider: {self.model_provider}. Supported providers: groq, openai")
