#Its sliding window problem by amintaining two pointers and calaculating number of times the less frequently character occures. formula is len(substring) - less frequent char <= k.
class solution:
    def solve(self,s):
      str1 = ""
      for ele in s:
            if ele.isalnum():
                  str1+=ele.lower()
      return str1==str1[::-1]
                       

   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve("0P")
    print(result)