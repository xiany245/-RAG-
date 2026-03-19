import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

class Settings:
    PROJECT_NAME: str = "RAG 智能知识库问答系统"
    
    # LLM 相关
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_API_BASE: str = os.getenv("OPENAI_API_BASE", "https://api.deepseek.com/v1")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "deepseek-chat")
    
    # Embedding 相关
    EMBEDDING_MODEL_NAME: str = os.getenv("EMBEDDING_MODEL_NAME", "shibing624/text2vec-base-chinese")
    
    # 路径相关
    VECTOR_STORE_PATH: str = os.getenv("VECTOR_STORE_PATH", "./vector_store/faiss_index")
    DATA_PATH: str = "./data"
    
    # RAG 参数
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", 500))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", 50))

settings = Settings()