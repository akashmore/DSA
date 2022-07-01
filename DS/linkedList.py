
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        str1 = ""
        itr = self.head 
        while(itr is not None):
            str1+=str(itr.data) + "->"
            itr = itr.next
        print(str1)
    def addElementAtStart(self,data):
        element = Node(data,self.head)
        self.head = element

    def addElementAtEnd(self,data):
        itr = self.head
        while(itr.next is not None):
            itr = itr.next
        element = Node(data,None)
        itr.next = element

    def deleteElementAtStart(self):
        ele = self.head
        self.head = self.head.next
        del ele

    def deleteElementAtEnd(self):
        itr = self.head
        while(itr.next.next is not None):
            itr = itr.next
        ele = itr.next
        itr.next = None
        del ele

    def insertElement(self,index,value):
        i = 1
        itr = self.head
        previous_head = None
        while(i!=index):
            i = i+1
            previous_head = itr
            itr = itr.next
        element = Node(value, itr)
        previous_head.next = element

    def deleteElementAtIndex(self,index):
        i = 1
        itr = self.head
        previous_head = None
        while(i!=index):
            i = i+1
            previous_head = itr
            itr = itr.next
        previous_head.next = itr.next
        del itr
    
    def reversList(self):
        first = self.head
        second = first.next
        while(second):
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None    
        self.head = first



if __name__ == "__main__":
    list = LinkedList()
    list.addElementAtStart(5)
    list.addElementAtStart(6)
    list.addElementAtStart(7)
    list.addElementAtEnd(8)
    list.addElementAtEnd(9)
    # list.deleteElementAtStart()
    # list.deleteElementAtEnd()
    list.insertElement(2,10)
    # list.deleteElementAtIndex(3)
    list.printList()
    list.reversList()
    list.printList()