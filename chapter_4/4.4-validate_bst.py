from interview.utils.bst_tree import Tree, Node

def validate_bst(root: Node, left :int = float('-inf'), right :int = float('inf')) -> bool:
    """
    :param root: root of the tree
    :param left: left boundary, initially -infinity as the left leave can be any number that less than its parent node
    :param right: similarly right boundary can be infinity, any number greater than its parent
    """
    if not root:
        return True
    
    if root.value < left or root.value>=right:
        #if current root is less than left value or greater than the right value, it's not a valid BST
        return False
    """
        10
    5       15
    
    Let's take the tree above as an example. For the root node, left boundary and right boundary are
    consecutively -inf and inf. However, for the node with value 5, the right boundary is 10 and
    left boundary is -inf. Similarly, for the node with value 15, the left boundary is 10 and right
    boundary is inf.
    That's what we did here.
    """
    return validate_bst(root.left, left, root.value) and validate_bst(root.right,root.value, right)



if __name__=="__main__":
    nums = [1, 5, 8, 10, 15, 25, 35, 40, 55, 67, 87]
    
    #I am using a previously created class to build a binary search tree
    tree = Tree.build_tree(nums)
    print(validate_bst(tree)) #it should return True
    
    #let's make some intentional changes to invalidate the tree and then check again
    #tree.left.value = 200
    #tree.right.value = 100
    #tree.right.right.value = 5
    print(validate_bst(tree))
    
        