from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def build_linked_list_through_list(self, head : ListNode, data: List):
        if head is None:
            return

        curr = head
        for num in data:
            curr.next = ListNode(num)
            curr = curr.next
        return head





    def print_linked_list(self, head: ListNode):
        if not head:
            print('Empty')
        while head:
            print(head.val, "->")