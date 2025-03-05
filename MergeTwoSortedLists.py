# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution using recursion
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        if list1.val > list2.val:
            list1, list2 = list2, list1

        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

'''class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Taking a dummy node
        dummy = ListNode()
        curr = dummy

        # Comparing list1 and list2
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                # Moving to the next element of list1
                list1 = list1.next
            else:
                curr.next = list2
                # Moving to the next element of list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next '''