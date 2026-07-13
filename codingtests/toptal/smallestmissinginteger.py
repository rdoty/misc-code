# From https://app.codility.com/demo/results/demoMWUUJC-GWW/
# 2019.01.16 Here testing for TopTal


def solution(the_list):
    the_list.sort()  # Sort the array so we don't have to go to the end

    # Count up from one and check the array provided until we
    # don't find our value in the array
    missing_int = 1
    found = True
    while found:
        for entry in the_list:
            if entry == missing_int:
                missing_int += 1
        found = False
    return missing_int

# tests


print("\nSolution 1")
print(solution([1, 2, 4, 6, 3]))  # expects 5
print(solution([1, 3, 5, 7, 9]))  # expects 2
print(solution([-1, -2, -3, -5]))  # expects 1
print(solution([1, 2, 3, 4, 5]))  # 6, expects ? -- this determines what to change above w.r.t. while loop


# 2019.04.30 Revised answer


def solution2(the_list):
    the_list.sort()

    missing_int = 0
    for entry in the_list:
        missing_int += 1
        if entry != missing_int:
            return missing_int
    # return None  # be explicit? It does this anyway...


# tests

print("\nSolution 2")
print(solution2([1, 2, 4, 6, 3]))  # expects 5
print(solution2([1, 3, 5, 7, 9]))  # expects 2
print(solution2([-1, -2, -3, -5]))  # expects 1
print(solution2([1, 2, 3, 4, 5]))  # None, expects None
