/** Definition for a singly-linked list node. */
class SLLNode {
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
function reverseList(singlyLinkedList) {
    let prev = null;
    let current = singlyLinkedList;

    while (current !== null) {
        let nextNode = current.next; // Temporarily store the next node
        current.next = prev;         // Reverse the current node's pointer
        prev = current;              // Move prev one step forward
        current = nextNode;          // Move current one step forward
    }
    return prev; // prev new head of reversed list
}

function printList(singlyLinkedList) {
    const nodeList = [];
    let current = singlyLinkedList;
    while (current !== null) {
        nodeList.push(current.val);
        current = current.next;
    }
    console.log(nodeList.length > 0 ? nodeList.join(" -> ") : "Empty List");
}

// Usage
const inputSLList = new SLLNode(1, new SLLNode(2, new SLLNode(3, new SLLNode(4, new SLLNode(5)))));
console.log("Original List:");
printList(inputSLList);

const reversedSLL = reverseList(inputSLList);
console.log("Reversed List:");
printList(reversedSLL);
