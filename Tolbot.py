import DEBUG_CONSTANTS

from UI.ui import UI
from Repository.Gerrit.GerritRepository import GerritRepository
from Repository.Gtms.GtmsRepository import GtmsRepository
from User.User import User
from Export.MSWord import MSWord


def main():
    # user =  {'username' : DEBUG_CONSTANTS.USERNAME,
    #          'password' : DEBUG_CONSTANTS.PASSWORD}

    # gerrit_repository = GerritRepository('***REMOVED***', DEBUG_CONSTANTS.CHANGE_ID, DEBUG_CONSTANTS.REVISION_ID, user)
    # repo = gerrit_repository.get_repo()

    # tests = gerrit_repository.get_tests()
    # suites = gerrit_repository.get_change_files()

    # gerrit_repository2 = GerritRepository('***REMOVED***',"I3cdac9f5d4e0f0c82b6935fb17f425d111a29f06","5b1ef982c893d7be3beee7062ac7017515bf0676", user)
    # repo2 = gerrit_repository2.get_repo()
    # tests2 = gerrit_repository2.get_tests()
    # suites2 = gerrit_repository2.get_change_files()

    # ms_word = MSWord("SP9999-2", "xFT-Cortex")
    # ms_word.create_statistic_page(suites | suites2, tests + tests2)
    # ms_word.fill_test_data(repo, tests)
    # ms_word.fill_test_data(repo2, tests2)
    # ms_word.save()

    # gtms_repository = GtmsRepository(user)
    # tests = gtms_repository.get_tests("c629b8b4-5bb0-4b9e-a578-483d7356f15a", user)

    ui = UI()
    ui.run_login()

if __name__ == "__main__":
    main()