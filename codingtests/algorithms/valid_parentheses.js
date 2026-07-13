/**
 * Given string containing just characters '(', ')', '{', '}', '[' and ']',
 * determine if it is valid.
 * Time Complexity: O(n) - Single pass through string of length n.
 * Space Complexity: O(n) - Worst case, stack will hold all brackets.
 */
function isValid(inputBracketString) {
    const stackOfNestedBrackets = [];
    const matchingBracketMap = {  // Mapping of closing / opening brackets
        ')': '(',
        '}': '{',
        ']': '['
    };

    for (let char of inputBracketString) {
        if (char in matchingBracketMap) {
            // if stack is not empty, Pop the top element, else assign dummy value
            const topElement = stackOfNestedBrackets.length > 0 ? stackOfNestedBrackets.pop() : '#';

            // If mapping doesn't match popped element, it's invalid
            if (matchingBracketMap[char] !== topElement) {
                return false;
            }
        } else {  // push opening bracket onto the stack
            stackOfNestedBrackets.push(char);
        }
    }
    return stackOfNestedBrackets.length === 0;  // If stack is empty, all brackets matched
}

// Usage
const testStrings = ["()[]{}", "(]", "([)]", "{[]}", "{(([{}]))}"];
testStrings.forEach(s => {
    console.log(`Is '${s}' valid?`, isValid(s));
});
