# a,b=0,1
# for i in range(10):
#     print(a)
#     tmp = a+b
#     a=b
#     b=tmp    

def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n-1)
print(calculate_factorial(5))     