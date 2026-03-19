import os
from typing import List
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from app.core.config import settings
from app.services.embedding_service import EmbeddingService

class VectorStoreService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = None
        self.index_path = settings.VECTOR_STORE_PATH

    def create_vector_store(self, documents: List[Document]):
        """根据切分后的文档创建 FAISS 索引并保存"""
        embeddings = self.embedding_service.get_embeddings()
        # 构建 FAISS 向量库
        self.vector_store = FAISS.from_documents(documents, embeddings)
        
        # 确保目录存在并保存索引
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        self.vector_store.save_local(self.index_path)
        return self.vector_store

    def load_vector_store(self):
        """加载本地已有的 FAISS 索引"""
        embeddings = self.embedding_service.get_embeddings()
        if os.path.exists(self.index_path):
            self.vector_store = FAISS.load_local(
                self.index_path, 
                embeddings, 
                allow_dangerous_deserialization=True # 加载本地文件需要开启此选项
            )
            return self.vector_store
        return None

    def get_retriever(self, search_kwargs={"k": 3}):
        """获取检索器，k 为召回的文档数量"""
        if not self.vector_store:
            self.load_vector_store()
        
        if self.vector_store:
            return self.vector_store.as_retriever(search_kwargs=search_kwargs)
        return None