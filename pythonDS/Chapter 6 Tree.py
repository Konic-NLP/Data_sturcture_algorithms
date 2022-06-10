'''
The tree data structure, including the implementation of a tree
heap, binary_search_tree, AVL etc.

'''



'''
Binary Heap

the time complexity oos O(logn)
minheap: the minimum element is always at the first of the queue
maxheap: the maximum element is always at the first of the queue

structural property: complete bisect tree:Binary heap is a complete bisect tree. That means all the sub tree are full except the bottom layer
The index of left child is 2n and the index of the right child is 2n+1 if n is the index of the parent node
ordered property:the child node are both bigger than the parent node 
'''

class binaryheap:
    def __init__(self):
        self.heaplist=[0]
        self.size=0
    def insert(self,i):
        self.heaplist.append(i)
        self.size+=1
        self.percup(self.size)
    def percup(self,i):
        while i //2 >0:
            # if the child node less than the parent node of that, they should change
            if self.heaplist[i]< self.heaplist[i//2]:
                self.heaplist[i],self.heaplist[i//2]=self.heaplist[i//2],self.heaplist[i]
            i=i//2








'''
Binary search tree: which can be implemented to mock the function of the hashtable and the dict

the property of bisect search: left child less than the parent node and the right child node is greater than 
parent node.

'''

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0

    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()


class Treenode:
    # the parameter for the constructor, the key, value pair(for dict), the left child, the right child, and the parent child
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key=key
        self.value=value
        self.leftchild=left
        self.rightchild=right
        self.parent=parent
    def hasleftchild(self):
        return self.leftchild
    def hasrightchild(self):
        return self.rightchild

    def isleftchild(self):
        return self.parent and self.parent.leftchild==self
    def isrightchild(self):
        return self.parent and self.parent.rightchild==self

    def isroot(self):
        # root node doesn't has a parent node
        return not self.parent
    def isleaf(self):
        # the leafnode doesn't has any child node
        return not self.leftchild and not self.rightchild
    def hasanychild(self):
        return self.rightchild or self.leftchild
    def hasbothchild(self):
        return self.rightchild&self.leftchild
    def repalcenode(self,key,value,lc,rc):
        self.key=key
        self.value=value
        self.leftchild=lc
        self.rightchild=rc
        # since it store the parent node information, so when the child node information changed, the parent information
        # of the child node should also be updated
        if self.hasleftchild():
            self.leftchild.parent=self
        if self.hasrightchild():
            self.rightchild.parent=self




def preorder(tree):
    if tree:
        print(tree.val)
        preorder(tree.leftchild)
        preorder(tree.rightchild)
def inorder(tree):
    if tree:
        inorder(tree.leftchild)
        print(tree.val)
        inorder(tree.rightchild)

def postorder(tree):
    if tree:
        postorder(tree.leftchild)
        postorder(tree.rightchild)
        print(tree.val)