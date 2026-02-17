n=[1,1,1,2,3,3,5,6,6,6,7,9,12,12,13]
tar=6
low=0
lower_bound=len(n)
high=len(n)-1
while low<=high:
    mid=(low+high)//2
    if n[mid]>=tar:
        lower_bound=mid
        high=mid-1
    else:
        low=mid+1
print(lower_bound)


#lower_bound:-Smallest index shuch that n[mid]>=tar value is called lower_bound