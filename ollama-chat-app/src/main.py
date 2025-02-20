from chat.client import OllamaClient
from utils.logger import log_info
import signal
import sys

def signal_handler(sig, frame):
    print("\n\n程序正在退出...")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    client = OllamaClient()
    log_info("Chat application started")
    
    print("欢迎与玲源真天慧雅美紫对话!")
    print("\n命令说明:")
    print("- 输入 'quit' 退出程序")
    print("- 输入 'clear' 清除对话历史")
    print("- 输入 'memory' 查看存储的记忆")
    print("- 输入 'upload <文件路径>' 上传知识库文件")
    print("- 按 Ctrl+C 强制退出\n")
    
    while True:
        try:
            user_input = input("\n你: ").strip()
            
            if not user_input:  # 忽略空输入
                continue

            if user_input.lower().startswith('upload '):
                file_path = user_input[7:].strip()
                if client.knowledge_base.add_file(file_path):
                    print(f"\n系统: 成功添加文件到知识库: {file_path}")
                else:
                    print("\n系统: 添加文件失败")
                continue

            if user_input.lower() == 'quit':
                break
            elif user_input.lower() == 'clear':
                client.clear_context()
                print("\n系统: 对话历史已清除")
                continue
            elif user_input.lower() == 'memory':
                memories = client.memory_manager.get_relevant_memories("", limit=10)
                print("\n最近的记忆:")
                for memory in memories:
                   print(f"\n时间: {memory['timestamp']}")
                   print(f"用户: {memory['user_input']}")
                   print(f"AI: {memory['assistant_response']}")
                continue
            print("\n玲源真天慧雅美紫:", end='', flush=True)
            for chunk in client.chat_stream(user_input):
                print(chunk, end='', flush=True)
            print()
            
        except Exception as e:
            print(f"\n系统错误: {str(e)}")
    
    print("\n感谢使用，再见！")

if __name__ == "__main__":
    main()