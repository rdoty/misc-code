# From https://app.codility.com/demo/results/demoMWUUJC-GWW/
# 2019.01.16 Here testing for TopTal

def smallest_missing_int_v1(the_list):
    the_list.sort()  # Sort the array so we don't have to go to the end

    # Count up from one and check the array provided until we
    # don't find our value in the array
    missing_int = 1
    gap_found = True
    while gap_found:
        for entry in the_list:
            if entry == missing_int:
                missing_int += 1
        gap_found = False
    return missing_int

def smallest_missing_int_v2(the_list):  # 2019.04.30 Revised answer
    the_list.sort()

    missing_int = 0
    for entry in the_list:
        missing_int += 1
        if entry != missing_int:
            return missing_int
    
    return the_list[-1] + 1


def test_smallest_missing_ints():
    test_functions = [smallest_missing_int_v1, smallest_missing_int_v2]
    test_data_list =[
        {'input': [1, 2, 4, 6, 3], 'expected': 5},
        {'input': [1, 3, 5, 7, 9], 'expected': 2},
        {'input': [-1, -2, -3, -5], 'expected': 1},
        {'input': [1, 2, 3, 4, 5], 'expected': 6},
    ]

    for def_name in test_functions:
        print(f"\nTesting {def_name.__name__}():")
        for count, test_data in enumerate(test_data_list):
            actual = def_name(test_data['input'])
            assert actual == test_data['expected'], \
                f"Test #{count+1}: Expected index of value: '{test_data['input']}' to be: '{test_data['expected']}': actual: {actual}"

        print(f"PASSED {len(test_data_list)} TESTS")


if __name__ == "__main__":
    test_smallest_missing_ints()

