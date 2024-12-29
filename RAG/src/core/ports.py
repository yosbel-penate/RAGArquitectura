from abc import ABC, abstractmethod

class InputPort(ABC):
    @abstractmethod
    def process_query(self, query: str) -> str:
        pass

class RetrievalPort(ABC):
    @abstractmethod
    def retrieve_documents(self, query: str) -> list:
        pass

class GenerationPort(ABC):
    @abstractmethod
    def generate_response(self, documents: list, query: str) -> str:
        pass

class OutputPort(ABC):
    @abstractmethod
    def present_response(self, response: str) -> None:
        pass

class VectorStorePort(ABC):
    @abstractmethod
    def search_fragments(self, query: str) -> list:
        pass

    @abstractmethod
    def index_documents(self, documents: list) -> None:
        pass

class DocumentSourcePort(ABC):
    @abstractmethod
    def get_documents(self) -> list:
        pass

class LanguageModelPort(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass
