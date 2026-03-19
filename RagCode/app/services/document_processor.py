import os
from app.core.config import settings
from typing import List
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class DocumentProcessor:
    def __init__(self, chunk_size: int = settings.CHUNK_SIZE, chunk_overlap: int = settings.CHUNK_OVERLAP):
        # 初始化文本切分器，chunk_size 控制每块的大小，chunk_overlap 保证上下文连贯
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", "。", "！", "？", " ", ""]
        )

    def load_document(self, file_path: str) -> List[Document]:
        """根据文件后缀加载文档"""
        ext = os.path.splitext(file_path)[-1].lower()
        if ext == ".pdf":
            loader = PyPDFLoader(file_path)
        elif ext == ".docx":
            loader = Docx2txtLoader(file_path)
        elif ext == ".txt":
            loader = TextLoader(file_path, encoding="utf-8")
        else:
            raise ValueError(f"不支持的文件格式: {ext}")
        
        return loader.load()

    def split_documents(self, documents: List[Document]) -> List[Document]:
        """将加载的文档切分成小块"""
        return self.text_splitter.split_documents(documents)

    def process(self, file_path: str) -> List[Document]:
        """封装完整的解析和切分流程"""
        docs = self.load_document(file_path)
        return self.split_documents(docs)