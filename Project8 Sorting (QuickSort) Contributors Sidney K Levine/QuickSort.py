#MODULE FILE

#Low to High Sort
#Start pivot bias

#Quick sort use starting position as pivot *low to high
def O_Partitioning(P_List, Start, End):
    #Partitioning works with 3 variables or more
    #Start with the Variables
    #pivot is the pivot point
    pivot = Start

    #i is the incrementer
    i = Start

    #j is the decrementer
    j = End
    
    while i <= j:
        #I is greater than pivot
        if(P_List[i] > P_List[pivot]):
            #J has to be less than pivot, therfore less than I
            if(P_List[j] < P_List[pivot]):
                P_List[j], P_List[i] = P_List[i] , P_List[j]
            else:
                j -= 1
        else:
            i += 1
    #Final swap
    P_List[j], P_List[pivot] = P_List[pivot], P_List[j]
    return j
            
#QuickSort Method from Low to High
def QuickSort(P_Li, Low, High):
    #If our passed through high and low functions is 1 element return none
    if((High - Low) < 1):
        return
    #Special case: If there are 2 elements passed through then compare them once and see if they are in the correct position
    elif((High-Low) == 1):
        if(P_Li[Low] > P_Li[High]):
            P_Li[Low], P_Li[High] = P_Li[High], P_Li[Low]
        return
    #Continue partitioning
    else:
        #Partition
        part_point = O_Partitioning(P_Li, Low, High)

        #Left Partition
        QuickSort(P_Li, Low, part_point-1)

        #Right partition
        QuickSort(P_Li,part_point+1, High)


#New partition function
def parti2(para_Li, Start, End):
    #Our pivot point is the low entry
    piv = para_Li[End]
    #incrementer
    i = Start

    #For loop
    for j in range(i - 1 , End):
        #If we found j to be less than pivot then swap
        if(para_Li[j] < piv):
            i += 1
            para_Li[i], para_Li[j] = para_Li[j], para_Li[i]
    para_Li[i + 1], para_Li[End] = para_Li[End], para_Li[i+1]
    return i + 1

#CSDojo QS
def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

#CSDojo QS
def qs(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r)

    qs(arr, l, p - 1)
    qs(arr, p + 1, r)

#CSDojo QS
def quicksort(arr):
    qs(arr, 0, len(arr) - 1)
