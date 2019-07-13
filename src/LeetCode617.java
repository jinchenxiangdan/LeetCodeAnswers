/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class LeetCode {
    /**
    Runtime: 1 ms, faster than 45.77% of Java online submissions for Merge Two Binary Trees.
    Memory Usage: 44.6 MB, less than 20.41% of Java online submissions for Merge Two Binary Trees.
    */
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        // if 
        if (t1 == null && t2 == null) {
            return null;
        }
        // merge all to t1
        if (t1 == null) {
            t1 = new TreeNode(0);
        }
        if (t2 == null) {
            t2 = new TreeNode(0);
        }
        
        // left
        if (t1.left != null || t2.left != null) {
            t1.left = mergeTrees(t1.left, t2.left);    
        }
        
        // right
        if (t1.right != null || t2.right != null) {
            t1.right = mergeTrees(t1.right, t2.right);
        }
        
        // this 
        t1.val = t1.val + t2.val;
        return t1;
    }
}
