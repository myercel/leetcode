"""
Problem No. 66

You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are 
ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4].
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # reverse lst
        digits = digits[::-1]
        carry = True
        i = 0

        """
        for i in range(len(digits)):
            if digits[i] == 9:
                digits[i] == 0
                if i == len(digits) -1:
                    digits.append(1)
                else:
                    digits[i+1] += 1
            else:
                digits[i] += 1
                return digits[::-1]
        """

        while carry:
            if i < len(digits):
                # done something
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = False
            else:
                # append to lst
                digits.append(1)
                carry = False

            i += 1

        # reverse again to get the og order
        return digits[::-1]