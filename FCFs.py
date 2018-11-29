class Node:
    def __init__(self,n1,ar1,va1,n2):
        self.name=n1
        self.arrivalTime=ar1
        self.burstTime1=va1
        self.next=n2
    def __init__(self,n1,ar1,va1):
        self.name=n1
        self.arrivalTime=ar1
        self.burstTime=va1
        self.next=0
class Queue:
    def __init__(self):
        self.head=self.tail=0
    def addAtTail(self,v,n,n1):
        if self.head==0:
            self.head=self.tail=Node(v,n,n1)
        else:
            a=Node(v,n,n1)
            self.tail.next=a
            self.tail=self.tail.next
    def removeFromHead(self):
        if self.head==0:
            return False
        self.head=self.head.next
        return True
    def printQueue(self):
        burstTimeiable=self.head
        while burstTimeiable!=0:
            print(burstTimeiable.arrivalTime)
            burstTimeiable=burstTimeiable.next
    def empty(self):
        if self.head==0:
            return True
    def delNode(self,v):
        if self.head!=0:
            burstTimeiable=self.head
            if burstTimeiable.name==v:
                self.head=self.head.next
            else:
                while burstTimeiable.next!=0:
                    if burstTimeiable.next.name==v:
                        burstTimeiable.next=burstTimeiable.next.next
                        break
                    burstTimeiable=burstTimeiable.next
    def getName(self):
        return self.head.name
    def getAValue(self):
        return self.head.arrivalTime
    def getValue(self):
        return self.head.burstTime
    def getEarliest(self):
        v=self.head
        node=self.head
        while True:
            if node==0:
                return v
            if int(node.arrivalTime)<int(v.arrivalTime):
                v=node
            node=node.next
file=open("File1.txt","r")
newQueue=Queue()
for element in file:
    data=element.split()
    print(data)
    newQueue.addAtTail(data[0],data[1],data[2])
newQueue.printQueue()
print('|')
value=0
while newQueue.empty()!=True:
    node=newQueue.getEarliest()
    a=node.name
    print(a)
    b=int(node.arrivalTime)
    while value<b:
        print('.')
        value+=1
    print('|')
    b=int(node.burstTime)
    value+=b
    for i in range(b):
        print('-')
    print("|",a)
    newQueue.delNode(a)
    newQueue.printQueue()
print(value)