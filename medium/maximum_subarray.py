"""
Problem No. 53

Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sliding window problem
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(maxSum, currSum)

        return maxSum