'''
The tree data structure, including the implementation of a tree
heap, binary_search_tree, AVL etc.

'''


# implement a binary tree with list
import operator


def binarytree(node):
    return [node,[],[]]
def insertleft(tree,node):
    l=tree.pop(1)
    if len(l)>1:
        tree.insert(1,[node,l,[]])
    else:
        tree.insert([node,[],[]])
    return tree


def insertright(tree,node):
    r=tree.pop(2)
    if len(r)>1:
        tree.insert(2,[node,[],r])
    else:
        tree.insert(2,[node,[],[]])
def getleftchild(tree):
    return tree[1]
def getrightchild(tree):
    return tree[2]
def getrooteval(tree):
    return tree[0]
def setrooteval(tree,node):
    tree[0]=node


'''
use reference and class to implement a binary tree
'''
class BinaryTree:
    def __init__(self,val):
        self.root=val
        self.leftchild=None
        self.rightchild=None
    def insertliftchild(self,leftchild):
        l=BinaryTree(leftchild)

        if self.leftchild is None:
            self.leftchild=l
        else:
            # notice the order
            l.leftchild=self.leftchild
            self.leftchild=l
    def insertrightchild(self,rightchild):
        if self.rightchild is None:
            r=BinaryTree(rightchild)
            self.rightchild=r
        else:
            r=BinaryTree(rightchild)
            r.rightchild=self.rightchild
            self.rightchild=r
    def getrightchild(self):
        return  self.rightchild
    def getleftchild(self):
        return self.leftchild
    def seteval(self,val):
        self.root=val
    def geteval(self):
        return self.root
    def preorder(self):
        print(self.root)
        # when the recurrsive, should call the method of the child node itself
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()
'''
parse tree to express a math expression with a tree
(: add a leftchild, and set the leftchild as the current node
numbers: set the node as the numbers. return to the parent node
operator: set the node as the operator, insert the right node and set the right node as the current node
): return to the parent node.
how to store the parent node: stack
'''

def binaryparsetree(exp):
    fplist=exp.split()
    pstack=[]
    tree=BinaryTree('') # set a default parent tree
    pstack.append(tree)  # first, need to push the root node into the parent node stack
    cur=tree
    for i in fplist:
        if i =='(':
            cur.insertliftchild('')
            pstack.append(cur)
            cur=cur.getleftchild()
        elif i not in '+-*/)':
            cur.seteval(eval(i))
            cur=pstack.pop()
        elif i in '+-*/':
            cur.seteval(i)
            cur.insertrightchild('')
            pstack.append(cur)
            cur=cur.getrightchild()
        elif i==')':
            cur=pstack.pop()
        else:
            raise ValueError('no such an operator'+ i)
    return tree


# compute the result of the binary Tree via recurrsion
def evaluate(parsetree):
    # def a dict for mapping the operator to the function
    op={'*':operator.mul,'/':operator.truediv,'+':operator.add,'-':operator.sub
    }
    left=parsetree.getleftchild()
    right= parsetree.getrightchild()
    if left and right:
        # the sub tree who has right and left, the root must be an operator
        fn=op[parsetree.geteval()]
        return fn(evaluate(left),evaluate(right))
    else:
        # leaf node has to be a number
        return parsetree.geteval()

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
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=Treenode(key,val)
        self.size+=1
    # helper function
    def _put(self,key,val,current):
        if key <current.key:
            if current.hasleftchild():
                self._put(key,val,current.leftchild)
            else:
                current.leftchild=Treenode(key,val,parent=current)
        else:
            if current.hasrightchild():
                self._put(key,val,current.rightchild)
            else:
                current.rightchild=Treenode(key,val,parent=current)
    def __setitem__(self, key, value):
        self.put(key,value)
    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None
    def _get(self,key,current):
        if not current:
            return None
        elif current.key==key:
            return current
        elif key< current.key:
            return self._get(key,current.leftchild)
        else:
            return self._get(key,current.rightchild)
    def __getitem__(self, item):
        self.get(item)
    def __contains__(self, item):
        if self._get(item,self.root):
            return True
        else:
            return False


    '''
    delete a key, first, locate the key
    '''
    def delete(self,key):
        if self.size>1:
            node2remove= self._get(key,self.root)
            if node2remove:
                self.remove(node2remove)
                self.size-=1  # don't forget change the size of the binary search tree
            else:
                raise KeyError('key not in the tree')
        elif self.size==1 and self.root.ket==key:
            self.root=None
            self.size=0
        else:
            raise KeyError('key not in the tree')
    def __delitem__(self, key):
        self.delete(key)
    '''
    three possibility for deleting a node from a binary search tree:
    1. the deleting node has no child nodes
    2. the deleting node has one child nodes
    3.the deleting node has two child nodes.
    '''
    #possible 1  the deleting node is a leaf node, just set its parent node's corresponding node as None
    if current.isleaf():  # jutisfy if it is a leaf node
        if current==curent.parent.leftchild:  # see if it is a leftchild of the parent node or rightchild
            current.parent.leftchild=None
        else:
            current.parent.rightchild=None




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
# print the expression using in order
def printexp(tree):
    ans=''
    if tree:
        ans='('+printexp(tree.getleftchild())
        ans+=str(tree.geteval())
        ans=ans+printexp(tree.getrightchild())+')'
    return ans


def postorder(tree):
    if tree:
        postorder(tree.leftchild)
        postorder(tree.rightchild)
        print(tree.val)

# postorder to get the result of computation
def postordereval(tree):
    op = {'*': operator.mul, '/': operator.truediv, '+': operator.add, '-': operator.sub}
    if tree:
        left=postordereval(tree.leftchild)
        right=postordereval(tree.right)
        if left and right:
            return op[tree.geteval()](left,right)
        else:
            return tree.geteval()


