from abc import ABC, abstractmethod

class Connection(ABC):
    @abstractmethod
    def connect():
        pass