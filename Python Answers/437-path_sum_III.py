# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        return self.dfs( root, [s] )

    def dfs(self, root, targets):
        if not root: return 0
        newtargets = [ targets[0] ] + [ target - root.val for target in targets ]
        return targets.count(root.val) + self.dfs(root.left, newtargets) + self.dfs(root.right, newtargets)

        