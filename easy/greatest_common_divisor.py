"""
Problem No. 1071

For two strings s and t, we say "t divides s" if and only if 
s = t + t + t + ... + t + t (i.e., t is concatenated with 
itself one or more times).

Given two strings str1 and str2, return the largest string 
x such that x divides both str1 and str2.

Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def isDivisor(length):
            if len1 % length or len2 % length:
                return False
            factor1 = len1 // length
            factor2 = len2 // length
            if str1[:length] * factor1 == str1 and str1[:length] * factor2 == str2:
                return True

        for i in range(min(len1, len2), 0, -1):
            if isDivisor(i):
                return str1[:i]
        return ""
