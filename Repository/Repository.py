from abc import ABC, abstractmethod

class Repository(ABC):

    @abstractmethod
    def get_tests(self):
        pass

    @classmethod
    def create_repo(cls, repo):
        return repo()