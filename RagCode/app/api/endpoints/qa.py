from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.qa import QARequest, QAResponse, UploadResponse
from app.services.document_processor import DocumentProcessor
from app.services.vector_store_service import VectorStoreService
from app.services.qa_service import QAService
import os
import shutil

router = APIRouter()

# 初始化服务
doc_processor = DocumentProcessor()
vector_store_service = VectorStoreService()
qa_service = QAService()

@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """上传文档并构建向量索引"""
    # 1. 保存文件到临时目录
    temp_path = f"data/{file.filename}"
    os.makedirs("data", exist_ok=True)
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # 2. 处理文档：解析 -> 切分
        documents = doc_processor.process(temp_path)
        
        # 3. 创建向量库
        vector_store_service.create_vector_store(documents)
        
        return UploadResponse(
            filename=file.filename,
            status="success",
            message="文档已成功处理并存入向量库"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ask", response_model=QAResponse)
async def ask_question(request: QARequest):
    """基于知识库进行问答"""
    try:
        result = qa_service.get_answer(request.query)
        return QAResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))