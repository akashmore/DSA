
class Node:
    def __init__(self,data,next,previous):
        self.data = data
        self.next = next
        self.previous = previous

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        str1 = ""
        itr = self.head
        while(itr is not None):
            str1+=str(itr.data) + "->"
            itr = itr.next
        print("straight",str1)

    def addElementAtStart(self,data):
        current_element = self.head        
        element = Node(data,current_element,None)
        if(self.head is not None):
            current_element.previous = element
        self.head = element

    def addElementAtEnd(self,data):
        itr = self.head
        while(itr.next is not None):
            itr = itr.next
        element = Node(data,None,itr)
        itr.next = element

    def deleteElementAtStart(self):
        ele = self.head
        self.head = self.head.next
        self.head.previous = None
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
        previous = None
        while(i!=index):
            i = i+1
            previous = itr
            itr = itr.next
        element = Node(value, itr,previous)
        previous.next = element
        itr.previous = element

    def deleteElementAtIndex(self,index):
        i = 1
        itr = self.head
        previous = None
        while(i!=index):
            i = i+1
            previous = itr
            itr = itr.next
        previous.next = itr.next
        itr.next.previous = previous
        del itr

    def reverseList(self):
        reverse_string = ""
        while(self.head.next is not None):
            self.head = self.head.next
        while(self.head is not None):
            reverse_string = reverse_string + str(self.head.data) + "->"
            self.head = self.head.previous
        print("reverse",reverse_string)

if __name__ == "__main__":
    list = LinkedList()
    list.addElementAtStart(5)
    list.addElementAtStart(6)
    list.addElementAtStart(7)
    list.addElementAtEnd(8)
    list.addElementAtEnd(9)
    list.deleteElementAtStart()
    list.deleteElementAtEnd()
    list.insertElement(2,10)
    list.deleteElementAtIndex(3)
    list.printList()
    list.reverseList()
    