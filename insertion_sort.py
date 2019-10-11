def insertion_sort(A):   #right，O(n)=n**2
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            A[i] = key
            i = i-1


