/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
 
 
/* 
Aurthor: Evan Kuo
Runtime: 2 ms, faster than 92.07% of Java online submissions for Add Two Numbers.
Memory Usage: 44.3 MB, less than 89.01% of Java online submissions for Add Two Numbers.
*/
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
	// Create initial head node
        ListNode L3 = new ListNode(-1);
		// Keep a reference to the start of the LL
		ListNode pointer = L3;
		// Keep track of carry, initially zero
		int carry = 0;
		
		// While there are numbers to add together
		while (l1 != null && l2 != null) {
			
			int addNums = l1.val + l2.val;
			
			if (carry == 1) {
				addNums = addNums + 1;
			}
			
			if (addNums >= 10) {
				carry = 1;
				addNums = addNums - 10;
			}
			
			else {
				carry = 0;
			}
			
			if (L3.val == -1) {
				L3.val = addNums;
			}
			
			else {
				L3.next = new ListNode(addNums);
				L3 = L3.next;
			}
			
			l1 = l1.next;
			l2 = l2.next;
		}
        
        if (l1 != null) {
			while(l1 != null) {
				int num = l1.val;
				if (carry == 1) {
					num = num + 1;
				}
				
				if (num == 10) {
					num = 0;
					carry = 1;
				}
				
				else {
					carry = 0;
				}
				L3.next = new ListNode(num);
                L3 = L3.next;
				l1 = l1.next;
			}
		}
		
		if (l2 != null) {
			while(l2 != null) {
				int num = l2.val;
				if (carry == 1) {
					num = num + 1;
				}
				
				if (num == 10) {
					num = 0;
					carry = 1;
				}
				
				else {
					carry = 0;
				}
				L3.next = new ListNode(num);
                L3 = L3.next;
				l2 = l2.next;
			}
		}
        
        if (carry == 1) {
			L3.next = new ListNode(1);
		}
        
        return pointer;
    }
}

// below is easier version of this problem
/**
Author: Shawn Jin
Runtime: 2 ms, faster than 91.81% of Java online submissions for Add Two Numbers.
Memory Usage: 44.4 MB, less than 88.47% of Java online submissions for Add Two Numbers.
*/
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode preNode = new ListNode(0);
        ListNode head = preNode;
        int carry = 0, answer = 0;
        while (l1 != null || l2 != null || carry == 1) {
            answer = (l1 == null? 0: l1.val) + (l2 == null? 0 : l2.val) + carry;
            if (answer > 9) {
                answer -= 10;
                carry = 1;
            } else {
                carry = 0;
            }
            ListNode node = new ListNode(answer);
            preNode.next = node;
            preNode = node;
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }
        return head.next;
    }

