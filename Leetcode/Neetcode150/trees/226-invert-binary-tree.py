# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        stack = [root]
        
        while stack:
            node = stack.pop()
            temp = node.left
            node.left = node.right
            node.right = temp
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root