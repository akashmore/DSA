class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        first_dict = {}
        second_dict = {}
        for val in s:
            if val not in first_dict:
                first_dict[val] = 1
            else:
                first_dict[val]+=1
        for val in t:
            if val not in second_dict:
                second_dict[val] = 1
            else:
                second_dict[val]+=1
        for item in second_dict.keys():
            if item in first_dict and first_dict[item] == second_dict[item]:
                pass
            else:
                return item