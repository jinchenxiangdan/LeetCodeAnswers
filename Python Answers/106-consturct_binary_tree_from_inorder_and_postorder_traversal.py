from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.helper(inorder, postorder, 0, len(inorder)-1, [len(inorder)-1])

    def helper(self, inorder, postorder, start, end, index):
        # Base case  
        if start > end:
            return None
        node = TreeNode(postorder[index[0]])
        index[0] -= 1
        if start == end:
            return None
        i_index = self.search(inorder, start, end, node.val)

        node.right = self.helper(inorder, postorder, i_index+1, end, index)
        node.left  = self.helper(inorder, postorder, start, i_index-1, index)

        return node
    # Function to find index of value in  
    # arr[start...end]. The function assumes  
    # that value is postsent in in[]  
    def search(self, arr, strt, end, value): 
        i = 0
        for i in range(strt, end + 1): 
            if (arr[i] == value):  
                break
        return i 

    # This funtcion is here just to test  
    def preOrder(self, node): 
        if node == None:  
            return
        print(node.val,end=" ") 
        self.preOrder(node.left)  
        self.preOrder(node.right)

# Driver code  
if __name__ == '__main__': 
    In = [4, 8, 2, 5, 1, 6, 3, 7] 
    post = [8, 4, 5, 2, 6, 7, 3, 1]  
    n = len(In) 
    solution = Solution()

    root = solution.buildTree(In, post)  

    print("Preorder of the constructed tree :")  
    solution.preOrder(root) 
    
    # This code is contributed by PranchalK 