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


if __name__=='__main__':
    testlist = [0, 1 ]
    print(binary_search_rec(testlist, 0))
    print(binary_search_rec(testlist, 13))
    print(1//2)
    # print(sequential_search([1,2,5,7,9],2))