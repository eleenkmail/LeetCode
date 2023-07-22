# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


        seen = {}
        pointer = head

        while(pointer != None):

            seen[pointer] = seen.get(pointer, 0) + 1
            
            if seen[pointer] == 2:
                return True

            pointer = pointer.next

        return False
