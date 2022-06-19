# chapter4  recursion
'''
three elements: 1) halt condition  2) reduce the problem into a smaller one 3) call itself

'''
from turtle import *

#add
def add(nums):
    if len(nums)==1:
        return nums[0]
    else:
        return nums[0]+add(nums[1:])



# mutiple
def multiple(alist):
    if len(alist)==1:
        return alist[0]
    else:
        return alist[0]* multiple(alist[1:])

# factorize
def factorize(x):
    if x==1:
        return x
    else:
        return x*factorize(x-1)

def convert(num,base):
    # string=''
    convertstring= '0123456789ABCDEF'
    if num < base:
        return convertstring[num]
    else:
        # notice concatenate the output and the recursive call, and the order
        return  convert(num//base,base)+convertstring[num % base]
stack=[]
def convert_stack(num,base,stack):
    # string=''
    convertstring= '0123456789ABCDEF'
    if num < base:
        stack.append(convertstring[num])

    else:
        # notice concatenate the output and the recursive call, and the order
        stack.append(convertstring[num % base])
        convert_stack(num//base,base,stack)

    return stack


# spiral
from turtle import *

def drawspiral(turtle, linelen):
  if linelen>0:
    turtle.forward(linelen)
    turtle.right(90)
    drawspiral(turtle,linelen-5)



# draw tree
def tree(branchline,t):
  if branchline >5:
    t.forward(branchline)
    t.right(20)
    tree(branchline-15,t)
    t.left(40)
    tree(branchline-10,t)
    t.right(20)
    t.backward(branchline)









def drawTriangle(points,color, turtle):
  turtle.fillcolor(color)
  turtle.up()
  turtle.goto(points[0])
  turtle.down()
  turtle.begin_fill()
  turtle.goto(points[1])
  turtle.goto(points[2])
  turtle.goto(points[0])
  turtle.end_fill()


def getMid(p1,p2):
  return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)



def sierpinski(points,degree,turtle):
  colormap=['blue','red','green','white','yellow','orange','violet']
  drawTriangle(points, colormap[degree],turtle)
  if degree >0:
    sierpinski([points[0], getMid(points[0],points[1]),getMid(points[0],points[2])], degree-1, turtle)
    sierpinski([points[1], getMid(points[0],points[1]),getMid(points[1],points[2])], degree-1, turtle)
    sierpinski([points[2], getMid(points[2],points[1]),getMid(points[0],points[2])], degree-1, turtle)


def movetower(height, start, end, mid):
    if height>=1:
        movetower(height-1,start,mid, end)
        movedisk(start,end,height)
        movetower(height-1, mid,end, start)
def movedisk(fp,tp,height):
    print('move '+ str(height)+'  disk from', fp ,'to', tp)




'''
change the money and dynamic programming


'''


# no memo just recursive

def changemoney(coinlist,change):
    mincoins=change #or infinity
    if change in coinlist:
        return 1   # fundamental condition
    else:
        for c in [x for x in coinlist if x<= change]:
            # get the coins that less than the current value
            numcoins=1+changemoney(coinlist,change-c)
            if numcoins < mincoins:
            #cannot call double times, we need to store the recursive result
                mincoins=numcoins
    return mincoins



# with memos to store the intermediate result:
def changemoney_memo(coinlist,change):
    mincoins=change #or infinity
    changememo=[0]*(change+1)  # or use dict
    if change in coinlist:
        changememo[change]=1
        return 1   # fundamental condition
    elif  changememo[change]>0 :
        # if recursive call, it can use the recorded intermediate result
        return changememo[change]
    else:
        for c in [x for x in coinlist if x<= change]:
            # get the coins that less than the current value

                numcoins=1+changemoney(coinlist,change-c)
                # when change-c not 0 in the changememo, it can just pickup the value via the elif statement
                if numcoins < mincoins:
                #cannot call double times, we need to store the recursive result
                    changememo[change]=numcoins
                    mincoins= numcoins
    return mincoins


# dynamic programming, from small to big
def changemoney_dp(coinlist, change):
    # not recursive, but a table-based method
    mincoins= (change+1)*[0]
    for cents in range(change+1):
        coincount=cents
        # record the min coins for the current value
        for j in [c for c in coinlist if c<= cents]:
            # less than the current value
            if 1+mincoins[cents-j]<coincount:
                coincount=1+mincoins[cents-j]
        mincoins[cents]=coincount
    return mincoins[change]

## add the traceback  to track the coins that used
def changemoney_dp(coinlist, change):
    # not recursive, but a table-based method
    mincoins= (change+1)*[0]
    coinused=(change+1)*[0]
    for cents in range(change+1):
        coincount=cents
        newcoin=1
        # record the min coins for the current value
        for j in [c for c in coinlist if c<= cents]:
            # less than the current value
            if 1+mincoins[cents-j]<coincount:
                coincount=1+mincoins[cents-j]
                newcoin=j
        mincoins[cents]=coincount
        coinused[cents]=newcoin
    return mincoins[change],coinused

def tracecoins(coinused,change):
    coin= change
    while coin >0:
        thiscoin=coinused[coin]
        print(thiscoin)
        coin-=coinused[coin]



if  __name__=='__main__':

    # turtle = Turtle()
    # win = turtle.getscreen()
    # points = [(-500, -250), [0, 500], (500, -250)]
    # #call the sierpinski triangle
    # sierpinski(points, 5, turtle)
    # # call the tree

    # t = Turtle()
    # win = t.getscreen()
    # t.left(90)
    # t.up()
    # t.backward(300)
    # t.down()
    # t.color('green')
    # tree(110, t)
    # # win.exitonclick()
    # movetower(2,'start','end','mid')
    change = 63
    c1 = [1, 5, 10, 21, 25]
    mincoins, coinused = changemoney_dp(c1, change)
    print(mincoins)
    tracecoins(coinused, change)