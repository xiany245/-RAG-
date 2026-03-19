from fastapi import FastAPI
import uvicorn
from app.api.endpoints import qa
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# 注册路由
app.include_router(qa.router, prefix="/api/v1", tags=["问答系统"])

@app.get("/")
async def root():
    return {"message": f"欢迎使用 {settings.PROJECT_NAME}"}

if __name__ == "__main__":
    # 启动命令：在项目根目录运行 python -m app.main
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)