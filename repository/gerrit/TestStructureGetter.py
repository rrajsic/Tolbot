import re

class TestStructureGetter:

    def get_structurized_tests_from_data(self, filtered_test_data):
        structurized_tests = []
        filtered_tests = TestStructureGetter.split_test_data(filtered_test_data)
        for test in filtered_tests:
                test_object = {}
                current_key = None
                current_value = []

                test_object["NAME"] = test.splitlines()[0].strip()
                structurized_tests.append(test_object)

                lines = test.splitlines()
                for line in lines:
                    line = line.rstrip()
                    if line:
                        match = re.match(r'^\s*(PREREQUISITES|UPDATE PRECONDITIONS|PURPOSE|TRIGGER|VERIFICATION|TRIGGER \d+|VERIFICATION \d+[a-z]*):', line)
                        if match:
                            if current_key:
                                test_object[current_key] = '\n'.join(current_value).strip()
                            current_key = match.group(1)
                            current_value = [line[match.end():].lstrip()]
                        else:
                            if current_key:
                                current_value.append(line)
                if current_key:
                    test_object[current_key] = '\n'.join(current_value).strip()

        return structurized_tests

    def split_test_data(filtered_data):
        filtered_data_string = "\n".join(filtered_data)
        tests = re.split(r'\n.*-{20,}.*\n', filtered_data_string)
        stripped_tests = []

        for test in tests:
            lines = test.split('\n')
            if lines[0].startswith('-' * 20):
                modified_test = '\n'.join(lines[1:])
                stripped_tests.append(modified_test)
            else:
                stripped_tests.append(test)

        split_test_data = []
        for test in stripped_tests:
            test_stripped = test.strip()
            if test_stripped:
                split_test_data.append(test_stripped)

        return split_test_data