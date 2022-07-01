a = [1,2,3,4,5]
b = [1,2,3]
# for ele in a:
#     if ele not in c: 
#         c.append(ele)
# for ele2 in b:
#     if ele2 not in c:
#         c.append(ele2)
# print(len(c))
# c = set(a).update(set(b))
# print(c)
print(set(a).union(set(b)))