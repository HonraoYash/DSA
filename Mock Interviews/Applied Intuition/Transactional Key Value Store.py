""" This question is from Applied Intuition - Software Engineer - AI Engineering role, Round 1 - Technical Interview (28th April, 2026) with Hiring Manager (Yanbo Fang) """
"""
Transactional Key-Value Store

Design a key-value store that supports transactions.

You are given a sequence of commands as a multi-line string. Process each command and return the results of all RETURN operations.

Commands:
SET key value - Set the value of key to value.
RETURN key - Return the current value of key. If the key does not exist, return an empty string "".
BEGIN - Start a new transaction. Transactions can be nested.
APPLY - Commit the current transaction. All changes are merged into the previous layer.
DISCARD - Discard the current transaction. All changes in it are lost.

Rules:
The system maintains a stack of states (global + transactions).
Inner transactions override outer values temporarily.
RETURN should always reflect the most recent visible value.

Example 1:

Input:
string = '''
SET my_key original_value
RETURN my_key
RETURN another_key
'''

Output:
["original_value", ""]

Example 2:

Input:
string = '''
SET my_key original_value
BEGIN
SET my_key second_value
RETURN my_key
DISCARD
RETURN my_key
BEGIN
SET my_key third_value
APPLY
RETURN my_key
'''

Output:
["second_value", "original_value", "third_value"]

Example 3:

Input:
string = '''
SET my_key original_value
BEGIN
SET my_key second_value
SET another_key some_other_value
BEGIN
SET my_key third_value
RETURN another_key
APPLY
RETURN my_key
DISCARD
RETURN my_key
RETURN another_key
'''

Output:
["some_other_value", "third_value", "original_value", ""]
"""
from typing import List

class Solution:
    def __init__(self):
        self.transactions = [{}]

    def keyValueStore(self, string: str) -> List[str]:
        commands = string.split("\n")
        res = []

        for command in commands:
            if command == '':
                continue
            parts = command.split(" ")
            type_of_command = parts[0]
            if type_of_command == "SET":
                key, value = parts[1], parts[2]
                self.transactions[-1][key] = value
            elif type_of_command == "BEGIN":
                copy = self.transactions[-1].copy()
                self.transactions.append(copy)
            elif type_of_command == "DISCARD":
                self.transactions.pop()
            elif type_of_command == "APPLY":
                current = self.transactions.pop()
                self.transactions.pop()
                self.transactions.append(current)
            elif type_of_command == "RETURN":
                key = parts[1]
                if key not in self.transactions[-1]:
                    res.append("")
                    continue
                res.append(self.transactions[-1][key])
            else:
                continue

        return res

string = '''
SET my_key original_value
BEGIN
SET my_key second_value
SET another_key some_other_value
BEGIN
SET my_key third_value
RETURN another_key
APPLY
RETURN my_key
DISCARD
RETURN my_key
RETURN another_key
'''
obj = Solution()
result = obj.keyValueStore(string)
print(result)