class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None


class BinaryTree():
    def __init__(self):
        self.root=None

    # 전위순회
    def preorder(self,n):
        if n!=None:
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    # 중위순회
    def inorder(self,n):
        if n!=None:
            if n.left:
                self.preorder(n.left)

            if n.right:
                self.preorder(n.right)

    # 후위순회
    def postorder(self,n):
        if n!=None:
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    '''
    레벨순회
    
    '''

    def height(self,root):
        if root==None:
            return 0
        return max(self.height(root.left), self.height(root.right)+1)


tree=BinaryTree()
arr=[1,2,3,4,5]



