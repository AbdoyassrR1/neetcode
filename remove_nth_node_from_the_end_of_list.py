# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse the linked list to delete from the end
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        
        # delete the nth element
        curr = head
        prev = None
        counter = 1
        while curr and counter <= n:
            if counter == n and prev:
                prev.next = curr.next
                break
            elif counter == n:
                curr = curr.next
                head = curr
                break
            else:
                prev = curr
                curr = curr.next
                counter += 1
        
        # reverse the linked list to the original one
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev

        return head


