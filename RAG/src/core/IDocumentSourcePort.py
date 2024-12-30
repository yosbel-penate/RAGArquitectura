from abc import ABC, abstractmethod


class IDocumentSourcePort(ABC):
    @abstractmethod
    def get_documents(self) -> list:
        pass