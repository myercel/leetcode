"""
Problem No. 1390

Given an integer array nums, return the sum of divisors of the 
integers in that array that have exactly four divisors. If there 
is no such integer in the array, return 0.

Example 1:
    Input: nums = [21,4,7]
    Output: 32
    Explanation: 
    21 has 4 divisors: 1, 3, 7, 21
    4 has 3 divisors: 1, 2, 4
    7 has 2 divisors: 1, 7
    The answer is the sum of divisors of 21 only.
"""

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum_divs = 0
        for num in nums:
            total = set()
        
            for i in range(1, floor(sqrt(num)) + 1):
                if num % i == 0:
                    total.add(num//i)
                    total.add(i)
                if len(total) > 4:
                    break

            if len(total) == 4:
                sum_divs += sum(total)

        return sum_divs

        """
        13/18 test cases passed - time limit exceeded
        
        total = 0

        for num in nums:
            count = 0
            divisors = 0
            for i in range(1, num+1):
                if num % i == 0:
                    count += 1
                    divisors += i
            if count == 4:
                total += divisors

        return total
        """