#queue can be implemented using both array and linked list, below is linked list implementation but using array for queue is costly

import queue


class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next
class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def enque(self,value):
        ele = Node(value,self.head)
        self.head = ele
        self.size += 1
    
    def deque(self):
        if(self.head is None):
            print("Queue is empty")
        else:
            itr = self.head
            while(itr.next):
                previous = itr
                itr = itr.next
            ele = itr
            previous.next = None
            self.size -= 1
            del ele
    
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
            print("Queue is empty")
        else:
            print(self.head.value)

if __name__ == "__main__":
    que = Queue()
    que.enque(10)
    que.enque(20)
    # que.enque(30)
    # que.enque(40)
    que.deque()
    # que.deque()
    # que.deque()
    que.peek()
    que.getSize()
    que.printElement()
