from UI.main_window import UI
from export.ms_word import MSWord

def main():
    ui = UI()
    data = ui.run()

    ms_word = MSWord(data["sp_name"], data["team_name"])
    ms_word.create_statistic_page(data["files"], data["tests"])
    for repo, test in zip(data["repos"], data["tests"]):
        ms_word.fill_test_data(repo, test)

    ms_word.save(data["sp_name"])

if __name__ == "__main__":
    main()