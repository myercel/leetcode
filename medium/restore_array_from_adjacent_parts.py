"""
Problem No. 1743

There is an integer array nums that consists of n unique elements, 
but you have forgotten it. However, you do remember every pair of adjacent elements in nums.
You are given a 2D integer array adjacentPairs of size n - 1 where each 
adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
It is guaranteed that every adjacent pair of elements nums[i] and 
nums[i+1] will exist in adjacentPairs, either as 
[nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.
Return the original array nums. If there are multiple solutions, return any of them.

Example 1:
    Input: adjacentPairs = [[2,1],[3,4],[3,2]]
    Output: [1,2,3,4]
    Explanation: This array has all its adjacent pairs in adjacentPairs.
    Notice that adjacentPairs[i] may not be in left-to-right order.
"""

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        curr = None
        for u in graph:
            if len(graph[u]) == 1: # found start or end point
                curr = u
                break
        
        ans = []
        seen = set()

        while curr != None:
            ans.append(curr)
            seen.add(curr)
            neighbors = graph[curr]
            curr = None

            for nei in neighbors:
                if nei not in seen:
                    curr = nei

        return ans