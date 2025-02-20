import json
import os
from datetime import datetime

class MemoryManager:
    def __init__(self, memory_file="memory.json"):
        self.memory_file = memory_file
        self.memories = self._load_memories()
    
    def _load_memories(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_memory(self, user_input: str, assistant_response: str):
        memory = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "assistant_response": assistant_response
        }
        self.memories.append(memory)
        
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(self.memories, f, ensure_ascii=False, indent=2)
    
    def get_relevant_memories(self, query: str, limit: int = 5):
        # 简单实现：返回最近的几条记忆
        return self.memories[-limit:] if self.memories else []