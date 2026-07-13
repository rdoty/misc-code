# 2019.05.22 Amazon coding shared exercise with Tim
# return the node that is x places from the end of the list
# Was asked for multiple implementations...

def find_from_end_1(input_list: list, input_value):
    index = len(input_list) - 1  # initializing (zero based)
    list_copy = input_list.copy()  # so don't affect passed in value
    while list_copy:
        if list_copy[0] == input_value:
            return index
        list_copy.pop(0)
        index -= 1

    return  -1  # not found


def find_from_end_2(input_list: list, input_value):
    for index, value in enumerate(reversed(input_list)):
        if value == input_value:
            return index

    return  -1  # not found


def find_from_end_3(input_list: list, input_value):
    for index, value in enumerate(input_list[::-1]):
        if value == input_value:
            return index

    return  -1  # not found


# Test data
basic_list = [1, 2, 3, 4, 5, 6]
empty_list = []
basic_value = 2
outside_value= 99

for def_name in [find_from_end_1, find_from_end_2, find_from_end_3]:
    print(f"\nTest {def_name.__name__}")
    print(f"List: {basic_list}, seeking: {basic_value}")
    assert 4 == def_name(basic_list, basic_value), "EXPECTED 4"
    print(f"List: {basic_list}, seeking: {outside_value}")
    assert -1 == def_name(basic_list, outside_value), "EXPECTED -1"
    print(f"List: {empty_list}, seeking: {basic_value}")
    assert -1 == def_name(empty_list, basic_value), "EXPECTED -1"
    print(f"List: {empty_list}, seeking: {outside_value}")
    assert -1 == def_name(empty_list, basic_value), "EXPECTED -1"
