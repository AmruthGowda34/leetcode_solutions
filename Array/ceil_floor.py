n=[3,4,4,4,8,9,9,10,12,12,14,15]
low=0
tar=7
high=len(n)-1
floor=-1
ceil=-1
while low<=high:
    mid=(low+high)//2
    if n[mid]==tar:
        floor=n[mid]
        ceil=n[mid]
        break
    elif n[mid]>tar:
        ceil=n[mid]
        high=mid-1
    else:
        floor=n[mid]
        low=mid+1
print(floor,ceil)

#ceil = Finding smallest element in array > target value
#floor = Finding largest element in array < target value   