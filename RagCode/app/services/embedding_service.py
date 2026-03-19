from langchain_community.embeddings import HuggingFaceEmbeddings
from app.core.config import settings

class EmbeddingService:
    def __init__(self):
        # 使用配置文件中的模型名称初始化 HuggingFaceEmbeddings (基于 SentenceTransformer)
        self.embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL_NAME,
            model_kwargs={'device': 'cpu'} # 如果你有 GPU，可以改为 'cuda'
        )

    def get_embeddings(self):
        return self.embeddings