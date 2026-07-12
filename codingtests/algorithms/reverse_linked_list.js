/** Definition for a singly-linked list node. */
class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

/**
 * Reverses singly linked list (iteratively).
 * Time Complexity: O(n) - through list of length n exactly once.
 * Space Complexity: O(1) - Constant space for pointers.
 */
function reverseList(head) {
    let prev = null;
    let current = head;

    while (current !== null) {
        let nextNode = current.next; // Temporarily store the next node
        current.next = prev;         // Reverse the current node's pointer
        prev = current;              // Move prev one step forward
        current = nextNode;          // Move current one step forward
    }
    return prev; // prev new head of reversed list
}

function printList(head) {
    const nodes = [];
    let current = head;
    while (current !== null) {
        nodes.push(current.val);
        current = current.next;
    }
    console.log(nodes.length > 0 ? nodes.join(" -> ") : "Empty List");
}

// Usage
const head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
console.log("Original List:");
printList(head);

const reversedHead = reverseList(head);
console.log("Reversed List:");
printList(reversedHead);
