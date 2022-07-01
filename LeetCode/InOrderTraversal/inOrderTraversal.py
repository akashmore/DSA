# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tmpArray = []
        self.callHelper(tmpArray,root)
        return tmpArray
    
    def callHelper(self,tmpArray,root):
        if root:
            self.callHelper(tmpArray,root.left)
            tmpArray.append(root.val)
            self.callHelper(tmpArray,root.right)