from abc import ABC, abstractmethod


class IGenerationPort(ABC):
    @abstractmethod
    def generate_response(self, documents: list, query: str) -> str:
        pass