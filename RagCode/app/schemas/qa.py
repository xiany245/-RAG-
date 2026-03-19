from pydantic import BaseModel
from typing import List, Optional

class QARequest(BaseModel):
    query: str

class QAResponse(BaseModel):
    answer: str
    source_documents: List[str]

class UploadResponse(BaseModel):
    filename: str
    status: str
    message: str