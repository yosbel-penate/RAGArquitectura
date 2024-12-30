from abc import ABC, abstractmethod


class IInputPort(ABC):
    @abstractmethod
    def process_query(self, query: str) -> str:
        pass