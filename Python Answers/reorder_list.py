# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        curr = head
        while (curr.next):
            # find tail 
            fast_tail = curr.next
            slow_tail = curr
            while (fast_tail.next != None):
                slow_tail = fast_tail
                fast_tail = fast_tail.next
            # cut tail
            slow_tail.next = None
            # insert 
            fast_tail.next = curr.next
            curr.next = fast_tail
            curr = fast_tail.next

        

from my_tool.build_binary_tree_through_array import List
# import build_binary_tree_through_array
# from build_binary_tree_through_array import ListNode

if __name__ == "__main__":
    data = [2,3,4]
    head = build_binary_tree_through_array.ListNode(1)
    head = build_binary_tree_from_array(data, head)
    print_linked_list(head)
    s = Solution()
    s.reorderList(head)
    print_linked_list(head)



