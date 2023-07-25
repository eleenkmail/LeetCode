# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


        first, slow, fast = head, head, head


        while(fast.next != None):
            slow = slow.next

            fast = fast.next.next

            if fast == None: 
                break

        prev, curr = None, slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 

        while prev: 
            if first.val != prev.val:
                return False

            prev = prev.next
            first = first.next
         

            

        return True