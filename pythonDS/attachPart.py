# 1. List, consecutive memory block
''' once the list is filled, just assign a bigger one and copy all the elements in the original list to the bigger new one'''
import random

'''the analysis of performance:
index, set value :O(1)
append(1),  the worst case is O(n
pop :O(1)
delete :O(n)
insert: O(n)

'''


class Arraylist:
    def __init__(self):
        self.exp = 0
        self.maxsize = 0
        self.lastindex = 0
        self.array = []

    def append(self, val):
        # check whether the array is full,
        if self.lastindex > self.maxsize - 1:  # that means the array[n] can be gotten
            self.__resize()  # reassign the memory and get a bigger list
        self.array[self.lastindex] = val
        self.lastindex += 1

    def __resize(self):  # call the function just use the _classname__resize()
        newsize = 2 ** self.exp  # use the exponent to get the size for each expansion
        newarray = [0] * newsize
        for i in range(self.maxsize):
            newarray[i] = self.array[i]  # copy the element in the old array to the new one

        self.maxsize = newsize
        self.array = newarray
        self.exp += 1
        # generally, the append operation is 1, while N when calling the __resize

    def __getitem__(self, item):
        if item < self.lastindex:  # not indexerror
            return self.array[item]
        else:
            raise IndexError('index out of bounds')

    def __setitem__(self, key, value):
        if key < self.lastindex:  # current last one but not the max_size since that the array can not full
            self.array[key] = value
        else:
            raise IndexError('index out of bounds')

    def insert(self, key, val):
        if self.lastindex > self.maxsize - 1:
            self.__resize()
        for i in range(self.lastindex, key - 1, -1):  # from the last one to the insert location
            self.array[i + 1] = self.array[i]  # the current one move only if after moving the next one
        self.lastindex += 1
        self.array[key] = val


''' review of recurrsion'''


# 1. encrypt the password, just move the password for m index, and then use the new location to get the mingwen

def encrypt(m):
    s = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in m:
        # find would return -1 if not found while index will raise Error
        k = (s.find(i) + 13) % 26
        res += s[k]
    return res


def decrypt(m, k):
    s = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in m:
        # find would return -1 if not found while index will raise Error
        pos = (s.find(i) + 26 - k) % 26
        res += s[pos]
    return res


def encrypt_k(m, k):
    s = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in m:
        # find would return -1 if not found while index will raise Error
        pos = (s.find(i) + k) % 26
        res += s[pos]
    return res


def modexp(x, n, p):
    if n == 0:
        return 1
    t = (x * x) % p
    tmp = modexp(t, n // 2, p)
    if n % 2 == 0:
        tmp = (tmp * x) % p
    return tmp


# Euclidean's method to compute the gcd between a and b
def gcd(a, b):
    if b == 0:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(a - b, b)


def gcd_beta(a, b):
    if b == 0:
        return a
    else:
        return gcd_beta(b, a % b)


def ext_gcd(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = ext_gcd(y, x % y)
        return (d, b, a - (x // y) * b)


def RSAgenkeys(p, q):
    n = p * q
    pgminus = (p - 1) * (q - 1)
    e = int(random.random() * n)
    while gcd(pgminus, e) != 1:
        e = int(random.random() * n)
    d, a, b = ext_gcd(pgminus, e)
    if b < 0:
        d = pgminus + b
    else:
        d = b
    return ((e, d, n))

def RSAencrypt(m,e,n):
    chunks=tochunks(m,n.bit_length()//8*2)
    enclist=[]
    for messchunk in chunks:
        c= modexp(messchunk,e,n)
        enclist.append(c)
    return enclist


def chunkstoplain(rlist, param):
    hexlist=[]
    for c in rlist:
        hexstring=hex(c)[2:]
        clen=len(hexstring)
        hexlist.append('0'* ((param-clen)%2)+hexstring)
    hstring="".join(hexlist)
    messarray=bytearray.fromhex(hstring)
    return messarray.decode('utf-8')


def RSAdecrypt(chunklist,d,n):
    rlist=[]
    for c in chunklist:
        m=modexp(c,d,n)
        rlist.append(m)
    return chunkstoplain(rlist,n.bit_length()//8*2)

def tochunks(m,chunksize):
    bytemess=bytes(m,'utf-8')
    hexstring=""
    for b in bytemess:
        hexstring+=("%02x"%b)
    numchunks=len(hexstring)//chunksize
    chunklist=[]
    for i in range(0,numchunks*chunksize+1,chunksize):
        chunklist.append(hexstring[i:i+chunksize])
    chunklist=[eval('0x'+x) for x in chunklist if x]
    return chunklist


'''datastructure: skiplist'''
# each layer has a head node, and each data node has one pointer to the next, and one pointer to the right, the height of
#the layers decided by the random event
class HeaderNode:
    def __init__(self):
        self.next=None
        self.down=None
    def getnext(self):
        return self.next
    def getdown(self):
        return self.down
    def setnext(self,node):
        self.next=node

    def setdown(self,node):
        self.down=node


class Datanode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.down=None

    def getkey(self):
        return self.key
    def getdata(self):
        return self.val

    def getnext(self):
        return self.next
    def getdown(self):
        return self.down
    def setdata(self,newdata):
        self.data=newdata
    def setnext(self,node):
        self.next=node
    def setdown(self,node):
        self.down=node


def flip():
    return random.randrange(2)
class skiplist:
    def __init__(self):
        self.head=None
    def search(self,key):
        current=self.head
        found=False
        stop=False
        while not found and not stop:
            if current==None:
                stop=True
            else:
                if current.getnext()==None:
                    # if there is no element on the right hand, just lower one level
                    current=current.getdown()
                else:
                    # if there are any other elements on the current level
                    if current.getnext().getkey()==key: # the first element except the header node of the current level
                        found=True
                    else:
                        if key<current.getnext.getkey():
                            current=current.getdown()
                        else:
                            current=current.getnext()
            if found:
                return current.getnext().getdata()
            else:
                return None



    def insert(self,key,data):
        if self.head==None:  # if no head, just create one
            self.head=HeaderNode()
            temp=Datanode(key,data)
            self.head.setnext(temp)
            # have created the current level,
            top=temp
            # continue build higher level
            while flip()==1:
                newhead=HeaderNode()

                temp = Datanode(key, data)
                temp.setdown(top)
                newhead.setnext(temp)
                newhead.setdown(self.head)
                self.head=newhead
                top=temp
        else:
            towerstack=[]
            current=self.head
            stop=False
            while not stop:
                # find out the insertion point
                if current is None:
                    stop=True
                else:
                    if current.getnext()==None:  # no node at the current level
                        towerstack.append(current)
                        current=current.getdown()
                    else:
                        if current.getnext().getkey()>key:
                            towerstack.append(current)
                            current=current.getdown()
                        else:
                            current=current.getnext()
            lowerestlevel=towerstack.pop()# the element at the top of the stack
            temp=Datanode(key,data)
            temp.setnext(lowerestlevel.getnext()) # the new node insert between the lowest level and the nextOne
            lowerestlevel.setnext(temp)
            top=temp
            while flip()==1:
                if towerstack==[]:
                    newhead=HeaderNode()
                    temp=Datanode(key,data)
                    temp.setdown(top)
                    newhead.setnext(temp)
                    newhead.setdown(self.head)
                    self.head=newhead
                    top=temp
                else:
                    nextlevel=towerstack.pop()
                    temp=Datanode(key,data)
                    temp.setdown(top)
                    temp.setnext(nextlevel.getnext())
                    nextlevel.setnext(temp)
                    top=temp











if __name__ == '__main__':
    print(encrypt('uryybjbeyq'))
    print(encrypt('helloworld'))
    s = encrypt_k('helloworld', 11)
    print(decrypt(s, 11))
