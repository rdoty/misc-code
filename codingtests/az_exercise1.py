# 2019.05.22 Amazon coding shared exercise with Tim
# return the node that is x places from the end of the list


def find_x_from_end(the_list, x):
    error_value = -1

    # initializing
    values_iterated_through = the_list.add()
    list_length = 0
    while the_list.next:
        list_length += 1
        values_iterated_through.add(the_list.node)
        if values_iterated_through.length > x:
            # truncate values_iterated_through to last x values
            pass
        the_list = the_list.next

    values_iterated_through.add(the_list.node)
    if x < list_length:
        return error_value

    return values_iterated_through[0]


find_x_from_end([1, 2, 3, 4, 5, 6], 2)
