class solution:
    def encode(self,arr):
        ip_str = ""
        for ele in arr:
            ip_str = ip_str + str(len(ele)) + "#" + ele
        return  ip_str
        
    def decode(self,str):
        tmp_array = []
        i=0
        while i < len(str):
            j=i
            while str[j]!= "#":
                j+=1
            length = int(str[i:j])
            tmp_array.append(str[j+1:j+1+length])
            i=j+1+length
        return tmp_array
                               

   
if __name__ == '__main__':
    obj = solution()
    encode = obj.encode(["neet","code","lihre"])
    print(encode)
    decode = obj.decode(encode)
    print(decode)