def max_heapify(a,n,i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i],a[largest] = a[largest],a[i]
        max_heapify(a,n,largest)

def heap_sort(a):
    n = len(a)
    #build max_heap
    for i in range(n//2-1,-1,-1):
        max_heapify(a,n,i)
    for i in range(n-1,0,-1):
        a[i],a[0] = a[0],a[i]
        max_heapify(a,i,0)
