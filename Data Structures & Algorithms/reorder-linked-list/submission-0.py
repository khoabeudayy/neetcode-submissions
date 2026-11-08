# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow

        second = middle.next
        middle.next = None

        prev = None
        current = second

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first = head
        second = prev

        while second is not None:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2


        