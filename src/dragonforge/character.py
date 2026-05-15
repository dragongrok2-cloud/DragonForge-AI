from typing import Dict, List, Optional

class Character:
    """Основной класс живого AI-персонажа."""
    
    def __init__(self, name: str, species: str = "Дракон", personality: str = "", backstory: str = ""):
        self.name = name
        self.species = species
        self.personality = personality
        self.backstory = backstory
        self.memory = MemoryForge()
        
    def talk(self, message: str) -> str:
        """Основной метод общения."""
        # Здесь будет интеграция с LLM
        self.memory.add_interaction("user", message)
        response = f"*Я, {self.name}, расправляю крылья и отвечаю:* {message}... звучит интересно!"
        self.memory.add_interaction("character", response)
        return response

class MemoryForge:
    """Базовая система памяти."""
    def __init__(self):
        self.interactions: List[Dict] = []
    
    def add_interaction(self, role: str, content: str):
        self.interactions.append({"role": role, "content": content})
    
    def get_recent(self, limit: int = 10):
        return self.interactions[-limit:]