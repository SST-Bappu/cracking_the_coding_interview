"""
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
    1
2       3
    4       5

here in the example above, first common ancestor of 4 and 5 is 3
"""
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val: int):
        queue = deque()
        queue.append(self)
        while queue:
            cur = queue.popleft()
            
            if not cur.left:
                cur.left = TreeNode(val)
                return
            if not cur.right:
                cur.right = TreeNode(val)
                return
            
            queue.extend([cur.left, cur.right])


def find_first_common_ancestor(root: TreeNode, node1: TreeNode, node2: TreeNode) -> TreeNode | None:
    """
       if root is None, there's no possible common ancestor.
       if root is equal to node1 or node2, then root is actually the first common ancestor
    """
    if not root or root==node1 or root==node2:
        return root
    ancestor = None
    
    def dfs(node):
        nonlocal ancestor
        if not node:
            return False
        
        cur_node = False
        if node == node1 or node == node2:
            cur_node = True
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        # if we find both node1 and node2 in the path starting from current node, that's the first ancestor
        if left + right +cur_node>=2:
            ancestor = node
        
        return left or right or cur_node
    
    dfs(root)
    return ancestor


tree_root = TreeNode(10)

tree_root.insert(5)
tree_root.insert(6)
tree_root.insert(7)
tree_root.insert(8)

print(tree_root.left.left.val, tree_root.left.right.val)
ancestor = find_first_common_ancestor(tree_root, tree_root.left.left, tree_root.left.right)

print(ancestor.val)
