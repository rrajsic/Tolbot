import DEBUG_CONSTANTS
import word_writer
from Repository.Gerrit.GerritRepository import GerritRepository
from User.User import User


def main():
    user =  {'username' : DEBUG_CONSTANTS.USERNAME,
             'password' : DEBUG_CONSTANTS.PASSWORD}

    gerrit_repository = GerritRepository(DEBUG_CONSTANTS.CHANGE_ID, DEBUG_CONSTANTS.REVISION_ID, user)
    tests = gerrit_repository.get_tests()

    word_writer.write(tests)

if __name__ == "__main__":
    main()