from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def get_tests(self):
        pass
    @abstractmethod
    def get_change_files(self):
        pass
    @abstractmethod
    def get_repo(self):
        pass