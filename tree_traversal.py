class newNode:  
  
    # Construct to create a newNode  
    def __init__(self, key):  
        self.data = key  
        self.left = None
        self.right = None
  
# function to fill the map 
def fillMap(root, d, l, m): 
    if(root == None): 
        return
      
    if d not in m: 
        m[d] = [root.data,l] 
    elif(m[d][1] > l): 
        m[d] = [root.data,l] 
    fillMap(root.left, d - 1, l + 1, m) 
    fillMap(root.right, d + 1, l + 1, m) 