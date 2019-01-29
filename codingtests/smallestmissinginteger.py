# From https://app.codility.com/demo/results/demoMWUUJC-GWW/
# 2019.01.16 Here testing for TopTal


def solution(a):
    # Count up from one and check the array provided until we
    # don't find our value in the array

    # Sort the array so we don't have to go to the end
    a.sort()
    ret_val = 1
    found = True
    while found:
        for i in a:
            if i == ret_val:
                ret_val += 1
        found = False
    return ret_val

# tests


print(solution([1, 2, 4, 6, 3]))  # expects 5
print(solution([1, 3, 5, 7, 9]))  # expects 2
print(solution([-1, -2, -3, -5]))  # expects 1
