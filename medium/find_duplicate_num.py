"""
Problem No. 287

Given an array of integers nums containing n + 1 integers 
where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array 
nums and using only constant extra space.

Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Linked list cycle problem - uses FLoyd's algo
        fast, slow = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        """
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        """
        
        """
        # Brute force approach
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[j]
        """