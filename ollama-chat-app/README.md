# README.md

# Ollama Chat App

这是一个基于本地部署的 `qwen2.5:latest` 模型的 AI 对话程序。该应用程序允许用户与模型进行交互，发送消息并接收响应。

## 项目结构

- `src/main.py`：应用程序的入口点，负责启动聊天程序并处理用户输入。
- `src/chat/`：包含与聊天相关的功能。
  - `client.py`：负责与模型进行交互。
  - `models.py`：定义聊天相关的数据模型。
- `src/config/`：包含应用程序的配置设置。
- `src/utils/`：提供实用工具，例如日志记录功能。
- `tests/`：包含对应用程序功能的单元测试。

## 安装依赖

请确保您已安装 Python 3.x。然后，您可以使用以下命令安装项目所需的依赖项：

```
pip install -r requirements.txt
```

## 使用说明

1. 配置 `.env` 文件以设置 API 密钥和其他环境变量。
2. 运行主程序：

```
python src/main.py
```

## 贡献

欢迎任何形式的贡献！请提交问题或拉取请求。

## 许可证

此项目采用 MIT 许可证。