# Output kth to the end val in a linked list.
# Tip: use 2 pointers, fast pointer first go k steps and then two pointers go together.

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter
# TC: O(N)
# SC: O(1)
