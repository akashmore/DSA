#stack can be implemented using both array and linked list, below is linked list implementation
class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def pushEle(self,value):
        ele = Node(value,self.head)
        self.head = ele
        self.size += 1
    
    def popEle(self):
        if(self.head is None):
            print("Stack is empty")
        else:
            delElement = self.head
            self.head = self.head.next
            self.size -= 1
            del delElement
    
    def printElement(self):
        itr = self.head
        string = ""
        while(itr):
            string += str(itr.value) + "->"
            itr = itr.next
        print(string)
    
    def getSize(self):
        print(self.size)
    
    def peek(self):
        if(self.head is None):
            print("Empty stack")
        else:
            print(self.head.value)

if __name__ == "__main__":
    stack = Stack()
    stack.pushEle(10)
    stack.pushEle(20)
    stack.pushEle(30)
    stack.pushEle(40)
    stack.popEle()
    # stack.popEle()
    # stack.popEle()
    stack.peek()
    stack.getSize()
    stack.printElement()
