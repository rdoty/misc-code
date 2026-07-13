class SLLNode:
    """ Definition for a singly-linked list node. """
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: SLLNode = next

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

    return prev  # will be new head of reversed list

def print_linked_list(linked_list):
    nodes = []
    current = linked_list
    while current:
        nodes.append(str(current.val))
        current = current.next
    print(" -> ".join(nodes) if nodes else "Empty List")

# Usage
if __name__ == "__main__":
    input_linked_list = SLLNode(1, SLLNode(2, SLLNode(3, SLLNode(4, SLLNode(5)))))
    print("Original List:")
    print_linked_list(input_linked_list)

    reversed_head = reverse_list(input_linked_list)
    print("Reversed List:")
    print_linked_list(reversed_head)
