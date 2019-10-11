def counting_sort(a,k): #a中元素大小[0,k)
    b = [0]*len(a)
    c = [0]*k
    for i in range(len(a)):
        c[a[i]] = c[a[i]] + 1
    for j in range(1,k):
        c[j] = c[j] + c[j-1]
    for i in range(len(a)-1,-1,-1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] = c[a[i]] - 1
    return b
    
