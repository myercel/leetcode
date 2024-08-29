"""
Problem No. 204

Given an integer n, return the number of prime numbers that are 
strictly less than n.

Example 1:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less 
        than 10, they are 2, 3, 5, 7.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        # 0 and 1 are not primes
        if n == 0 or n == 1:
            return 0

        primes = [1] * n
        primes[0] = 0
        primes[1] = 0

        i = 2
        while i < n:
            product = i
            if primes[i] == 1:
                product += i
                while product < n:
                    primes[product] = 0
                    product += i
            i += 1

        return sum(primes)

        """
        count = 0

        for i in range(n):
            for j in range(1, i+1):
                if j % i == 0 and (j != i or j != 1):
                    break
                count += 1

        return count
        """