class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        tmparray = []
        for i in range(1,n+1):
            if i%3 == 0  and i%5 == 0:
                tmparray.append("FizzBuzz")
            elif i%3 == 0:
                tmparray.append("Fizz")
            
            elif i%5 == 0:
                tmparray.append("Buzz")
            else:
                tmparray.append(str(i))
        return tmparray
        