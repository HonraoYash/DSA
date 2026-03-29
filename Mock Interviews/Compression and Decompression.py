""" Mock Interview - 28th March, 2026 with Ellika """
"""
1. Compression and decompression

In this exercise, you're going to decompress a compressed string.

Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

The input

3[abc]4[ab]c

Would be output as

abcabcabcababababc

Other rules

Numbers can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

Characters allowed as input include digits, small English letters and brackets [ ].

Digits are only to represent the amount of repetitions.

Letters are just letters.

Brackets are only part of the syntax of writing repeated substring.

Input is always valid, so no need to check its validity.

Learning objectives: This question gives you the chance to practice with strings, recursion, algorithm, compilers, automata, and loops. It’s also an opportunity to work on coding with better efficiency.
"""

class Solution: 
    def decompressString(self, s:str) -> str:
        strStack = []
        cntStack = []
        current = ""
        multiplier = 0

        for char in s:
            if char.isdigit():
                multiplier = multiplier * 10 + int(char)
            elif char == '[':
                strStack.append(current)
                cntStack.append(multiplier)
                multiplier = 0
                current = ""
            elif char == ']':
                prevString = strStack.pop()
                for _ in range(cntStack.pop()): prevString += current
                current = prevString
            else:
                current += char

        return current

obj = Solution()
string = "2[3[a]b]"
print(obj.decompressString(string))