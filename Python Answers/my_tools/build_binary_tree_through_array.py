from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def search(self, val):
        # base case : 
        if self is None:
            return False
        if self.val == val:
            return True
        
        if self.left:
            if self.right:
                return self.left.search(val) or self.right.search(val)
            return self.left.search(val)
        if self.right:
            return self.right.search(val)
        return False
'''
data: a list with binary tree information
node: the head of binary tree
index: the initial should be 0
'''
def build_binary_tree_from_array(data: List, node:TreeNode, index: int) -> TreeNode:
    # base case : index out of range 
    if index >= len(data) or index < 0:
        return
    # left child 
    if index * 2 + 1 < len(data):
        node.left = TreeNode(data[index * 2 + 1])
        build_binary_tree_from_array(data, node.left, index * 2 + 1)
    # right child 
    if index * 2 + 2 < len(data):
        node.right = TreeNode(data[index * 2 + 2])
        build_binary_tree_from_array(data, node.right, index * 2 + 2)


def bfs(head):
    # bfs 
    curr = head
    queue = [curr]
    while queue:
        curr = queue.pop(0)
        print(curr.val, "-")
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

# test area
if __name__ == "__main__":
    binary_tree = [3,9,20,None,None,15,7]
    
    head = TreeNode(binary_tree[0])
    build_binary_tree_from_array(binary_tree, head, 0)
    bfs(head)

    # test 2
    bst = [2,1,3]        
    head2 = TreeNode(bst[0])
    build_binary_tree_from_array(bst, head2, 0)
    print(head2.search(3))
    # bfs(head2)
