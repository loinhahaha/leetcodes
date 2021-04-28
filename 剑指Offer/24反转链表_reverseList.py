# Reverse output link.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        nxt = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre
# TC: O(N)
# SC: O(1)



# Recursion
def reverseList(head):
    def recur(pre, cur):
        if not cur: return pre
        res=recur(cur, cur.next)
        cur.next=pre
        return res
    return recur(None, head)
  
