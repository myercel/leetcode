"""
Problem No. 1878

You are given an m x n integer matrix grid​​​.
A rhombus sum is the sum of the elements that form the border of a 
regular rhombus shape in grid​​​. The rhombus must have the shape of a 
square rotated 45 degrees with each of the corners centered in a grid cell. 
Below is an image of four valid rhombus shapes with the corresponding colored 
cells that should be included in each rhombus sum.
Note that the rhombus can have an area of 0, which is depicted by the purple 
rhombus in the bottom right corner.
Return the biggest three distinct rhombus sums in the grid in descending order. 
If there are less than three distinct values, return all of them.

Example 1:
    Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
    Output: [228,216,211]
    Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
    - Blue: 20 + 3 + 200 + 5 = 228
    - Red: 200 + 2 + 10 + 4 = 216
    - Green: 5 + 200 + 4 + 2 = 211
"""

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        pq = []

        def calc(l, r, u, d):
            ssum = 0
            c1 = c2 = (l+r) // 2
            expand = True
            for row in range(u, d+1):
                if c1 == c2:
                    ssum += grid[row][c1]
                else:
                    ssum += grid[row][c1] + grid[row][c2]

                if c1 == l:
                    expand = False

                if expand:
                    c1 -= 1
                    c2 += 1
                else:
                    c1 += 1
                    c2 -= 1

            return ssum

        for i in range(m):
            for j in range(n):
                l = r = j
                d = i
                while l >= 0 and r <= n-1 and d <= m-1:
                    ssum = calc(l, r, i, d)
                    l -= 1
                    r += 1
                    d += 2

                    if len(pq) < 3:
                        if ssum not in pq:
                            heapq.heappush(pq, ssum)
                        
                    else:
                        if ssum not in pq and ssum > pq[0]:
                            heapq.heappop(pq)
                            heapq.heappush(pq, ssum)

        pq.sort(reverse=True)
        return pq