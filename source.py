from UI.tkinter.main_window import TkinterUI
from export.ms_word.ms_word import MSWord
from json_handler import JSONHandler
from repository.gerrit.gerrit_repository_factory import GerritRepositoryFactory


def main():
    json_handler = JSONHandler("test_data.json")

    ui = TkinterUI(json_handler, GerritRepositoryFactory(["***REMOVED***","silver spoon in hand"]))
    ui.run()

    exporter = MSWord(json_handler)

    try:
        exporter.export()
        ui.notify("TOL successfully exported")
    except Exception as e:
        ui.notify(e)

if __name__ == "__main__":
    main()