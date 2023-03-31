# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if self.traverseTree(p) == self.traverseTree(q):
            return True
        else:
            return False

    def traverseTree(self, root):
        if not root:
            return ['null']
        else:
            return [root.val] + self.traverseTree(root.left) + self.traverseTree(root.right)