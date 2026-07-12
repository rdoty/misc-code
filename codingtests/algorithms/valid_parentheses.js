/**
 * Given string 's' containing just characters '(', ')', '{', '}', '[' and ']',
 * determine if input string is valid.
 * Time Complexity: O(n) - Single pass through string of length n.
 * Space Complexity: O(n) - Worst case, stack will hold all brackets.
 */
function isValid(s) {
    const stack = [];
    const bracketMap = {  // Mapping of closing / opening brackets
        ')': '(',
        '}': '{',
        ']': '['
    };

    for (let char of s) {
        if (char in bracketMap) {
            // if stack is not empty, Pop the top element, else assign dummy value
            const topElement = stack.length > 0 ? stack.pop() : '#';

            // If mapping doesn't match popped element, it's invalid
            if (bracketMap[char] !== topElement) {
                return false;
            }
        } else {  // push opening bracket onto the stack
            stack.push(char);
        }
    }
    return stack.length === 0;  // If stack is empty, all brackets matched
}

// Usage
const testStrings = ["()[]{}", "(]", "([)]", "{[]}"];
testStrings.forEach(s => {
    console.log(`Is '${s}' valid?`, isValid(s));
});
