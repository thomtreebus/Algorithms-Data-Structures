class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def dfs(root, target):
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node.val == target:
            return True
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return False

def construct_tree(preorder):
    def build(lower, upper):
        if not preorder:
            return 
        node = preorder[0]
        if lower <= node <= upper:
            preorder.pop(0)
            root = Node(node)
            root.left = build(lower, node)
            root.right = build(node, upper)
            return root
        return 
    
    return build(-99, 99)

def main():
    preorder = [8, 5, 1, 7, 10, 12]
    root = construct_tree(preorder)
    print(dfs(root, 5))


main()