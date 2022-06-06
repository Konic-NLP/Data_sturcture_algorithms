'''
Created on 2021年12月27日

@author: Konic

'''

import string
"""
============================================================================================================
stack
"""

'''
栈的实现
example: plate and the return button for the tab just closed of the internet broswer
'''
    
class Stack(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.stack=[]
    
    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
       return  self.stack.pop()
        
    def __len__(self):
        return len(self.stack)
    def peek(self):
        return self.stack[len(self.stack)-1]
    def is_empty(self):
        return self.stack==[]
        
    def clean(self):
        self.stack=[]
        

'''
check the parenthess, just ensure that each one would occur the matched one in the next step, not cross
'''

def parcheck(string):
    dic={'(':')','[':']','{':'}'}
    s=Stack()
    for i in string:
        if i in dic:
            s.push(i)
        elif s.is_empty(): #右边的括号如果比左边的多，也就是提前把栈清空了，返回false
                return False
        else:
            p=s.pop()
            if dic[p]!=i:
                return False
    return s.is_empty()




'''
convert the different base between numbers
'''
#这里假设Numbers必须大于0
def convertbase(numbers,base):
    digits='0123456789ABCDRF'
    s=Stack()
    #余数压栈，直到余数=0
    while numbers>0:
        rem=numbers%base
        s.push(rem)
        numbers=numbers//base
    
    str=''
    #逆序输出（出栈）
    while not s.is_empty():
        str=str+digits[s.pop()]
    return str

print(convertbase(100, 7))

'''
前中后序表达式的转换
'''
#中序到后序

def infixtopostfix(exp):
    #如果是操作数，直接输入到后缀表达式
    #如果是左括号，压栈；如果是右括号，弹出所有栈内元素，直到遇到左括号
    #如果是操作符，比较操作符优先级，输出所有比当前操作符优先级更高的操作符，并将当前操作符压栈
    #最后将所有栈内剩余的操作符输出到后缀表达式
    order={'*':3,'/':3,'+':2,'-':2,'(':1}  #set the priority of the operation
    postfix=''
    s=Stack()
    infix=exp.split()
    for i in infix:
        if i.isalpha():
            postfix+=i
        elif i=='(':
            s.push(i)
        elif i==')':
            token=s.pop()
            while token!='(':
                postfix+=token
                s.pop()
                
        else:
            while( not s.is_empty()) and (order[s.peek()]>= order[i]):
                postfix+=s.pop()
            s.push(i)
    while not s.is_empty():
        postfix+=s.pop()
    
    return postfix

#计算后缀表达式的值，碰到操作数压栈，碰到操作符取出栈顶两个元素并进行运算（注意顺序，尤其是除法），并将结果压栈
def evalpost(exp):
    exp=exp.split()
    s=Stack()
    for i in exp:
        if i not in '+-*/':
            s.push(int(i))
        else:
            first=s.pop()
            second=s.pop()
            result=do(i,second,first)# or eval(second+i+first).
            s.push(result)
    return s.pop()

def do(i,first,second):
    if i=='+':
        return first+second
    elif i=='*':
        return first* second
    elif i=='-':
        return first-second
    else:
        return int(first/second)
    
'''
=================================================================================================
'''    
   
   
'''
================================================================================================
queue
===============================================================================================
'''
class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0, item)
    def isempty(self):
        return self.items==[]
    def dequeue(self):
        return self.items.pop()
        
    def __len__(self):
        return len(self.items)

'''
hot potato
'''
#模拟一个环，队列最开头的马上加入到队尾

def hotpotato(namelist,num):
    queue=Queue()
    for name in namelist:
        queue.enqueue(name)
    
    while len(queue)>1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
    
        s=queue.dequeue()
        print(s)
    
    return queue.dequeue()


# print(hotpotato(['bill','david','susan','jane','kent','brad'], 7))
'''
simulate the printer tasks
'''
class Printer:
    def __init__(self,ppm):
        self.pagerate= ppm
        self.currentTask=None
        self.reamintime= 0

    def tick(self):
        if self.currentTask!= None:
            self.reamintime=self.reamintime-1
            if self.reamintime<=0:
                self.currentTask = None
    
    
    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False
    
    def startnext(self,nexttask):
        self.currentTask=nexttask
        self.reamintime=nexttask.getpages()* 60/self.pagerate
        
        
import random

class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages= random.randrange(1,21)
        
    def getstamp(self):
        return self.timestamp
    
    def getpages(self):
        return self.pages
    
    def waittime(self,currenttime):
        return currenttime-self.timestamp
    
    
def simulation(numseconds,pagesperminute):
    printer=Printer(pagesperminute)
    printqueue=Queue()
    waittimes=[]
    for currentsecond in range(numseconds):
        
        if newprinttask():
            task=Task(currentsecond)
            printqueue.enqueue(task)
        if (not printer.busy()) and (not printqueue.isempty()):
            nexttask=printqueue.dequeue()
            waittimes.append(nexttask.waittime(currentsecond))
            printer.startnext(nexttask)
        printer.tick()
        
    averagetime=sum(waittimes)/len(waittimes)
    print('average wait %6.2f secs %3d tasks remaining.'%(averagetime,len(printqueue)))
def newprinttask():
    num=random.randrange(1,181)
    if num==180:
        return True
    else:
        return False  
    
for i in range(10):
    simulation(3600,5 )
    
    

'''
deque双端队列
'''
class Deque:
    def __init__(self):
        self.deque=[]
        
    def isempty(self):
        return self.deque==[]
    def __len__(self):
        return len(self.deque)
    def addfront(self,x):
        self.deque.append(x)
    def addrear(self,x):
        self.deque.insert(0, x)
    def removefront(self):
        return self.deque.pop()
    def removerear(self):
        return self.deque.pop(0)


'''
检测回文
'''
s='abc i1='
s=[i for i in s if i in string.ascii_lowercase]
def checker(s):
    deque=Deque()
    for i in s:
        deque.addfront(i)
    while len(deque)>1:
        front=deque.removefront()
        rear=deque.removerear()
        if front !=rear:
            return False
        
    return True



'''
检测回文2，既然是回文数，应该把整个翻转，也不会发生任何变化,即  abcdedcba= abcdedcba[::-1]


'''

# 方法3， 只将一半进行翻转，应该和前边一个完全一样即  abcba ba[::-1]==ab
'''
==================================================================================================
'''
'''
list===================================================================
'''
#使用嵌套类来构建无序链表，其中链表中的每个元素使用的是node类，含有数据和指针
class node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
    def setdata(self,data):
        self.data=data
    def setnext(self,next):
        self.next=next
    def getdata(self):
        return self.data
    def getnext(self):
        return self.next
#implement a unordered List
class unorderlist:
    def __init__(self):
        self.head=None
        '''
        新add的元素永远是head，然后将之前的head设定为当前新head的下一个元素。第一个add的元素也就成为最后一个元素，且此元素的下一个元素为none
        '''
    def add(self,item): #O(1)
        temp=node(item)  #使用了另一个类进行初始化
        temp.setnext(self.head)
        self.head=temp#必须先将之前的head设定完当前节点的下一个，再把当前节点设定为新head，否则之前的head将不存在
    def isempty(self):  #O(1)
        return self.head==None
    #check whether the orderedlist is empty since the head is none when it's empty'、
    def length(self):#O(n)
        cnt=0
        current=self.head
        while current !=None: #最后一个元素的下一个元素等于默认的head=none，停止，返回当前cnt
            cnt+=1
            current=current.getnext()
        return cnt
    
    def search(self,item):  #O(n)
        current=self.head
        while current!=None:
            if current.getdata()==item:
                return True
            else:
                current=current.getnext()
                
                
        return False
    def remove(self,item):#需要考虑HEAD的特殊情况
        current=self.head
        previous=None
        found=False
        while current!=None and not found:
            if current.getdata()==item:
                if current==self.head:#如果正好是移除head,就将新head设为当前head的下一个。
                    self.head=current.getnext()
                else:
                    previous.setnext(current.getnext())
                found=True
                
    
            else:
                previous=current
                current=current.getnext()
                
    def index(self,index):
        cnt=0
        current=self.head
        while current !=None:
            if cnt==index:
                return current.getdata()
            else:
                cnt+=1
                current=current.getnext()
        
    
    
    def pop(self):  
        current=self.head
        previous=None
        while current!=None:
            if current.getnext()==None:
                previous.setnext(current.getnext())
                return current.getdata()
            previous=current
            current=current.getnext()
            
    def insert(self,i,item):#插入值在插入点之后
        cnt=0
        current=self.head
 
        while cnt!=i:
            cnt+=1
           
            current   = current.getnext()     
        new=node(item)  
        new.setnext(current.getnext())
        current.setnext(new)  
            
# ol=unorderlist()
# ol.add(17)
# ol.add(4)
# ol.add(28)
# ol.add(7)
# ol.remove(17)
# ol.insert(1,19)
# print(ol.pop(),ol.head.getnext().getnext().getdata())

class OrderedList(unorderlist):  #O(n)
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def length(self):
        cnt=0
        current=self.head
        while current!=None:
            cnt+=1
            current=current.getnext()
        return cnt
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while current!= None and not found:
            if current==item:
                found=True
            else:
                previous=current
                current=current.getnext()
                
        if current==self.head:
            self.head=current.getnext()
        else:
            previous.setnext(current.getnext())
    def search(self,item):
  
        current=self.head
        stop=False
        while current!=None and not stop:
            if current.getdata()==item:
                return True
            elif current.getdata()> item:
                stop=True
            else:
                current=current.getnext()
        return False
    
    def add(self,item):
        current=self.head
        previous=None
        stop=False
        new=node(item)
        while current !=None and not stop:
            if item<current.getdata():
                stop=True
            else:
                previous=current
                current=current.getnext()
            
        if previous ==None:
            self.head=node(item)
            self.head.setnext(current)
        else:
            previous.setnext(new)
            new.setnext(current)
            
            
            