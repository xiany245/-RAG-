# -RAG-
本项目是一个基于检索增强生成（RAG）的智能知识库问答系统，旨在实现对企业内部文档（如 PDF, Word, TXT）的高效语义检索与智能问答。
## ✨ 项目特色

- **多文档格式支持**: 可直接上传 PDF, Word, TXT 等常见格式的文档作为知识源。
- **语义检索**: 使用 `SentenceTransformer` 生成高质量的文本向量，并通过 `FAISS` 实现高效的相似度检索，确保召回与问题最相关的知识片段。
- **上下文增强生成**: 将检索到的知识片段作为上下文（Context）注入到大语言模型（LLM）的 Prompt 中，显著提升回答的准确性和相关性。
- **API 驱动**: 基于 `FastAPI` 构建服务化接口，易于集成和扩展。
- **灵活配置**: 支持通过 `.env` 文件灵活配置 API Key、模型名称和各类路径。

## 🛠️ 技术栈

- **后端框架**: FastAPI
- **RAG 核心**: LangChain
- **向量数据库**: FAISS (Facebook AI Similarity Search)
- **文本向量化**: SentenceTransformer (`shibing624/text2vec-base-chinese`)
- **大语言模型 (LLM)**: DeepSeek (兼容 OpenAI 接口)
- **环境管理**: python-dotenv

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone <your-repository-url>
cd RagCode
```

### 2. 配置环境

首先，复制 `.env.example` 文件（如果提供）或手动创建 `.env` 文件，并填入你的 API Key 等信息。

```bash
# .env
OPENAI_API_KEY=your_deepseek_api_key_here
OPENAI_API_BASE=https://api.deepseek.com/v1
LLM_MODEL=deepseek-chat
EMBEDDING_MODEL_NAME=shibing624/text2vec-base-chinese
VECTOR_STORE_PATH=./vector_store/faiss_index
```

### 3. 安装依赖

建议在虚拟环境中安装项目所需的依赖包。

```bash
pip install -r requirements.txt
```

### 4. 启动服务

在项目根目录下运行以下命令：

```bash
python -m app.main
```
