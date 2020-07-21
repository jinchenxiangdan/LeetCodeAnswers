# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # if head is None
        if not head:
            return
        # check head has the val that we want to remove 
        while head and head.val == val:
            head = head.next
        # check the others 
        last = head
        curr = None
        if head and head.next:
            curr = head.next
        while(curr):
            # print("current value: ", curr.val)
            if curr.val == val:
                last.next = curr.next
            else:
                last = curr                
            curr = curr.next
        return head