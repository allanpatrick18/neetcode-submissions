"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deep_copy = {None:None}

        cur = head
        while cur:
            cp = Node(cur.val)
            deep_copy[cur] = cp
            cur = cur.next

        cur = head    
        while cur:
            cp = deep_copy[cur]
            cp.next = deep_copy[cur.next]
            cp.random = deep_copy[cur.random]
            cur = cur.next
        
        return deep_copy[head]
