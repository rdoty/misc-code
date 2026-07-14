class SLLNode:
    """ Definition for a singly-linked list node. """
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: SLLNode = next


def print_linked_list(linked_list):
    nodes = []
    current = linked_list
    while current:
        nodes.append(str(current.val))
        current = current.next
    output = (" -> ".join(nodes) if nodes else "Empty List")
    print (output)
    return output


def reverse_list(input_linked_list):
    """
    Reverse a singly linked list iteratively.

    Time Complexity: O(n) - Iterate through list of length n once.
    Space Complexity: O(1) - Constant space utilized for pointers.
    """
    prev = None
    current = input_linked_list

    while current:
        next_node = current.next  # Temp storage of next node
        current.next = prev       # Reverse current node's pointer
        prev = current            # Move prev one forward
        current = next_node       # Move current one forward

    return prev  # new head of reversed list


def test_reverse_list():
    test_data_list = [
        {
            'input': SLLNode(1, SLLNode(2, SLLNode(3, SLLNode(4)))),
            'expected': '4 -> 3 -> 2 -> 1'
        },
        {'input': SLLNode(1), 'expected': '1'},
        {'input': SLLNode(), 'expected': '0'},
        {'input': [], 'expected': 'Empty List'},
    ]
    for count, test_data in enumerate(test_data_list):
        reversed_list = reverse_list(test_data['input'])
        actual = print_linked_list(reversed_list)
        assert actual == test_data['expected'], \
            f"Test #{count+1}: Expected {test_data['expected']}, actual: {actual}"
    
    print(f"PASSED {len(test_data_list)} TESTS")


if __name__ == "__main__":
    test_reverse_list()  # run tests
