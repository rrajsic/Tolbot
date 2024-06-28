import re

def remove_non_test_data(unfiltered_data):
    filtered_data = []
    filtered_data = [line for line in unfiltered_data if line.strip() == '' or line.strip().startswith('%%')]
    print(filtered_data)
    return filtered_data

def split_test_data(filtered_data):
  
    filtered_data_string = "\n".join(filtered_data)
    tests = re.split(r'\n.*-{10,}.*\n', filtered_data_string) 

    split_test_data = []
    for test in tests:
        test_stripped = test.strip()
        if test_stripped:
            split_test_data.append(test_stripped)

    return split_test_data

def remove_prefixes(tests):
    for i in range(len(tests)):
        tests[i] = '\n'.join(line.lstrip('%%') for line in tests[i].splitlines())
        tests[i] = '\n'.join(line.lstrip('!') for line in tests[i].splitlines())
        tests[i] = '\n'.join(line.lstrip('-------') for line in tests[i].splitlines())
        lines = tests[i].splitlines()
        
        if lines and not lines[0].strip():
            lines = lines[1:]
        
        tests[i] = '\n'.join(lines)
    return tests

def format(unfiltered_data):
    filtered_data = remove_non_test_data(unfiltered_data)
    tests = split_test_data(filtered_data)
    tests = remove_prefixes(tests)
    return tests

