# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# Write a function that given two strings S and T
# determines whether string T can be obtained from string S
# using only one the following operations

# INSERT c
# REPLACE c
# SWAP c d
# EQUAL
# IMPOSSIBLE


def solution(s, t):
    # Determine difference(s) between s and t
    # determine whether a single operation of insert, replace, swap are needed
    # Easy first test on EQUAL
    # String lengths off by more than one are IMPOSSIBLE

    if s == t:  # Are strings EQUAL
        return "EQUAL"
    elif abs(len(s) - len(t)) > 1:  # Are string off by more than a INSERT/SWAP?
        return "IMPOSSIBLE"
    elif len(s) - len(t) == 1:  # T shorter by one character, can we INSERT?
        for index, item in enumerate(t):
            if ord(item) != ord(s[index]):
                test = (t[:index] + s[index] + t[index:])
                if s == test:
                    return "INSERT"
                else:
                    return "IMPOSSIBLE"
    elif len(t) - len(s) == 1:  # T shorter by one character, can we INSERT?
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


# Tests
print(solution("foo", "foo"))  # expects EQUAL
print(solution("foo", "foods"))  # expects IMPOSSIBLE
print(solution("foods", "foo"))  # expects IMPOSSIBLE
print(solution("pfoo", "foo"))  # expects INSERT
print(solution("test", "tent"))  # expects REPLACE
print(solution("swap", "wsap"))  # expects SWAP
print(solution("swap", "sawp"))  # expects SWAP
print(solution("swap", "swpa"))  # expects SWAP
