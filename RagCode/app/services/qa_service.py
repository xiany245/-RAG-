from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from app.core.config import settings
from app.services.vector_store_service import VectorStoreService

class QAService:
    def __init__(self):
        self.vector_store_service = VectorStoreService()
        
        # 1. 初始化大语言模型
        self.llm = ChatOpenAI(
            openai_api_key=settings.OPENAI_API_KEY,
            openai_api_base=settings.OPENAI_API_BASE,
            model_name=settings.LLM_MODEL,
            temperature=0  # 设置为 0 保证回答更严谨
        )
        
        # 2. 定义 Prompt 模板
        self.prompt_template = """你是一个专业的企业知识库助手。请根据提供的上下文信息（Context）来回答用户的问题。
如果你在上下文中找不到答案，请诚实地告诉用户你不知道，不要胡乱猜测。

上下文：
{context}

用户问题：
{question}

你的回答："""
        
        self.QA_PROMPT = PromptTemplate(
            template=self.prompt_template, 
            input_variables=["context", "question"]
        )

    def get_answer(self, query: str):
        """执行 RAG 流程：检索 -> 增强 -> 生成"""
        retriever = self.vector_store_service.get_retriever()
        if not retriever:
            return "知识库为空，请先上传文档。"

        # 3. 构建问答链
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff", # "stuff" 是将检索到的文档全部塞进 Prompt
            retriever=retriever,
            chain_type_kwargs={"prompt": self.QA_PROMPT},
            return_source_documents=True # 返回参考的源文档
        )
        
        # 4. 获取结果
        result = qa_chain({"query": query})
        return {
            "answer": result["result"],
            "source_documents": [doc.metadata.get("source", "unknown") for doc in result["source_documents"]]
        }