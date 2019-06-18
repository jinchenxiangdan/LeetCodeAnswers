/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class LeetCode1008 {
    public TreeNode bstFromPreorder(int[] preorder) {
        		
		TreeNode root = new TreeNode(preorder[0]);
		
		
		int i = 1;
		while (i < preorder.length) {
			
			boolean foundSpot = false;
			TreeNode currRoot = root;
			
			while (foundSpot == false) {
				if (currRoot.val < preorder[i]) {
					
					if (currRoot.right == null) {
						currRoot.right = new TreeNode(preorder[i]);
						foundSpot = true;
					}
					else {
						currRoot = currRoot.right;
					}
				}
				
				else {
					if (currRoot.left == null) {
						currRoot.left = new TreeNode(preorder[i]);
						foundSpot = true;
					}
					else {
						currRoot = currRoot.left;
					}
				}
			}
			i = i + 1;
		}
        return root;
    }
}
