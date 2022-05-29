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
the slot can be  1) open  2) there exits the same key but old value 3) has been taken by other key
so that, get the second hashvalue by hashvalue +1 and mod the size of hashtable 
'''

class Hashtable:
    def __init__(self,size):
        self.size=size
        # build two lists to store the key and value
        self.slots=[None]*self.size
        self.data= self.size *[None]

    def put(self,key,data):
        hashvalue= self.hashfunc(key)# get the initial hashvalue
        # print(hashvalue)
        if self.slots[hashvalue]==None:  # if the slot not be taken, set the key-value pair
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        elif self.slots[hashvalue]==key:    # if there exists an old value for that key, update the data
            self.data[hashvalue]=data
        else:  # if there is no key in the slots and the initial slot has been taken
            nextvalue= self.rehash(hashvalue)  # get the second hash value, remember get the second hash value first
            # print(nextvalue)
            # one justify, whether the second value meet the requirement; until the slot meet the requirement
            while self.slots[nextvalue] != None and self.slots[nextvalue] !=key:
                nextvalue=self.rehash(nextvalue)

            # meet the requirement  two situations:  1) the slot is open   2) there exists the old value for the key.
            if self.slots[nextvalue]==None:
                self.slots[nextvalue]=key
                self.data[nextvalue]=data
            else:self.data[nextvalue]=data

    def hashfunc(self,key):
        return key%self.size

    def rehash(self,value):
        # notice here is not use the old value get the new value directly, that will not change the value, add 1
        return (value+1) % self.size
    def get(self,key):
        data=None # default return value, remember it has to be a return value.
        stop=False
        found=False
        startslot=self.hashfunc(key)
        position=startslot   # important, justify that the hashvalue has returned to the initial hashvalue
        # , stop the loop
        while self.slots[position] is not None and not stop:  # because it's search, so it has to be equivalent to the key,
            # # rather than open, notice the loop variable should be the same,  !false: hashvalue, nextvalue
            # print(position)
            if self.slots[position]== key:    # notice, even if the current slot is not none, if might be taken up by the other value
                data= self.data[position]
                break
                # found=True
            else: # if not key, continue getting the second hashvalue

                position= self.rehash(position)
                # print(nextvalue)
                if position== startslot:  # if the hashvalue = initial hashvalue, it means has one round, stop the loop
                    stop=True
        #     '''
        #     the other implementation for the loop
        #     '''
        # while self.slots[position] != key:
        #     if self.slots[position] == startslot:
        #         break
        #     position=self.rehash(position)
        # # the loop ended, either get the initial key, or not found in the end,
        # # if get the key, update the data from none to the value
        # if self.slots[position]== key:
        #     data= self.data[position]

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key,value)


# class Hashtable:
#     def __init__(self, size):
#         self.size = size
#         self.slots = self.size * [None]
#         self.data = self.size * [None]


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
    print(H[20])
    print(H[17])
    H[20] = 'DUCK'
    print(H[20])
    # print(H.data)
    # print(sequential_search([1,2,5,7,9],2))