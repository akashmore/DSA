a = [1,2,3,4,5]
maximum,minimum = a[0],a[0]
for ele in a:
    if ele > maximum:
        maximum = ele
    elif ele < maximum:
        minimum = ele
print(maximum,minimum)