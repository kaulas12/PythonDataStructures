class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftNode = None
        self.rightNode = None
        
objBinaryTree = TreeNode('Drinks')
objLeftChild = TreeNode('Hot')
objRightChild = TreeNode('Cold')

objBinaryTree.leftNode=objLeftChild
objBinaryTree.rightNode=objRightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return None
    print(rootNode.data)
    preOrderTraversal(rootNode.leftNode)
    preOrderTraversal(rootNode.rightNode)
   
def inOrderTraversal(rootNode):
    if not rootNode:
        return None
    inOrderTraversal(rootNode.leftNode)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightNode)
    
def postOrderTraversal(rootNode):
    if not rootNode:
        return None
    postOrderTraversal(rootNode.leftNode)
    postOrderTraversal(rootNode.rightNode)
    print(rootNode.data)
    
postOrderTraversal(objBinaryTree)
