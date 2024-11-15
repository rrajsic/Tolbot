from UI.tkinter.main_window import TkinterUI
from export.ms_word.ms_word import MSWord
from json_handler import JSONHandler
from repository.gerrit.gerrit_repository_factory import GerritRepositoryFactory
from server_config import ServerConfig


def main():
    json_handler = JSONHandler("test_data.json")
    server_config = ServerConfig("servers_config.json")
    servers = []
    servers = server_config.import_from_json()

    ui = TkinterUI(json_handler, GerritRepositoryFactory(servers))
    ui.run()

    exporter = MSWord(json_handler)

    try:
        exporter.export()
        ui.notify("TOL successfully exported")
    except Exception as e:
        ui.notify(e)

if __name__ == "__main__":
    main()