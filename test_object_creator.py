import re

def create_test_objects(tests):
    test_objects = []
    for test in tests:
        test_object = {}
        current_key = None
        current_value = []

        test_object["NAME"] = test.splitlines()[0].strip()
        test_objects.append(test_object)

        lines = test.splitlines()
        for line in lines:
            line = line.rstrip()
            if line:
                match = re.match(r'^\s*(PREREQUISITES|UPDATE PRECONDITIONS|PURPOSE|TRIGGER|VERIFICATION|TRIGGER \d+|VERIFICATION \d+):', line)
                if match:
                    print(line)
                    if current_key:
                        test_object[current_key] = '\n'.join(current_value).strip()
                    current_key = match.group(1)
                    current_value = [line[match.end():].lstrip()]
                else:
                    if current_key:
                        current_value.append(line)
        if current_key:
            test_object[current_key] = '\n'.join(current_value).strip()
    return test_objects


