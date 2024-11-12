from UI.main_window import UI
from export.ms_word import MSWord
from json_handler import JSONHandler

def main():
    json_handler = JSONHandler("test_data.json")
    ui = UI(json_handler)
    ui.run()

    ms_word = MSWord(json_handler)

    try:
        ms_word.export()
        ui.notify("TOL successfully exported")
    except Exception as e:
        ui.notify(e)

if __name__ == "__main__":
    main()