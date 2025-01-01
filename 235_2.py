# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root

        while current is not None:
            
            # p and q on the left subtree
            if p.val < current.val and q.val < current.val:
                current = current.left
            
            # p and q on the right subtree
            elif p.val > current.val and q.val > current.val:
                current = current.right

            # p and q are on different sides, this is the LCA
            else:
                return current