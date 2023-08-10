# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def BST(root,mx,mi):
            if not root:
                return True
            if root.val>=mx or root.val<=mi:
                return False
            
            return BST(root.left,root.val,mi) and BST(root.right,mx,root.val)
        return BST(root,float('inf'),float('-inf'))
        