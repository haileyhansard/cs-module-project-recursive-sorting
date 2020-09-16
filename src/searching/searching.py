# TO-DO: Implement a recursive implementation of binary search
# arr: the input array to search through
# target: the target we're searching for
# start: left-side index of the sub-array we're searching through
# end: right-side index of the sub-array we're searching through
def binary_search(arr, target, start, end):
    # Your code here
    #check base case
    #make sure to call the function in itself
    #each recursive call should bring us closer to reaching the base case(s)
    #it stops when we either find the target or start and end go past each other (i.e. we don't find the target)
    
    if start > end:  
    #first base case
    # if start becomes greater than end, we stop and the target isn't in the array
        return -1
    else:
        mid = (start + end) // 2

        if arr[mid] == target:  
        #this is our second base case
            return mid
        
        #otherwise, we need to move towards one of our base cases
        #arr doesn't change, just because we'll end updating start and end
        #target doesn't change between recursive calls
        #end changes if we toss out the right side of the array
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)

        #start changes if we toss out out the left side of the array 
        else:
            return binary_search(arr, target, mid + 1, end)



    # if end >= start:
    #     mid = (end + start) // 2
    #     #if element is present at the middle itself
    #     if arr[mid] == target:
    #         return mid       
    #     #if element is smaller than mid, then it can only be present in the left subarray
    #     elif arr[mid] > target:
    #         return binary_search(arr, start, mid - 1, target)
    #     #else, the element can only be present in right subarray
    #     else:
    #         return binary_search(arr, mid + 1, end, target)
    # else:
    #     #element is not present in the array
    #     return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

# def agnostic_binary_search(arr, target):
#     # Your code here
#     pass
