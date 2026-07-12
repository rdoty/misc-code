# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(s):
    # write your code in Python 3.6

    # iterate over string from first character
    count_returned = 0
    last_lowest = ord(s[0])
    for i in s:
        if ord(i) >= last_lowest:
            if ord(i)+1 > last_lowest:
                last_lowest = ord(i)
                count_returned += 1
    return count_returned

# tests


print(solution("banana"))  # expects 3
print(solution("ape"))  # expects 1
