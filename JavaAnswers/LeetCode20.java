import java.util.*;

/**
Author: Shawn Jin

Runtime: 1 ms, faster than 98.81% of Java online submissions for Valid Parentheses.
Memory Usage: 34.1 MB, less than 100.00% of Java online submissions for Valid Parentheses.
*/
class LeetCode20 {
    public static boolean isValid(String s) {
        // use stack 1:() 2:{}, 3:[]
        LinkedList<Integer> stack = new LinkedList<>();
        for (int i = 0; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case '(':
                    stack.add(1);
                    break;
                case ')':
                    if (stack.isEmpty()) return false;
                    if (stack.pollLast() != 1) return false;
                    break;
                case '{':
                    stack.add(2);
                    break;
                case '}':
                    if (stack.isEmpty()) return false;
                    if (stack.pollLast() != 2) return false;
                    break;
                case '[':
                    stack.add(3);
                    break;
                case ']':
                    if (stack.isEmpty()) return false;
                    if (stack.pollLast() != 3) return false;
                    break;
            }
        }
        return stack.isEmpty();
    }

    // testing
    public static void main(String[] args) {
        String s = "([)]";
        System.out.println(isValid(s));
    }
}
