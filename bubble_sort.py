def bubble_sort(a): #O(n)=n**2 把小数往前交换
    for i in range(0,len(a)):
        for j in range(len(a)-1,i,-1):
            if a[j]< a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
                

def bubbleSort(arr):
    n = len(arr)
    for i in range(n): 
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort2(A): #把大数往后交换
    for i in range(len(A)-1,0,-1):
        for j in range(0,i):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                
