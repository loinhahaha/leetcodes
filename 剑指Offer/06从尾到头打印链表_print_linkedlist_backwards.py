# Backwards print linked list
# Input: [1,3,2]
# Output：[2,3,1]
# Tip1: Add val from head.
# Tip2: Save and reverse.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []

        Ans = []
        while head:
            Ans.append(head.val)
            head = head.next
        Ans.reverse()
        return Ans
