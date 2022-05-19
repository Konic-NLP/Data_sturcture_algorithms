# chapter4  recursion
'''
three elements: 1) halt condition  2) reduce the problem into a smaller one 3) call itself

'''

#add
def add(nums):
    if len(nums)==1:
        return nums[0]
    else:
        return nums[0]+add(nums[1:])

# def convert(num,base)