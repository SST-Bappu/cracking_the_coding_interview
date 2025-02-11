from __future__ import annotations


class Node:
    def __init__(self, value: int = 0):
        self.value = value
        self.left = None
        self.right = None
    
    @classmethod
    def traverse(cls, root: Node) -> [int]:
        if not root:
            return []
        result = []
        result += cls.traverse(root.left)
        result.append(root.value)
        result += cls.traverse(root.right)
        
        return result


class Tree:
    @classmethod
    def minimal_tree(cls, nums: [int]) -> Node | None:
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        root = Node(nums[mid])
        root.left = cls.minimal_tree(nums[:mid])
        root.right = cls.minimal_tree(nums[mid + 1:])
        
        return root
    @classmethod
    def build_tree(cls, nums: [int])->Node|None:
        
        root = cls.minimal_tree(nums)
        # print(Node.traverse(root))
        return root


