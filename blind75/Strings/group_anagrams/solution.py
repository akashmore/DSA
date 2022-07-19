from collections import defaultdict


class solution:
    def solve(self,strs):
        temp = defaultdict(list)
        for word in strs:
            tmp = [0 for i in range(0,26)]
            for ele in word:
                tmp[ord(ele)-ord("a")]+=1
            temp[tuple(tmp)].append(word)
        return temp.values()
                       

   
if __name__ == '__main__':
    obj = solution()
    result = obj.solve(["eat","tea","tan","ate","nat","bat"])
    print(result)