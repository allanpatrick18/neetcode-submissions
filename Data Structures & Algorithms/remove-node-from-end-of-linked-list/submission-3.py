# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        # counter = 0
        # curr =  head
        # prev = None
        # while curr and counter < n :
        #     prev = curr
        #     curr = curr.next
        #     counter += 1
        
        # print(prev.val, counter)
        # if curr:
        #     prev.next = curr.next
        # elif head == prev:
        #     head = None
        # else:
        #     prev.next = None
        

        # return head


