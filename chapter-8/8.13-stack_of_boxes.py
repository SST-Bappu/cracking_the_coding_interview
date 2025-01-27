class Box:
    def __init__(self, h, w, d):
        self.height = h
        self.width = w
        self.depth = d
    
    
    def can_above(self, other):
        return not other or (self.height>other.height and self.width>other.width and self.depth>other.depth)


class StackOfBoxes:
    def __init__(self, boxes):
        self.boxes = boxes
        self.cache = {}
    
    def buildStack(self):
        self.boxes.sort(key=lambda box: box.height, reverse=True)
        def dfs(i):
            if i>= len(self.boxes):
                return 0
            if i in self.cache:
                return self.cache[i]
            
            max_height = 0
            bottom = self.boxes[i] if i>=0 else None
            for j in range(i+1, len(self.boxes)):
                if self.boxes[j].can_above(bottom):
                    max_height = max(max_height, dfs(j))
            
            max_height+=bottom.height if bottom else 0
            self.cache[i] = max_height
            return max_height
        
        return dfs(-1)
if __name__ == "__main__":
    boxes = [
        Box(4, 6, 7),
        Box(1, 2, 3),
        Box(4, 5, 6),
        Box(10, 12, 32)
    ]

    stack = StackOfBoxes(boxes)
    print(stack.buildStack())