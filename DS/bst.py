class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

 
 
  
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
 
def lookup(root,key):
    if root is None:
        return "Not Found"
    if root.val == key:
        return "found"
    else:
        if key > root.val:
            return lookup(root.right, key)
        else:
            return lookup(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
        

def postorder(root):
    if root:        
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def bfs(root):
    current_node = root
    data_list = []
    queue = []
    queue.append(current_node)
    while(len(queue)>0):
        current_node = queue.pop()
        data_list.append(current_node.val)
        if(current_node.left):
            queue.append(current_node.left)
        if(current_node.right):
            queue.append(current_node.right)
    print(data_list)
    return data_list
    
def remove(root,key):
    parent = None
    if root is None:
        print("empty tree")
    if key == root.val:
        ele = root
        new_ele = root.right.left
        root = new_ele
        del ele
        
    if key < root.val:
        parent = root
        remove(root.left,key)
    else:
        parent = root
        remove(root.right,key)


if __name__ == "__main__": 
    r = Node(50)
    r = insert(r, 30)                                                   
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 52)
    r = insert(r, 50)
    r = insert(r, 55)
    #remove(r,60)
    # r = insert(r, 80)
    print("inorder",inorder(r))
    bfs(r)
    #print("postorder",postorder(r))
    #print("preorder",preorder(r))
    #print(lookup(r,75))