'''
Created on 2021年12月23日

@author: Konic
'''
from timeit import Timer, timeit
from pip._vendor.distlib._backport.tarfile import TUREAD

'''
为何不使用准确的时间，因为执行时间会受到计算机性能，编程语言等因素的影响

参数N一般称为问题规模。
'''



'''
异序词检测：相同的字母，但是顺序不一样
'''


#法一： 遍历两个字符串，将第二个字符串转换为list,找s1每个字符时，初始为false，当在s2中找到对应字符时，s2中该位置变none，否则查找失败

def detect(s1,s2):
    alist=list(s2)
    pos1=0
    answer=True
    while pos1 <len(s1) and answer:
        pos2=0
        found=False
        while pos2<len(alist) and not found:
            if s1[pos1]==alist[pos2]:
                found=True
            else:
                pos2+=1
        
        if found:
            alist[pos2] =None
        else:
            answer=False
        pos1+=1
    return answer


#法一的for循环版，原理相同，当在s2整个字符串中找到一个s1对应字符时，则将s2种对应字符变none，同时表示找到了，如果遍历整个s2未找到s1当前字符在s2中对应字符，则查找失败


nums= [1,1]
for  i in nums:
    print(nums.count(i))
def detect1(s1,s2):
    answer=True
    alist=list(s2)
    
    for i in s1:
        found=False
        for k,v in enumerate(alist):
            if i==v:
                
                alist[k]=None
                found=True
                continue
          
        if not found:    
            answer=False
    return answer

#法2：排序法，排序后两个字符串应相同

def detect3(s1,s2):
    a=list(s1)
    b=list(s2)
    a.sort()
    b.sort()
    #复杂写法:

    
#     for i in range(len(a)):
#         if a[i]==b[i]:
#             continue
#         else:
#             return False
#     return True
    if a==b:
        return True
    else:
        return False


# 法4： 两个字符串异序，说明其字符计数相同
from collections import Counter
def detect4(s1,s2):
    a=dict()
    b=dict()
    for i in s1:
        a[i]=a.setdefault(i,0)+1

    for j in s2:
        b[j]=b.setdefault(j,0)+1
#     a=Counter(s1)
    
#     b=Counter(s2)
    if a==b:
        return True
    else:
        return False
print(detect4('earth', 'heart'))    



'''
四种创建前1000个数list的方法
'''
        
def f1():
    s=[]
    for i in range(10000):
       s+=[i]
    return s
       
def f2():
    s=[]
    for i in range(10000):
        s.append(i)
    return s
        
def f3():
    return list(range(10000))
    
def f4():
    return [i for i in range(10000)]
#test the time of the function, also you can create an  instance of Timer(), then use Timer.timeit() function to calculate the time 
t1=timeit('f1()','from __main__ import f1',number=1000)
t2=timeit('f2()','from __main__ import f2',number=1000)
t3=Timer('f3()', 'from __main__ import f3',1000)
t4=Timer('f4()', 'from __main__ import f4',1000)

print(t1,t2)
a=f1()
b=f2()
c=f3()
d=f4()

