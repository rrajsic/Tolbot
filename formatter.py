import re

def print_tests(tests):
    for i, test in enumerate(tests, start=1):
        print(f"Test {i}:")
        print(test)
        print()  # Add an empty line between groups for clarity
def remove_prefixes(filename, output_filename=None):
    with open(filename, 'r') as infile:
        lines = infile.readlines()

        # Remove the prefix from each line
        cleaned_lines_percent = [line.replace('%%', '', 1).strip() + '\n' for line in lines]
        cleaned_lines_exclamation = [line.replace('!', '', 1).strip() + '\n' for line in cleaned_lines_percent]

        # Determine the output filename
        if output_filename is None:
            output_filename = filename

        # Write the cleaned lines to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(cleaned_lines_exclamation)

        print(f"Prefix '%%!' removed from all lines in {output_filename}.")

def remove_non_test_data(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()

        filtered_lines = [line for line in lines if line.strip() == '' or line.strip().startswith('%%')]
        with open(filename, 'w') as outfile:
            outfile.writelines(filtered_lines)

        print(f"All non test data lines removed.")

def split_test_data(filename):
    with open(filename, 'r') as file:
        content = file.read()

    tests = re.split(r'\n.*-{10,}.*\n', content) 

    stripped_tests = []
    for test in tests:
        test_stripped = test.strip()
        if test_stripped:
            stripped_tests.append(test_stripped)

    return stripped_tests

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

def format(filename):
    print("format called")
    remove_non_test_data(filename)
    tests = split_test_data(filename)
    tests = remove_prefixes(tests)
    return tests

