import DEBUG_CONSTANTS

import formatter
import gerrit_functions
import word_writer
import test_object_creator


def main():
    print("Enter username:")
    print("Authenticated User:", DEBUG_CONSTANTS.USERNAME)
    # password = getpass.getpass(prompt="Enter Windows password: ")
    # print("Passoword is: ", password)
    # changeId = input("Enter Change-Id:")
   
    unfiltered_data = gerrit_functions.get_unfiltered_diff_data()
    tests = formatter.format(unfiltered_data)
    tests = test_object_creator.create_test_objects(tests)
    word_writer.write(tests)

if __name__ == "__main__":
    main()