import random
def random_partiton(a,p,r):
    i = random.randint(p,r) #可以取到两边边界
    a[i],a[r] = a[r],a[i]
    i = p-1
    key = a[r]
    for j in range(p,r):
        if a[j] < key:
            i = i+1
            a[i],a[j] = a[j],a[i]
        a[i+1],a[r] = a[r],a[i+1]
    return i+1

def quick_sort(a,p,r): #nlgn
    if p < r:
        q = random_partiton(a,p,r)
        quick_sort(a,q+1,r)
        quick_sort(a,p,q-1)



