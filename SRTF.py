class Node:
    def __init__(self,n1,ar1,va1,n2):
        self.name=n1
        self.arrivalTime=ar1
        self.burstTime=va1
        self.next=n2
    def __init__(self,n1,ar1,va1):
        self.name=n1
        self.arrivalTime=ar1
        self.burstTime=va1
        self.next=0
    def getName(self):
        return self.name
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
        return False
    def delNode(self,v):
        if self.head!=0:
            if self.head.name==v and self.head.next==0:
                self.head=self.tail=0
            else:
                burstTimeiable=self.head
                if burstTimeiable.name==v:
                    self.head=self.head.next
                else:
                    while burstTimeiable.next!=0:
                        if burstTimeiable.next.name==v:
                            burstTimeiable.next=burstTimeiable.next.next
                            break
                        burstTimeiable=burstTimeiable.next
    def getSmallest(self):
        if self.head!=0:
            v = self.head
            node = self.head
            while True:
                if node == 0:
                    return v
                if int(node.burstTime) < int(v.burstTime):
                    v = node
                node = node.next
    def setAllSmall(self,readyQueue,v):
        v1=self.head
        while v1!=0:
            if int(v1.arrivalTime)<=v:
                readyQueue.addAtTail(v1.name,v1.arrivalTime,v1.burstTime)
                self.delNode(v1.name)
            v1=v1.next
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
    def smaller(self,v):
        if self.head!=0:
            v1=self.head
            while v1!=0:
                if int(v1.burstTime)<v:
                    return True
                v1=v1.next
        return False
file=open("File1.txt","r")
newQueue=Queue()
for element in file:
    data=element.split()
    print(data)
    newQueue.addAtTail(data[0],data[1],data[2])
print('|')
flag=False
value=0
readyQueue=Queue()
node = newQueue.getEarliest()
v1=int(node.arrivalTime)
if newQueue.empty()==False:
    newQueue.setAllSmall(readyQueue,v1)
while readyQueue.empty()!=True or newQueue.empty()!=True:
    if readyQueue.empty()==True:
        node=newQueue.getEarliest()
        newQueue.setAllSmall(readyQueue,int(node.arrivalTime))
    node1=readyQueue.getSmallest()
    a=node1.name
    b=int(node1.arrivalTime)
    while value<b:
        print('.')
        value+=1
        flag=True
    if flag==True:
        print('|',a)
        flag=False
    c=int(node1.burstTime)
    while c>0:
        if newQueue.empty()!=True:
            newQueue.setAllSmall(readyQueue,value)
            if readyQueue.smaller(c)==True:
                print('|',a)
                readyQueue.addAtTail(a,b,c)
                node1=readyQueue.getSmallest()
                readyQueue.delNode(a)
                a=node1.name
                b=int(node1.arrivalTime)
                c=int(node1.burstTime)
                readyQueue.printQueue()
        print('-')
        c-=1
        value+=1
    print('|',a)
    readyQueue.delNode(a)
    readyQueue.printQueue()
    print('2')
    newQueue.printQueue()
    if newQueue.empty() == False:
        newQueue.setAllSmall(readyQueue, value)
print(value)