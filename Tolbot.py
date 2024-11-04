import DEBUG_CONSTANTS

from Export.MSWord import MSWord
from UI.ui import UI
from Repository.Gerrit.GerritRepository import GerritRepository
from Repository.Gtms.GtmsRepository import GtmsRepository
from User.User import User



def main():
    user =  {'username' : DEBUG_CONSTANTS.USERNAME,
             'password' : DEBUG_CONSTANTS.PASSWORD}

    gerrit_repository2 = GerritRepository('***REMOVED***',"I2d96e5333507e701b851e2e44d7accc7d6f0219f","b2dfd24d7409ced285f3cdac313925ff75b651a7", user)
    repo2 = gerrit_repository2.get_repo()
    tests2 = gerrit_repository2.get_tests()
    suites2 = gerrit_repository2.get_change_files()

    gerrit_repository3 = GerritRepository('***REMOVED***',"I30bc219b20ddf756c49d6941f66f40a253eaa27f","95617bbc84cea9a6574f070bdde6ab0c05d83fdb", user)
    repo3 = gerrit_repository3.get_repo()
    tests3 = gerrit_repository3.get_tests()
    suites3 = gerrit_repository3.get_change_files()

    ms_word = MSWord("SP742-1", "xFT-Cortex")
    ms_word.create_statistic_page(suites2 | suites3, tests2 + tests3)
    ms_word.fill_test_data(repo2, tests2)
    ms_word.fill_test_data(repo3, tests3)
    ms_word.save()

    # gtms_repository = GtmsRepository(user)
    # tests = gtms_repository.get_tests("c629b8b4-5bb0-4b9e-a578-483d7356f15a", user)








    # ui = UI()
    # ui.start_main_window(user)
    # user = ui.run_login()
    # gerrit_repository = ui.run_gerrit_form_ui(user)
    # repo = gerrit_repository.get_repo()

    # tests = gerrit_repository.get_tests()
    # suites = gerrit_repository.get_change_files()
    # ms_word = MSWord("SP9999-2", "xFT-Cortex")
    # ms_word.create_statistic_page(suites, tests)
    # ms_word.fill_test_data(repo, tests)
    # ms_word.save()

if __name__ == "__main__":
    main()