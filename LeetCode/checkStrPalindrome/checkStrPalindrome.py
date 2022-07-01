def do(self, s):
        tmpArray = []
        for ele in s:
            if ele.isalnum():
                tmpArray.append(ele.lower() if ele.isalpha() else ele)
        str1="".join(tmpArray)
        if str1 == str1[::-1]:
            return True
        else:
            return False