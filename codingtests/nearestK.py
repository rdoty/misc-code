# Inspiration taken from
# https://www.geeksforgeeks.org/find-k-closest-elements-given-value/


# basically do a binary search to find the value closest
def find_cross_over(arr, low, high, x):
    if arr[high] <= x:  # x is greater than all
        return high

    if arr[low] > x:  # x is smaller than all
        return low

    mid = (low + high) // 2  # Find the middle point

    if arr[mid] <= x < arr[mid + 1]:  # If x same as mid, return mid
        return mid

    # If x is greater than arr[mid], then either arr[mid + 1] is ceiling of x or
    # ceiling lies in arr[mid+1...high]
    if arr[mid] < x:
        return find_cross_over(arr, mid + 1, high, x)

    return find_cross_over(arr, low, mid - 1, x)


# This function prints k closest elements to x in arr[]. n is the number of elements in arr[]
# Assumption: all elements in arr[] are distinct
def k_closest(array, target, num_to_return):
    length = len(array)
    pos = find_cross_over(array, 0, length - 1, target)  # Find the crossover point
    r = pos + 1  # Right index to search
    count = 0  # To keep track of count of elements already printed
    closest_list = []

    # If x is present in arr[], then reduce left index.
    if array[pos] == target:
        pos -= 1

    # Compare elements on left and right of crossover point to find the k closest elements
    while pos >= 0 and r < length and count < num_to_return:
        if target - array[pos][0] < array[r][0] - target:
            closest_list.append(array[pos][1])
            pos -= 1
        else:
            closest_list.append(array[r][1])
            r += 1
        count += 1

    # If there are no more elements on right side, then print left elements
    while count < num_to_return and pos >= 0:
        closest_list.append(array[pos][1])
        pos -= 1
        count += 1

    # If there are no more elements on left side, then print right elements
    while count < num_to_return and r < length:
        closest_list.append(array[r][1])
        r += 1
        count += 1

    return closest_list


def guess(array, target):
    num_items_returned = 5
    closest_list = k_closest(array, target, num_items_returned)

    return max(set(closest_list), key=closest_list.count)


# Testing stub
if __name__ == "__main__":
    starting_array = [[84.44284478, 'cat'], [88.64275596, 'cat'], [89.88920134, 'cat'],
                      [92.63887306, 'dog'], [95.86518967, 'dog'], [96.03619648, 'dog'],
                      [96.63887306, 'cat'], [97.86518967, 'cat'], [98.03619648, 'cat'],
                      [98.63887306, 'dog'], [98.86518967, 'dog'], [99.03619648, 'dog']]
    target_value = 98  # pull this from the input values sqrt(w^2+h^2)

    print("For target {:d}:".format(target_value))
    print(guess(starting_array, target_value))
