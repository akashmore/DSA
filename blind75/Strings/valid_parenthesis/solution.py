#Its sliding window problem by amintaining two pointers and calaculating number of times the less frequently character occures. formula is len(substring) - less frequent char <= k.
class solution:
    def solve(self,s):
      tmp_array = []
      mapping = {")":"(","}":"{","]":"["}
      for ele in s:
            if ele in mapping.values():
                  tmp_array.append(ele)
            else:
                  if ele in mapping.keys() and len(tmp_array)!=0:
                        value = tmp_array[-1]
                        if value == mapping[ele]:
                              tmp_array.pop()
                        else:
                              tmp_array.append(ele)
                  else:
                        tmp_array.append(ele)
      if len(tmp_array) == 0:
            return True
      else:
            return False
   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve("]")
    print(result)