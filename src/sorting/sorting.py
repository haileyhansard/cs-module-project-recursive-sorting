# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    #merge function is used for merging two halves
    elements = len(arrA) + len(arrB)
    #pre-allocating our output array with the number of elements we know it will hold at the end
    merged_arr = [0] * elements

    # Your code here
    a = 0
    b = 0

    for i in range(elements):
        #check if a is in bounds of arrA
        if a >= len(arrA):
            #we've moved all elements from arrA into merged_arr already
            #we still have elements from arrB that need to be moved
            merged_arr[i] = arrB[b]
            b += 1
        #check if b is in bounds of arrB
        elif b >= len(arrB):
            #we've moved all the elements from arrB into merged_arr
            #we still have elements from arrA that need to be moved
            merged_arr[i] = arrA[a]
            a += 1
        #compare arrA[a] against arrB[b]
        elif arrA[a] < arrB[b]:
            #move the smaller element into the merged_arr
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    
    return merged_arr


    # if arrA[a] <= arrB[b]:
    #     output.append(arrA[a])
    #     a += 1
    # else:
    #     output.append(arrB[b])
    #     b += 1

    #return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        L = merge_sort(arr[0 : len(arr) // 2])
        R = merge_sort(arr[len(arr) // 2:])
        #mid = len(arr)//2 #finding the mid of the array by dividing it in half
        #L = arr[:mid] #left is equal to the first index to the mid point. could also do arr[:mid]
        #R = arr[mid:] #right is equal to the mid point through the rest of the array to end. could also do arr[mid:]

        #merge_sort(L) #sort the first half
        #merge_sort(R) #sort the second half
        arr = merge(L, R)

        # i = j = k = 0

        # while i < len(L) and j <len(R):
        #     if L[i] < R[j]:
        #         arr[k] = L[i]
        #         i += 1
        #     else:
        #         arr[k] = R[j]
        #         j += 1
        #     k += 1

        # while i < len(L):
        #     arr[k] = L[i]
        #     i += 1
        #     k += 1

        # while j < len(R):
        #     arr[k] = R[j]
        #     j += 1
        #     k += 1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input

# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

