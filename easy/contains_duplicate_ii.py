"""
Problem No. 219

Given an integer array nums and an integer k, return true if there are 
two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        window = set()

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])