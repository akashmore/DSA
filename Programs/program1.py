class A:
    def __init__(self,a_val):
        self.a = a_val
    
class B(A):
    def __init__(self,b_val,a_val):
        self.b = b_val
        A.__init__(self,a_val)
        
class C(B):
    def __init__(self,c_val,b_val,a_val):
        self.c = c_val
        B.__init__(self,b_val,a_val)

    def printStatement(self):
        print(self.a + " " + self.b + " " + self.c)

if __name__ == "__main__":
    varible = C("akash","zakas","bakas")
    varible.printStatement()