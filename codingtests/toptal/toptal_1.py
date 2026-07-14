""" ORIGINAL INSTRUCTIONS
    you can write to stdout for debugging purposes, e.g.
    print("this is a debug message")
    Given two strings S and T consisting of N and M characters, respectively
    determine whether string T can be obtained from string S by at most one
    the operation from the following set on string S:
    # INSERT c -- T can be obtained from S by insertng a single character 'c'
    # REPLACE c d -- T can be obtained from S by replacing single occurence of 'c'
    # with a single character 'd' 
    # SWAP c d -- T can be obtained from S by swapping two adjanced characters
    # 'c' and 'd' (distint characters in the same order in both strings)
    # EQUAL -- No operations needed
    # IMPOSSIBLE -- None of the above works
"""


def which_allowed_method_obtains_t_from_s(s:str, t:str) -> str:
    # Determine difference(s) between s and t
    # determine whether a single operation of insert, replace, swap are possible

    if s == t:  # Are strings EQUAL
        return "EQUAL"
    elif abs(len(s) - len(t)) > 1:  # Are string off by more than a INSERT/SWAP?
        return "IMPOSSIBLE"  # String lengths off by more than one are IMPOSSIBLE
    elif len(s) - len(t) == 1:  # T shorter by one character, can we INSERT?
        for index, item in enumerate(t):
            if ord(item) != ord(s[index]):
                test = (t[:index] + s[index] + t[index:])
                if s == test:
                    return "INSERT"
                else:
                    return "IMPOSSIBLE"
    elif len(t) - len(s) == 1:  # T longer by one character, can we INSERT?
        for index, item in enumerate(s):
            if ord(item) != ord(t[index]):
                test = (s[:index] + t[index] + s[index:])
                if t == test:
                    return "INSERT"
                else:
                    return "IMPOSSIBLE"
    elif len(s) == len(t):  # Same length, can we SWAP or REPLACE?
        for index, item in enumerate(s):
            if index == 0:
                continue
            if t == s[:index - 1] + s[index] + s[index - 1] + s[index + 1:]:
                return "SWAP " + s[index - 1] + " " + s[index]
        for index, item in enumerate(s):
            if item != t[index]:
                if s == t.replace(t[index], item):
                    return "REPLACE " + s[index] + " " + t[index]
                else:
                    return "IMPOSSIBLE"
    return "UNDEFINED"


def can_obtain_str_t_from_str_s(source_str: str, target_str: str) -> bool:
    """
    Take the set of characters in source, update with set of characters
    in destination. If the source set doesn't change, you can obtain
    the target from the source (but not necessarily with the allowed methods).
    """
    merged_set = set(source_str)
    merged_set.update(set(target_str))
    return merged_set == set(source_str)


def test_t_from_s_methods():
    test_data_list = [
        {'source': 'foo', 'target': 'foo', 'is_t_in_s': True, 'method_contains': 'EQUAL'},
        {'source': 'foo', 'target': 'foods', 'is_t_in_s': False, 'method_contains': 'IMPOSSIBLE'},
        {'source': 'foods', 'target': 'foo', 'is_t_in_s': True, 'method_contains': 'IMPOSSIBLE'},
        {'source': 'pfoo', 'target': 'foo', 'is_t_in_s': True, 'method_contains': 'INSERT'},
        {'source': 'swap', 'target': 'wsap', 'is_t_in_s': True, 'method_contains': 'SWAP'},
        {'source': 'swap', 'target': 'sawp', 'is_t_in_s': True, 'method_contains': 'SWAP'},
        {'source': 'swap', 'target': 'swpa', 'is_t_in_s': True, 'method_contains': 'SWAP'},
        {'source': 'test', 'target': 'tent', 'is_t_in_s': False, 'method_contains': 'REPLACE'},
        {'source': 'swap', 'target': 'bad', 'is_t_in_s': False, 'method_contains': 'IMPOSSIBLE'},
        {'source': 'nice', 'target': 'niece', 'is_t_in_s': True, 'method_contains': 'INSERT'},
        {'source': 'form', 'target': 'from', 'is_t_in_s': True, 'method_contains': 'SWAP'},
        {'source': 'o', 'target': 'odd', 'is_t_in_s': False, 'method_contains': 'IMPOSSIBLE'},
        {'source': 'niece', 'target': 'nice', 'is_t_in_s': True, 'method_contains': 'INSERT'},
    ]

    print(f"\nTesting can_obtain_str_t_from_str_s():")
    for count, test_data in enumerate(test_data_list):
        actual = can_obtain_str_t_from_str_s(test_data['source'], test_data['target'])
        assert test_data['is_t_in_s'] == actual, \
            f"Test #{count+1}: Expected: target '{test_data['target']}' to be: '{test_data['is_t_in_s']}': actual: {actual}"

    print(f"PASSED {len(test_data_list)} TESTS")

    print(f"\nTesting which_allowed_method_obtains_t_from_s():")
    for count, test_data in enumerate(test_data_list):
        actual = which_allowed_method_obtains_t_from_s(test_data['source'], test_data['target'])
        assert test_data['method_contains'] in actual, \
            f"Test #{count+1}: Expected: method '{test_data['method_contains']}' to be in: '{actual}'"

    print(f"PASSED {len(test_data_list)} TESTS")


if __name__ == "__main__":
    test_t_from_s_methods()  # run tests
