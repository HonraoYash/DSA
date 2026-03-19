""" Mock Interview; 18th March, 2026. with Andrew on Exponent """
"""
Generate Parentheses
Generate all combinations of well-formed parentheses. A parenthesis combination is well-formed if each opening parenthesis "(" is closed by a matching closing parenthesis ")" in the correct order.

For example, "()", "()()", and "((()))" are all combinations of well-formed parentheses, while ")(", "((" and "(()" are not.

Examples:
n = 1
output: ["()"]

n = 2
output: ["(())", "()()"]

n = 3
output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

n = 4
output should contain: ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]
"""

from typing import List

def generate_parentheses(n: int) -> List[str]:
    opening = closing = 0
    paranthesis = ""
    output = []

    def backtrack(opening, closing, paranthesis):
        if opening == n and closing == opening:
            output.append(paranthesis)
            return 
        if opening > n or closing > opening:
            return
        backtrack(opening + 1, closing, paranthesis + "(")
        backtrack(opening, closing + 1, paranthesis + ")")
    
    backtrack(opening, closing, paranthesis)
    return output
    # Time Complexity: O(4^n/root(n))
    # Space Complexity: O(n * (4^n/root(n))) + O(N) (auxiliary space)


# debug your code below
print(generate_parentheses(4))