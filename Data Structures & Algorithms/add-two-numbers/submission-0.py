# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_node = ListNode()
        ret_ = 0
        target = l_node
        while True :
            val = l1.val + l2.val + ret_
            # Add the retenue 
            if val > 9:
                ret_ = 1 
                val -= 10
            else : 
                ret_ = 0 
            target.val = val

            # Next value 
            l1 = l1.next
            l2 = l2.next
            if (l1 is None) & (l2 is None) & (ret_ ==0) :
                return l_node
            if (l2 is None) :
                l2 = ListNode()
            if (l1 is None)  : 
                l1 = ListNode()
            target.next = ListNode()
            target = target.next

