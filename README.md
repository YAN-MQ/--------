# 玲源真天慧雅美紫 AI 助手

这是一个基于 Ollama 本地部署的 AI 对话助手应用程序,使用 qwen2.5 模型,支持上下文记忆和对话历史保存功能。

## 功能特点

- 基于 qwen2.5 模型的智能对话
- 支持流式响应输出
- 自动保存对话记忆
- 支持查看历史记忆
- 清除对话上下文
- 优雅的退出处理

## 部署步骤



```bash
1. 安装 Ollama
# Windows 安装
# 下载 Ollama 安装包
访问 https://ollama.ai/download 下载 Windows 安装包

# 运行安装包完成安装

# Linux 安装
curl -fsSL https://ollama.ai/install.sh | sh

2. 下载 qwen2.5 模型
# 打开终端运行
ollama pull qwen2.5:latest

3. 安装 Python 依赖
# 创建并激活虚拟环境(可选)
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows
# 安装依赖
pip install -r requirements.txt

4. 配置项目
确保 Ollama 服务运行在 http://localhost:11434
检查 settings.py 中的配置是否正确

5. 运行程序
python src/main.py

使用说明
程序启动后支持以下命令:

quit: 退出程序
clear: 清除当前对话上下文
memory: 查看存储的历史记忆
Ctrl+C: 强制退出程序

项目结构
ollama-chat-app/
├── src/
│   ├── main.py          # 程序入口
│   ├── chat/
│   │   ├── client.py    # Ollama 客户端
│   │   └── models.py    # 数据模型
│   ├── config/
│   │   └── settings.py  # 配置文件
│   └── utils/
│       ├── logger.py    # 日志工具
│       └── memory.py    # 记忆管理
├── tests/               # 测试文件
└── requirements.txt     # 项目依赖

开发说明
使用 Python 3.x 开发
采用 requests 库进行 HTTP 请求
支持流式响应处理
实现了记忆管理系统
使用 JSON 文件持久化存储对话历史
技术栈
Python 3.x
Ollama API
requests
python-dotenv
logging
许可证
MIT License

作者
lithic

贡献
欢迎提交 Issues 和 Pull Requests!
