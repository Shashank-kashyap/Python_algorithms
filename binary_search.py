
#num has to be sorted list
#N is the item u want to search in the list nums
def b_search(num,N):
    l=0
    u=len(num)-1
    while(l<=u):
        mid=(l+u)//2
        if(num[mid]==N):
            print(mid)
            break
        else:
            if(num[mid]>N):
                u=(mid-1)
            else:
                l=(mid+1)
    return -1
b_search()
