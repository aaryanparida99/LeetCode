# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if( head is None or head.next is None):
            return None
        lst = []
        itr = head
        while(itr.next):
            if itr in lst:
                return itr
            else:
                lst.append(itr)
            itr = itr.next
        return None