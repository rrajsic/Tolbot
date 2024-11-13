from ..repository_factory import RepositoryFactory
from .gerrit_repository import GerritRepository

class GerritRepositoryFactory(RepositoryFactory):
    def __init__(self, servers):
        self.servers = servers

    def get_servers(self):
        return self.servers
    
    def create_repository(self, server, change_id=None, revision_id=None, user=None):
        return GerritRepository(
            server=server,
            change_id=change_id,
            revision_id=revision_id,
            user=user
        )


