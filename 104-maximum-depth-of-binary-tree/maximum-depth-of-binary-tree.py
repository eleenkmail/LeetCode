# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def Depth(root, count):
            if not root:
                return count
            count+=1
            
            return max(Depth(root.left, count), Depth(root.right, count))
            
            
            

        count = 0
        return Depth(root, count)
        
