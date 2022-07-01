#Find minimum of list replace with the first element of list and procedd same for n length

a = [1,10,2,3,8,4,7,9,5,6]
for i in range(0,len(a)):
    small = a[i]
    for j in range(i+1,len(a)):
        if(a[j]<small):
            small = a[j]
    tmp = a[i]
    a[a.index(small)] = tmp
    a[i] = small    
print(a)

