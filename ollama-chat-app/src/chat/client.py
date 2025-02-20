import json
import requests
from typing import Optional, Generator
from config.settings import OLLAMA_BASE_URL, MODEL_NAME, MODEL_PARAMS
from utils.logger import log_error, log_info
from .models import ChatResponse, ChatContext, Message
from utils.memory import MemoryManager
from utils.knowledge import KnowledgeBase
class OllamaClient:
    def __init__(self):
        self.base_url = OLLAMA_BASE_URL
        self.model = MODEL_NAME
        self.context = ChatContext()
        self.params = MODEL_PARAMS
        self.memory_manager = MemoryManager()
        self.knowledge_base = KnowledgeBase()

    def chat_stream(self, message: str) -> Generator[str, None, None]:
        try:
            # 获取相关知识
            relevant_knowledge = self.knowledge_base.get_relevant_knowledge(message)
            if relevant_knowledge:
                context = f"基于以下知识来回答问题:\n{relevant_knowledge}\n\n用户问题: {message}"
            else:
                context = message
                
            # 将知识添加到上下文
            self.context.add_message("user", context)
            
            # 获取相关记忆
            relevant_memories = self.memory_manager.get_relevant_memories(message)
            memory_context = self._format_memories(relevant_memories)
            
            # 将记忆添加到用户消息前
            if memory_context:
                self.context.add_message("system", memory_context)
            
            self.context.add_message("user", message)
            
            messages = [{"role": msg.role, "content": msg.content} 
                       for msg in self.context.get_context()]
            
            response = requests.post(
                f"{self.base_url}/api/chat",
                json={
                    "model": self.model,
                    "messages": messages,
                    "stream": True,
                    **self.params
                },
                stream=True
            )
            response.raise_for_status()
            
            full_response = ""
            for line in response.iter_lines():
                if line:
                    try:
                        json_response = json.loads(line)
                        if 'message' in json_response:
                            chunk = json_response['message']['content']
                            full_response += chunk
                            yield chunk
                    except json.JSONDecodeError:
                        continue
                    except Exception as e:
                        log_error(f"处理响应时出错: {str(e)}")
                        continue

            # 保存对话到记忆
            self.memory_manager.save_memory(message, full_response)
            self.context.add_message("assistant", full_response)
            
        except requests.RequestException as e:
            error_msg = f"网络请求错误: {str(e)}"
            log_error(error_msg)
            yield f"\n{error_msg}"
        except Exception as e:
            error_msg = f"系统错误: {str(e)}"
            log_error(error_msg)
            yield f"\n{error_msg}"

    def _format_memories(self, memories: list) -> str:
        """将记忆格式化为上下文字符串"""
        if not memories:
            return ""
            
        context = "以下是相关的历史对话记忆:"
        for memory in memories:
            context += f"用户: {memory['user_input']} 助手: {memory['assistant_response']} "
            
        return context

    def clear_context(self):
        """清除对话上下文，但保留记忆"""
        self.context.clear()
'''
class OllamaClient:
    
    def __init__(self):
        self.base_url = OLLAMA_BASE_URL
        self.model = MODEL_NAME
        self.context = ChatContext()
        self.params = MODEL_PARAMS
        self.memory_manager = MemoryManager()
    def chat_stream(self, message: str) -> Generator[str, None, None]:
     try:
        self.context.add_message("user", message)
        
        messages = [{"role": msg.role, "content": msg.content} 
                   for msg in self.context.get_context()]
        
        response = requests.post(
            f"{self.base_url}/api/chat",
            json={
                "model": self.model,
                "messages": messages,
                "stream": True,
                **self.params  # 添加其他模型参数
            },
            stream=True  # 启用HTTP流式传输
        )
        response.raise_for_status()
        
        full_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    json_response = json.loads(line)
                    if 'message' in json_response:
                        chunk = json_response['message']['content']
                        full_response += chunk
                        yield chunk
                except json.JSONDecodeError:
                    continue
                except Exception as e:
                    log_error(f"处理响应时出错: {str(e)}")
                    continue

        self.context.add_message("assistant", full_response)
        
     except requests.RequestException as e:
        error_msg = f"网络请求错误: {str(e)}"
        log_error(error_msg)
        yield f"\n{error_msg}"
     except Exception as e:
        error_msg = f"系统错误: {str(e)}"
        log_error(error_msg)
        yield f"\n{error_msg}"

    def clear_context(self):
        self.context.clear()
        '''