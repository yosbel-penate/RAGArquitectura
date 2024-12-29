from abc import ABC, abstractmethod


class VectorStorePort(ABC):
    @abstractmethod
    def search_fragments(self, query: str) -> list:
        pass

    @abstractmethod
    def index_documents(self, documents: list) -> None:
        pass