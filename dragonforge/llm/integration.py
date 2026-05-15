from langchain_ollama import OllamaLLM
# или from groq import Groq  / openai и т.д.

class DragonLLM:
    def __init__(self, model="llama3.2", provider="ollama"):
        self.provider = provider
        if provider == "ollama":
            self.llm = OllamaLLM(model=model, temperature=0.8)

    async def think(self, character, user_message: str, context: Dict) -> str:
        prompt = f"""Ты — {character.name}, {character.soul}.
Контекст: {context}
Пользователь: {user_message}

Отвечай от первого лица, сохраняя характер:"""
        return await self.llm.ainvoke(prompt)