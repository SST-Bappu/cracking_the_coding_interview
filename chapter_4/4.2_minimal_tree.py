from __future__ import annotations



class Node:
    def __init__(self, value: int = 0):
        self.value = value
        self.left = None
        self.right = None
    
    @classmethod
    def traverse(cls, root: Node)-> [int]:
        if not root:
            return []
        result = []
        result += cls.traverse(root.left)
        result.append(root.value)
        result+= cls.traverse(root.right)
        
        return result
        




class Tree:
    def minimal_tree(self, nums: [int]) -> Node:
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        root = Node(nums[mid])
        root.left = self.minimal_tree(nums[:mid])
        root.right = self.minimal_tree(nums[mid + 1:])
        
        return root
    def build_tree(self):
        nums = [1,5,8,10,15,25,35,40,55,67,87]
    
        root = self.minimal_tree(nums)
        # print(Node.traverse(root))
        return root


