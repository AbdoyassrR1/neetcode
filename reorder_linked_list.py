#!/usr/bin/python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_nodes = []
        
        curr = head
        while curr:
            list_nodes.append(curr)
            curr = curr.next
        
        l, r = 0, len(list_nodes) - 1
        while l < r:
            list_nodes[l].next = list_nodes[r]
            l += 1
            list_nodes[r].next = list_nodes[l]
            r -= 1
        
        list_nodes[l].next = None
