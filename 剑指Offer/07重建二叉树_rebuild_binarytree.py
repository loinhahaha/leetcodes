# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Rebuild a binary tree from its preorder form and inorder form.
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Tip: preorder[0] is root and base on that build binary tree recursively.
# Steps: root = 3 -> inorder [9,3] so 3.left = 9 -> preorder [20,..] so 3.right = 20 -> 20.left = 15 -> 20.right = 7 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == []:
            return None    
          
        loc = inorder.index(preorder[0])  # find root index in inorder
        root = TreeNode(preorder[0])
        
        root.left = self.buildTree(preorder[1:loc+1] , inorder[:loc])
        root.right = self.buildTree(preorder[loc+1:] , inorder[loc+1:])
        return root

    
