"""
Problem No. 290

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between 
a letter in pattern and a non-empty word in s.

Example 1:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        words_dict = {}
        pattern_dict = {}

        # edge case: unequal lengths
        if len(pattern) != len(words):
            return False

        for w, p in zip(words, pattern):
            if w in words_dict and words_dict[w] != p:
                return False
            if p in pattern_dict and pattern_dict[p] != w:
                return False

            words_dict[w] = p
            pattern_dict[p] = w

        return True