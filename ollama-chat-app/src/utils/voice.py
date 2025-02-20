import asyncio
import edge_tts

class VoiceHandler:
    def __init__(self):
        self.voice = "zh-CN-XiaoyiNeural"  # 女性声音
        self.rate = "+0%"
        self.volume = "+0%"

    async def text_to_speech(self, text: str):
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save("output.mp3")
        
    def speak(self, text: str):
        asyncio.run(self.text_to_speech(text))