# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 

        self.diameter = 0
        self.depth(root)
        return self.diameter

    def depth(self, root):
        
        if not root:
            return 0

        left = self.depth(root.left)
        right = self.depth(root.right)

        self.diameter = max(self.diameter, left+right)
        return max(left, right) + 1
        

       
    
    