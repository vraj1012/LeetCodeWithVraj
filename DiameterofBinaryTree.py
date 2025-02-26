# 543. Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
          self.diameter = 0

          def helper(node):
            # Base condition
            if not node:
                return 0
            # Two function calls for left & right depth
            left_depth = helper(node.left)
            right_depth = helper(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

          helper(root)
          return(self.diameter)