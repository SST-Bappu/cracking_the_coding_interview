import random


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1
    
    def __str__(self):
        return f"val = {self.val} and size = {self.size}"
    

    def insert(self, val: int):
        
        if val<= self.val:
            if not self.left:
                self.left = TreeNode(val)
                
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = TreeNode(val)
                
            else:
                self.right.insert(val)
        
        self.size+=1
    
    def find_random(self):
        left_size = 0 if not self.left else self.left.size
        
        rand_num = random.randint(0, self.size)
        print(rand_num, self.size, left_size)
        if rand_num == left_size:
            return self
        elif rand_num<left_size:
            return self.left.find_random()
        else:
            return self.right.find_random()


if __name__=="__main__":
    root = TreeNode(20)
    root.insert(10)
    root.insert(25)
    root.insert(12)
    root.insert(5)
    root.insert(30)
    root.insert(45)
    
    
    rand_node = root.find_random()
    print(rand_node)