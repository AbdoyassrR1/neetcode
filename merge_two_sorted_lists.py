# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        initial_list = ListNode()
        init_ptr = initial_list

        while list1 and list2:
            if list1.val < list2.val:
                init_ptr.next = list1
                list1 = list1.next
            else:
                init_ptr.next = list2
                list2 = list2.next

            init_ptr = init_ptr.next

        init_ptr.next = list1 or list2
    

        return initial_list.next