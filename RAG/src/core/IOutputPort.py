from abc import ABC, abstractmethod


class IOutputPort(ABC):
    @abstractmethod
    def present_response(self, response: str) -> None:
        pass