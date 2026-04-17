""" Mock Interview with Mahima: 17th April, 2026 """
"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence 
of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

Input: s = "applepenapple", wordDict = ["apple","pen"]
O/P: True
s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
O/P:
"""
"""
s = "leetcode"
    [1,0,0,0,1,0,0,0,1]
     p
"""
from typing import List

class Solution:
    def findSegmented(self, s: str, wordDict: List[str]):
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        res = []
        
        for i in range(len(dp)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(dp):
                   if word == s[i:i+len(word)] and dp[i+len(word)]:
                      res.append(word)
                      dp[i] = 1
        return True if dp[0] else False
    # Time Complexity - O(N*M)
    # Space Complexity - O(N)
    
s = "applepenapple"
wordDict = ["apple","pen"]
object = Solution()
print(object.findSegmented(s, wordDict))