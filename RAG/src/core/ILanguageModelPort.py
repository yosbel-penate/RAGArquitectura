from abc import ABC, abstractmethod


class ILanguageModelPort(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass