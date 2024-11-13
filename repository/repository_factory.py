from abc import ABC, abstractmethod

class RepositoryFactory(ABC):
    @abstractmethod
    def create_repository(self, server, change_id, revision_id, user):
        pass
    @abstractmethod
    def get_servers(self):
        pass