import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = "http://localhost:11434"
MODEL_NAME = "qwen2.5:latest"

# 模型参数配置
MODEL_PARAMS = {
    "temperature": 0.6,
    "top_p": 0.8,
    "stream": True
}