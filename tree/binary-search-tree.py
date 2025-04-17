class Node:
    def __init__(self, value):
        self.Left = None
        self.Right = None
        self.Value = value        

def insert_node(root, value):
    if value < root.Value:
        if root.Left is None:
            print("Parent:", root.Value, "Left Child:", value)
            root.Left = Node(value)
        else:
            insert_node(root.Left, value)
    elif value > root.Value:
        if root.Right is None:
            print("Parent:", root.Value, "Right Child:", value)
            root.Right = Node(value)
        else:
            insert_node(root.Right, value)

def preorder(root):
    print(root.Value, end=" ")
    if root.Left is not None:
        preorder(root.Left)
    if root.Right is not None:
        preorder(root.Right)
    
def inorder(root):
    if root.Left is not None:
        inorder(root.Left)
    print(root.Value, end=" ")
    if root.Right is not None:
        inorder(root.Right)

def postorder(root):
    if root.Left is not None:
        postorder(root.Left)
    if root.Right is not None:
        postorder(root.Right)
    print(root.Value, end=" ")

if __name__ == "__main__":
    root = Node(7)
    for x in [5, 11, 6, 3, 8, 15]:
        insert_node(root, x)
    
    print("PreOrder:")
    preorder(root)
    print("\nInOrder:")
    inorder(root)
    print("\nPostOrder:")
    postorder(root)
    