def merge(A,p,q,r):
    L = [A[p+i] for i in range(q-p+1)]
    L.append(9999999999)
    R = [A[q+1+j] for j in range(r-q)]
    R.append(9999999999) #防止后面循环时下标溢出
    i = 0
    j = 0
    for k in range(p,r+1):
        if i < q-p+1 and L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        elif j < r-q and L[i] > R[j]:
            A[k] = R[j]
            j = j+1

def merge_sort(a,p,r): #nlgn,  T(n)=2T(n/2)+n
    if p < r:
        q = (p+r) // 2
        merge_sort(a,p,q) #分治法
        merge_sort(a,q+1,r)
        merge(a,p,q,r)
