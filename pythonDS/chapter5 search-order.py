# sequential search
def sequential_search(alist, item):
    found= False
    for i in alist:
        if i == item:
            found=True
            break

    return found


# binary search, prerequisite: ordered list
# non-recursive
def binary_search(alist,item):
    start=0
    end= len(alist)-1 # the last index
    found=False
    while start<end:
        mid=(start+end)//2
        if alist[mid]== item:
            found= True
            break
        elif alist[mid] >item:
            end=mid-1
        else:
            start=mid+1
    return found




# recursive
def binary_search_rec(alist,item):
    # don't forget the fundamental condition
    if len(alist) ==0:
        # when only last one element in the list,
        # the next recursive would be 0, 1//2=0
        return False

    else:
        mid=len(alist)//2
        if alist[mid]==item:
            return True
        elif alist[mid] >item:
            # don't forget the return statement
            return binary_search_rec(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:],item)


def hash_words(word, size):
    sum=0
    for k,v in enumerate(word):
        sum+=ord(v)%size
        # if mutiple the position weights to avoid the issue that
        # two words that have same char but different order
        # sum+= k* ord(v)
    return size

'''
implement the dict() from scatch,
the original hash function is using the key % the hash table size
and the rehash function is the original hashvalue +1 % hash tabel size

'''

class Hashtable:
    def __init__(self,size):
        self.size=size
        self.slots=[None]*self.size
        self.data= self.size *[None]

    def put(self,key,data):
        hashvalue= self.hashfunc(key)
        print(hashvalue)
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        elif self.slots[hashvalue]==key:
            self.data[hashvalue]=data
        else:
            nextvalue= self.rehash(hashvalue)
            # print(nextvalue)
            while self.slots[nextvalue] != None and self.slots[nextvalue] !=key:
                nextvalue=self.rehash(nextvalue)
            if self.slots[nextvalue]==None:
                self.slots[nextvalue]=key
                self.data[nextvalue]=data
            else:self.data[nextvalue]=data

    def hashfunc(self,key):
        return key%self.size

    def rehash(self,value):
        # notice here is not use the old value get the new value directly, that will not change the value, add 1
        return (value+1)%self.size
    def get(self,key):
        data=None # default return value
        stop=False
        # found=False
        hashvalue=self.hashfunc(key)
        startposition=hashvalue
        while self.slots[hashvalue] != None and not stop:
            if self.slots[hashvalue]!= key:    # notice, even if the current slot is not none, if might be taken up by the other value
                data= self.data[hashvalue]
                break
                # found=True
            else:
                nextvalue= self.rehash(hashvalue)
                if nextvalue == startposition:
                    stop=True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key,value)
if __name__=='__main__':
    # testlist = [0, 1 ]
    # print(binary_search_rec(testlist, 0))
    # print(binary_search_rec(testlist, 13))
    # print(1//2)

    H = Hashtable(11)
    H[54] = 'cat'
    H[26] = 'DOG'
    H[93] = 'LION'
    H[17] = 'TIGER'
    H[77] = 'BIRD'
    H[31] = 'COW'
    H[44] = 'GOAT'
    H[55] = 'PIG'
    H[20] = 'CHICKEN'
    print(H.slots)
    print(H.data)
    H[20]
    H[17]
    H[20] = 'DUCK'
    print(H[20])
    print(H.data)
    # print(sequential_search([1,2,5,7,9],2))