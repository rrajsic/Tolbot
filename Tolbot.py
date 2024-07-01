import DEBUG_CONSTANTS

import word_writer
from Repository.Gerrit.GerritRepository import GerritRepository
from Repository.Gtms.GtmsRepository import GtmsRepository
from User.User import User


def main():
    user =  {'username' : DEBUG_CONSTANTS.USERNAME,
             'password' : DEBUG_CONSTANTS.PASSWORD}

    # gerrit_repository = GerritRepository(DEBUG_CONSTANTS.CHANGE_ID, DEBUG_CONSTANTS.REVISION_ID, user)
    # tests = gerrit_repository.get_tests()

    # word_writer.write(tests)

    gtms_repository = GtmsRepository(user)
    tests = gtms_repository.get_tests("c629b8b4-5bb0-4b9e-a578-483d7356f15a", user)

if __name__ == "__main__":
    main()