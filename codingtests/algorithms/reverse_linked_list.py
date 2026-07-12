class ListNode:
    """ Definition for a singly-linked list node. """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    """
    Reverse a singly linked list iteratively.

    Time Complexity: O(n) - Iterate through list of length n once.
    Space Complexity: O(1) - Constant space utilized for pointers.
    """
    prev = None
    current = head

    while current:
        next_node = current.next  # Temp storage of next node
        current.next = prev       # Reverse current node's pointer
        prev = current            # Move prev one forward
        current = next_node       # Move current one forward

    return prev  # will be new head of reversed list

def print_list(head):
    nodes = []
    current = head
    while current:
        nodes.append(str(current.val))
        current = current.next
    print(" -> ".join(nodes) if nodes else "Empty List")

# Usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original List:")
    print_list(head)

    reversed_head = reverse_list(head)
    print("Reversed List:")
    print_list(reversed_head)
