"""
Problem No. 814

Given the root of a binary tree, return the same tree where 
every subtree (of the given tree) not containing a 1 has been removed.
A subtree of a node node is node plus every node that is a 
descendant of node.

Example 1:
    Input: root = [1,null,0,0,1]
    Output: [1,null,0,null,1]
    Explanation: 
    Only the red nodes satisfy the property "every subtree not containing a 1".
    The diagram on the right represents the answer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # if it is a leaf
        if root.left != None or root.right != None:
            return root
            
        # if subtree doesn't contain 1
        if root.val == 0:
            return None

        return root