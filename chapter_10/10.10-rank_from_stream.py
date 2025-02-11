class RankNode:
    def __init__(self, data=None):
        self.data = data
        self.left_count = 0
        self.left = None
        self.right = None
    
    def insert(self, data):
        if not self.data:
            self.data = data
            return
        if data <= self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = RankNode(data)
            self.left_count+=1
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = RankNode(data)
    
    def get_rank(self, data):
        if data==self.data:
            return self.left_count
        if data<=self.data:
            return self.left.get_rank(data) if self.left else -1
        else:
            right_rank = self.right.get_rank(data) if self.right else -1
            return self.left_count+1+right_rank if right_rank!=-1 else -1
        
            


arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

def dfs(nod):
    if not nod:
        return
    dfs(nod.left)
    print(nod.data)
    print(f'---> {nod.left_count}')
    dfs(nod.right)
node = RankNode()
for numb in arr:
    node.insert(numb)


for numb in arr:
    print(node.get_rank(numb))

# dfs(node)