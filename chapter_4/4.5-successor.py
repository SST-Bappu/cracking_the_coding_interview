"""
successor is the next node of a particular node in a tree.
for the sake of this problem, we have a pointer named parent pointing to the parent of the current node.
"""
from __future__ import annotations

from collections import deque


class TreeNode:
    
    def __init__(self, value: int = 0, parent: TreeNode = None):
        """
        :param value: value of the TreeNode
        :param parent: parent of the TreeNode if any
        """
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
    
    def insert(self, value: int) -> bool:
        queue = deque()
        queue.append(self)
        while queue:
            cur = queue.popleft()
            
            # insert to the left if left is empty or enqueue left
            if not cur.left:
                cur.left = TreeNode(value, cur)
                return True
            else:
                queue.append(cur.left)
            
            # insert to the right if right is empty or enqueue right
            if not cur.right:
                cur.right = TreeNode(value, cur)
                return True
            else:
                queue.append(cur.right)
    
    @classmethod
    def left_most_node(cls, node: TreeNode) -> TreeNode | None:
        """
        This will retrieve the left most node of a particular node and return that
        """
        if not node:
            return None
        
        while node.left:
            node = node.left
        
        return node
    
    @classmethod
    def successor(cls, node: TreeNode) -> TreeNode | None:
        if not node:
            return None
        if node.right:
            # it means the next node is either the right node or the left most node of the right node
            return cls.left_most_node(node.right)
        
        prev_node = node
        while node and node.left != prev_node:
            prev_node = node
            node = node.parent
        
        return node


if __name__ == "__main__":
    # let's build the tree first
    root = TreeNode(10)
    root.insert(5)
    root.insert(8)
    root.insert(15)
    root.insert(20)
    root.insert(25)
    
    next_node = TreeNode.successor(root.left.left)
    
    
