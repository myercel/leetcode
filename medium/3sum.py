"""
Problem No. 15

Given an integer array nums, return all the triplets [nums[i], 
nums[j], nums[k]] such that i != j, i != k, and j != k, and 
nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.
"""

class Solution:
    # passed 312/313
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {} # num : index
        n = len(nums)
        out = set()

        for i, num in enumerate(nums):
            hashmap[num] = i

        for i in range(n):
            for j in range(i+1, n):
                desired = -nums[i] - nums[j]
                if desired in hashmap and hashmap[desired] != i and hashmap[desired] != j:
                    out.add(tuple(sorted([nums[i], nums[j], desired])))

        return out


        """
        out = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            lo, hi = i+1, n-1

            while lo < hi:
                if nums[i] != nums[lo] and nums[i] != nums[hi] and nums[lo] != nums[hi]:
                    if nums[i] + nums[lo] + nums[hi] == 0:
                        out.append([nums[i], nums[lo], nums[hi]])
                        break
                    
                    if nums[i] + nums[lo] + nums[hi] < 0:
                        lo += 1
                    else:
                        hi -= 1
        return out
        """