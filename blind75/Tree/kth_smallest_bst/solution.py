# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#solution by converting tree to array and sort and return k smallest
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []
        self.dfs(root,array)
        array.sort()
        return array[k-1]
    
    def dfs(self,root,array):
        if root is None:
            return None
        else:
            self.dfs(root.left,array)
            array.append(root.val)
            self.dfs(root.right,array)
            