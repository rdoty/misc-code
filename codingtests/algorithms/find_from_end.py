# 2019.05.22 Amazon coding shared exercise with Tim
# return the node that is x places from the end of the list
# Was asked for multiple implementations...

def find_from_end_v1(input_list: list, input_value):
    index = len(input_list) - 1  # initializing (zero based)
    list_copy = input_list.copy()  # so don't affect passed in value
    while list_copy:
        if list_copy[0] == input_value:
            return index
        list_copy.pop(0)
        index -= 1

    return  -1  # not found


def find_from_end_v2(input_list: list, input_value):
    for index, value in enumerate(reversed(input_list)):
        if value == input_value:
            return index

    return  -1  # not found


def find_from_end_v3(input_list: list, input_value):
    for index, value in enumerate(input_list[::-1]):
        if value == input_value:
            return index

    return  -1  # not found


test_data_list = [
    {'list': [2, 3, 4, 5, 7], 'search_value': 2, 'expected_index': 4},
    {'list': [2, 3, 4, 5, 7], 'search_value': 5, 'expected_index': 1},
    {'list': [2, 3, 4, 5, 7], 'search_value': 9, 'expected_index': -1},
    {'list': [2, 3, 4, 5, 7], 'search_value': 6, 'expected_index': -1},
    {'list': [2, 3, 4, 5, 7], 'search_value': 1, 'expected_index': -1},
    {'list': [9], 'search_value': 2, 'expected_index': -1},
    {'list': [9], 'search_value': 9, 'expected_index': 0},
    {'list': [], 'search_value': 2, 'expected_index': -1},
    {'list': [], 'search_value': 99, 'expected_index': -1},
]

# run tests
for def_name in [find_from_end_v1, find_from_end_v2, find_from_end_v3]:
    print(f"\nTesting {def_name.__name__}:")
    for test_data in test_data_list:
        actual_index = def_name(test_data['list'], test_data['search_value'])
        assert test_data['expected_index'] == actual_index, \
            f"Expected index of value: '{test_data['search_value']}' to be: '{test_data['expected_index']}', in list {test_data['list']}"

    print(f"PASSED {len(test_data_list)} TESTS")
