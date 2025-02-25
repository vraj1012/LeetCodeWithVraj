# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.rightview(root, result, 0)
        return result

    def rightview(self, curr: Optional[TreeNode], result: List[int], level: int):
        if not curr:
            return
        if level == len(result):
            result.append(curr.val)

        self.rightview(curr.right, result, level + 1)
        self.rightview(curr.left, result, level + 1)