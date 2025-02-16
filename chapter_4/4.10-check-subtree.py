from collections import deque

from sqlalchemy.dialects.mysql import insert


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


def check_sub_tree(t1: TreeNode, t2: TreeNode) -> bool:
    def dfs(node1: TreeNode, node2: TreeNode, level):
        if not node2:
            return True
        if not node1 or (level > 0 and node1.val != node2.val):
            return False
        
        if node1.val == node2.val:
            return (dfs(node1.left, node2.left, level + 1) and dfs(node1.right, node2.right, level + 1)) or dfs(
                node1.left, node2, level) or dfs(node1.right, node2, level)
        
        else:
            return dfs(node1.left, node2, level) or dfs(node1.right, node2, level)

    
    return dfs(t1, t2, 0)

"""
if we traverse the tree and take all the values, we can easily check the strings if T2 is a subtree of T1.
"""
def tree_to_string(t: TreeNode):
    s = []
    def dfs(node: TreeNode):
        
        if not node:
            return
        dfs(node.left)
        s.append(node.val)
        dfs(node.right)
    
    dfs(t)
    return ''.join(map(str,s))
    
def check_sub_tree_string(t1: TreeNode, t2: TreeNode)->bool:
    t1_string = tree_to_string(t1)
    t2_string = tree_to_string(t2)
    
    if t2_string in t1_string:
        return True
    
    return False
    
T1 = TreeNode(5)
T1.insert(4)
T1.insert(10)
T1.insert(4)
T1.insert(26)
T1.insert(12)
T1.insert(15)
T1.insert(25)
T1.insert(26)

T2 = TreeNode(4)
T2.insert(25)
T2.insert(26)

print(check_sub_tree(T1, T2))

print(check_sub_tree_string(T1, T2))