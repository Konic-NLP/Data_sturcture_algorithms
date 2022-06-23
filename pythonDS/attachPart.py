#1. List, consecutive memory block
''' once the list is filled, just assign a bigger one and copy all the elements in the original list to the bigger new one'''
'''the analysis of performance:
index, set value :O(1)
append(1),  the worst case is O(n
pop :O(1)
delete :O(n)
insert: O(n)

'''



class Arraylist:
    def __init__(self):
        self.exp=0
        self.maxsize=0
        self.lastindex=0
        self.array=[]
    def append(self,val):
        # check whether the array is full,
        if self.lastindex>self.maxsize-1:  # that means the array[n] can be gotten
            self.__resize()   # reassign the memory and get a bigger list
        self.array[self.lastindex]=val
        self.lastindex+=1

    def __resize(self):  # call the function just use the _classname__resize()
        newsize=2**self.exp   # use the exponent to get the size for each expansion
        newarray=[0]*newsize
        for i in range(self.maxsize):
            newarray[i]=self.array[i]   # copy the element in the old array to the new one

        self.maxsize=newsize
        self.array=newarray
        self.exp+=1
        # generally, the append operation is 1, while N when calling the __resize

    def __getitem__(self, item):
        if item <self.lastindex:  # not indexerror
            return self.array[item]
        else:
            raise IndexError('index out of bounds')
    def __setitem__(self, key, value):
        if key<self.lastindex:  # current last one but not the max_size since that the array can not full
            self.array[key]=value
        else:
            raise IndexError('index out of bounds')
    def insert(self,key,val):
        if self.lastindex>self.maxsize-1:
            self.__resize()
        for i in range(self.lastindex,key-1,-1): # from the last one to the insert location
            self.array[i+1]=self.array[i]  # the current one move only if after moving the next one
        self.lastindex+=1
        self.array[key]=val



''' review of recurrsion'''

#1. encrypt the password, just move the password for m index, and then use the new location to get the mingwen

def encrypt(m):
    s='abcdefghijklmnopqrstuvwxyz'
    res=''
    for i in m:
        # find would return -1 if not found while index will raise Error
        k=(s.find(i)+13)%26
        res+=s[k]
    return res

def decrypt(m,k):
    s='abcdefghijklmnopqrstuvwxyz'
    res=''
    for i in m:
        # find would return -1 if not found while index will raise Error
        pos=(s.find(i)+26-k)%26
        res+=s[pos]
    return res

def encrypt_k(m,k):
    s='abcdefghijklmnopqrstuvwxyz'
    res=''
    for i in m:
        # find would return -1 if not found while index will raise Error
        pos=(s.find(i)+k)%26
        res+=s[pos]
    return res
def modexp(x,n,p):
    if n==0:
        return 1
    t=(x * x) % p
    tmp=modexp(t,n//2,p)
    if n%2==0:
        tmp=(tmp * x) % p
    return tmp

# Euclidean's method to compute the gcd between a and b
def gcd(a,b):
    if b==0:
        return a
    elif a<b:
        return gcd(b,a)
    else:
        return gcd(a-b,b)


def gcd_beta(a,b):
    if b==0:
        return a
    else:
        return gcd_beta(b, a % b)


def ext_gcd(x,y):
    if y==0:
        return (x,1,0)
    else:
        (d, a, b) =ext_gcd(y, x % y)
        return (d, b, a - (x // y) * b)
if __name__=='__main__':
    print(encrypt('uryybjbeyq'))
    print(encrypt('helloworld'))
    s=encrypt_k('helloworld',11)
    print(decrypt(s,11))