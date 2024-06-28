import re

class Filter():

    def filter_data(self, unfiltered_data):
        test_data = Filter.remove_non_test_data(unfiltered_data)
        filtered_test_data = Filter.remove_prefixes(test_data)

        return filtered_test_data

    def remove_non_test_data(unfiltered_data):
        filtered_data = []
        filtered_data = [line for line in unfiltered_data if line.strip() == '' or line.strip().startswith('%%')]

        return filtered_data

    def remove_prefixes(tests):
        for i in range(len(tests)):
            tests[i] = '\n'.join(line.lstrip('%%') for line in tests[i].splitlines())
            tests[i] = '\n'.join(line.lstrip('!') for line in tests[i].splitlines())
            lines = tests[i].splitlines()
            
            if lines and not lines[0].strip():
                lines = lines[1:]
            tests[i] = '\n'.join(lines)

        return tests
