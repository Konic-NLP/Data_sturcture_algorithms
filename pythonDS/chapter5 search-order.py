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





'''
bubble sort??? n-1 round, each round will iterate the number of comparison in the last round -1 
the first round: compare n-1 times. since only if n-1 has been comparison, the last one can be known ordered

time complexity: O(N^2)

'''
def bubble_sort2(L):
    '''????????????????????????????????????????????????????????????????????????'''
    n=len(L)
    for i in range(n-1):
        for j in range(n-1-i):
            if L[i]>L[i+1]:
                L[i],L[i+1]=L[i+1],L[i]
    return L


def bubble_sort(alist):
    for compare in range(len(alist)-1,0,-1):  # first round:n-1, second round: n-2, ........
        print('outer loop '+str(compare))
        for num in range(compare):
            # the maximum index would be less than 1 of elements in the round to avoid the out of index
            print(num)
            if alist[num]> alist[num+1]:
                # each element in the alist must compare with the next element until the next to last element
                alist[num],alist[num+1]= alist[num+1], alist[num]

    print(alist)

    
    
def short_bubble_sort(alist):
    round= len(alist)-1
    stop = False
    # while round >0 and not stop:
    for compare in range(len(alist)-1,0,-1):  # first round:n-1, second round: n-2, ........
        # print('outer loop '+str(compare))
    # first round:n-1, second round: n-2, ........

        stop = True # presupposed each round set there no need to compare anymore, and terminate the outer loop
        for num in range(compare):
            # the maximum index would be less than 1 of elements in the round to avoid the out of index
            print(num)
            if alist[num]> alist[num+1]:
                # each element in the alist must compare with the next element until the next to last element
                alist[num],alist[num+1]= alist[num+1], alist[num]
                stop = False # once exchange happens, it means that we need comparison
        round-=1

    print(alist)
  
    

'''
optimzied bubble sort, instead of comparing between the current one and the next one\
, it just select the maximum one, and exchange this one with the last one, and compare n-1 rounds

O(N^2)
'''
def selection_sort(alist):
    for compare in range(len(alist)-1,0,-1):  # first round:n-1, second round: n-2, ........
        print('outer loop '+str(compare))
        maxnum=compare
        for num in range(compare):  # get from the first to the next to last element, and compare with the last one.
            # the maximum index would be less than 1 of elements in the round to avoid the out of index
            print(num)
            if alist[num]> alist[maxnum]:
                maxnum=num
        alist[compare],alist[maxnum]=alist[maxnum], alist[compare]
#         maxvalue=0   # get from the second one to the last one, and compare with the first one at the begining. 
#         for num in range(1, compare+1):   # can start from the second element and compare with the first one at the begining
#             if alist[num]>alist[maxvalue]:
#                 maxvalue = num
#         alist[maxvalue], alist[compare] = alist[compare], alist[maxvalue]  # exchange the maxindex with the last element within the current round.
    print(alist)


# another implementation

def select_sort(arr):
    for i in range(len(arr) - 1):
        remain = arr[i + 1:len(arr)]
        count = i + remain.index(min(remain)) + 1
        if arr[count] < arr[i]:
            arr[i], arr[count] = arr[count], arr[i]

    return arr



'''
insert sort,
any elements before the current that wait for sorting is ordered, the elements just iterate all the elements,
if the current element is less than the compared element, then swap the element, else, the current position is the 
current elemnt should be 
'''

def insert_sort(arr):
   '''????????????'''
   for i in range(1, len(arr)):
       current = arr[i]  # ???????????????????????????
       pre = i - 1  # ?????????????????????????????????
       while pre >= 0 and arr[pre] > current:
           arr[pre + 1], arr[pre] = arr[pre], arr[pre + 1]  # ????????????????????????????????????????????????????????????
           pre -= 1
   return arr


def insert_sort2(arr):
    pass



def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])

    return merge(left,right)
'''
shell sort, the optimized edition of the insert sort, first, split the elements into several subgroup based on the step
then execute the insert sort within each sub group, and in the end, just execute one round insert sort.
Since some elements has been ordered within the subgroup, so the overall efficient is better than the insert sort
'''
def shell_sort(arr):
    '''????????????'''
    gap=len(arr)//2  #??????????????????????????????
    while gap>0:
        for i in range(gap,len(arr)):  #???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
            while i-gap>=0 and arr[i]<arr[i-gap]:
                arr[i],arr[i-gap]=arr[i-gap],arr[i]
                i-=gap
        gap//=2 #?????????????????????
    return arr


'''
quick sort,
just select one element as the base, all the element that less than the base would be on the left and all element greater
than the element on the right, and rucursive  
'''
def quicksort(arr):
   if len(arr)<2:  #????????????0?????????1??????????????????
       return arr
   else:
       st=arr[0]
       smaller=[i for i  in arr[1:] if  i < st]#???????????????????????????????????????????????????????????????????????????????????????????????????????????????
       bigger=[i for i in arr[1:]if i > st]
       return quicksort(smaller) +[st]+quicksort(bigger)  #???????????????????????????

if __name__=='__main__':
    selection_sort([1,5,2,3,3,9,7])
    # testlist = [0, 1 ]
    # print(binary_search_rec(testlist, 0))
    # print(binary_search_rec(testlist, 13))
    # print(1//2)

    # H = Hashtable(11)
    # H[54] = 'cat'
    # H[26] = 'DOG'
    # H[93] = 'LION'
    # H[17] = 'TIGER'
    # H[77] = 'BIRD'
    # H[31] = 'COW'
    # H[44] = 'GOAT'
    # H[55] = 'PIG'
    # H[20] = 'CHICKEN'
    # print(H.slots)
    # print(H.data)
    # print(H[20])
    # print(H[17])
    # H[20] = 'DUCK'
    # print(H[20])
    # print(H.data)
    # print(sequential_search([1,2,5,7,9],2))
