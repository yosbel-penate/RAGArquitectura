from abc import ABC, abstractmethod


class IRetrievalPort(ABC):
    @abstractmethod
    def retrieve_documents(self, query: str) -> list:
        pass