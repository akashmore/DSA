#Its sliding window problem by amintaining two pointers and calaculating number of times the less frequently character occures. formula is len(substring) - less frequent char <= k.
class solution:
    def solve(self,s,k):
      if len(s)!=len(t):
            return False
      for i in range(0,len(k)):
        if k[i] in s and s.count(k[i]) == k.count(k[i]):
              pass
        else:
            return False
      return True
                       

   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve("anagram","nagaram")
    print(result)