# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged.append(
                        self.mergeTwoLists(lists[i], lists[i+1])
                        )
                else:
                    merged.append(lists[i])

            lists = merged
        return lists[0] if lists else None
    
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next
        