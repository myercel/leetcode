"""
Problem No. 16

Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sliding window problem
        # sort array

        nums.sort()
        n = len(nums)
        closest_sum = float("inf")
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            lo, hi = i + 1, n - 1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]
                if curr_sum == target:
                    return curr_sum

                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum < target: # we need to add to the sum
                    lo += 1
                else: # we need to subtract from the sum
                    hi -= 1

        return closest_sum