"""
Problem No. 412

Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
    Input: n = 3
    Output: ["1","2","Fizz"]
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n+1):
            if (i%3 == 0) and (i%5 == 0):
                ans.append("FizzBuzz")
            elif (i%3 == 0):
                ans.append("Fizz")
            elif (i%5 == 0):
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans