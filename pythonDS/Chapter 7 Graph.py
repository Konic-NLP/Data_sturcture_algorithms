
'''Graph'''
queue=__import__('Chapter 3 Stack;Queue;Array')
#implement a Graph with connection tables

class Vertex:
    # store the id and the connecting vertex with a dict
    def __init__(self,key):
        self.id = key
        self.connect={}
    def addNeibor(self,key,weight=0):
        self.connect[key]=weight
    def __str__(self):
        return str(self.id) +'connect to: '+str([x.id for x in self.connect ])
    def getConnections(self):
        return self.connect.keys()
    def getid(self):
        return self.id
    def getweight(self,nbr):
        return self.connect[nbr]
    def setdistance(self,dist):
        self.dist=dist
    def getdistance(self):
        return self.dist
    def setcolor(self,color):
        self.color=color
    def getcolor(self,color):
        return self.color
    def setpred(self,pred):
        self.pred=pred
    def getpred(self):
        return self.pred
    def setDiscovery(self, time):
        self.discovery = time
    def setfinish(self,time):
        self.finish=time




class Graph:
    def __init__(self):
        self.vertlist={}
        self.numvertex=0
    def addvertex(self,key):
        vertex=Vertex(key)
        self.numvertex+=1
        self.vertlist[key]= vertex
        return vertex
    def getvertex(self,n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None
    def __contains__(self, item):
        return item in self.vertlist
    def addEdge(self,f,t,cost=0):
        if f not in self.vertlist:
            x=self.addvertex(f)
        if t not in self.vertlist:
            y=self.addvertex(t)
        self.vertlist[f].addNeibor(self.vertlist[t],cost)
    def getVertices(self):
        return self.vertlist.keys()
    def __iter__(self):
        return iter(self.vertlist.values())


'''Breadth First Search, BFS'''

# Word ladder: any words that there exits just one char between them, they can be connected
from collections import defaultdict
def buildgraph(wordfile):
    d=defaultdict(list)
    g=Graph()
    for line in wordfile:
        word=line
        for i in range(len(word)):
            bucket=word[:i]+'-'+word[i+1:]
            # if bucket not in d:
                # d[bucket]=[]
            # else:
            # print(d.get(bucket,[]),bucket)
            d[bucket].append(word)
            # d.get(bucket,[]).append(word)
            # print(d)
    for k,v in d.items():
        # print(k,v)
        for word1 in v:
            for word2 in v:
                if word1!= word2:
                    # print(word1,word2)
                    g.addEdge(word1,word2)
    return g


words=['fool','pool','pole','poll','pale','sale','sage']
# O(V+E)
def bfs(g:Graph,start):
    start.setdistance(0)
    start.setpred(None)
    queue=[]
    queue.insert(0,start)
    while queue:
        current=queue.pop() # get the first one in the start of the queue
        for nbr in current.getConnections(): # iterate each neighbor of the current node
            if nbr.getcolor() =='white':  #unvisited
                nbr.setcolor('gray')     # first visited
                nbr.setdistance(current.getdistance()+1)
                nbr.setpred(current)#  track the pred
                queue.insert(0,nbr)
        current.setcolor('black') # all the connections has been visited

def traverse(y:Vertex):
    x=y
    while x.getpred():
        print(x.getid())
        x=x.getpred()
    print(x.getid())


'''DFS depth first search for knight traverse'''
'''any location on the tablet is a vertex,and the path is an edge'''


def KnightGraph(bdsize):
    kg=Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeid=pos2id(row,col,bdsize)  # get the representation of the current location
            nextsteps=legalmoves(row,col,bdsize)  # get the location of the next possible moves

            for pos in nextsteps:   # iterate each possible move
                nextid=pos2id(pos[0],pos[1],bdsize) # transfer the representation
                kg.addEdge(nodeid,nextid)  # add the edge
    return kg
def pos2id(x,y,bdszie):
    if x<bdszie and y<bdszie:
        return x*5+y
def legalmoves(x,y,bdsize):
    newmoves=[]
    moves=[(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]
    for i in moves:
        if x+i[0] >=0 and x+i[0]<bdsize and y+i[1]>=0 and y+i[1]<bdsize:
            # print(x+i[0],y+i[1])
            newmoves.append((x+i[0],y+i[1]))
    return newmoves


'''
n:current depth
path: the visited path
u: intended vertex
limit: the number of vertices in the path
'''

# only if that one way cannot achieve the goal, just throw out the current path and check out the other branch
def KnightTour(n,path,u:Vertex,limit):
    u.setcolor('gray')
    path.append(u)
    if n<limit:  # if not traverse
        nbrlist=list(u.getConnections())
        i=0
        done=False
        # traverse the child nodes of tehe current node
        while i <len(nbrlist) and not done:
            if nbrlist[i].getcolor() =='white':
                done=KnightTour(n+1,path,nbrlist[i],limit)
            i+=1
        # if traverse all the neighbor nodes but not complete the iteration
        if not done:
            path.pop()  # traceback, set the last one unvisited
            u.setcolor('white')
    else:
        done=True
    return done

def orderbyavail(n:Vertex):
    reslist=[]
    for v in n.getConnections():
        if v.getcolor()=='white':
            c=0
            for w in v.getConnections():
                if w.getcolor()=='white':
                    c+=1
            reslist.append((c,v)) # get nerighbor's neighbor and sort them by the neighbor's nums
    reslist.sort(key=lambda x:x[0])
    # traverse each neighbor based on the number of nerighbors they have (ascending)
    return [y[1] for y in reslist]

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time=0
        self.discovery=0
        self.finish=0
    def dfs(self):
        for vertex in self:
            vertex.setcolor('white')
            vertex.setpred(-1)
        for vertex in self:
            if vertex.setcolor()=='white':
                self.dfsvisit(vertex)

    def dfsvisit(self, vertex:Vertex):
        vertex.setcolor('gray')
        self.time+=1
        vertex.setDiscovery(self.time)
        for neighbor in vertex.getConnections():
            if neighbor.getcolor()=='white':
                neighbor.setpred(vertex)
                self.dfsvisit(neighbor)
        vertex.setcolor('black')
        self.time+=1
        vertex.setfinish(self.time)
