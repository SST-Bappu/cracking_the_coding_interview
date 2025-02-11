from collections import deque

from interview.utils.bst_tree import Tree, Node


class LinkedList:
    def __init__(self, val: int = 0):
        self.value = val
        self.next = None


def list_of_depths(tree_root: Node)->LinkedList:
    """
    It's a BFS implementation.
    we will go level by level and linked list will take first node of each level
    """
    
    #root will hold the head and cur to go to deeper of the linked list
    root = cur = LinkedList()
    
    queue = deque()
    
    queue.append(tree_root)
    while queue:
        cur.next = LinkedList(queue[0].value) #first node of each level
        cur = cur.next
        
        #iterate through each of the nodes of this level to get the nodes of next level
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    
    return root.next

if __name__=="__main__":
    #let's create a tree first
    nums = [1, 5, 8, 10, 15, 25, 35, 40, 55, 67, 87]
    tree_node = Tree.build_tree(nums)
    
    
    root = list_of_depths(tree_node)
    while root:
        print(root.value)
        root = root.next
    
