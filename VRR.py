class Node:
    def __init__(self,n1,ar1,va1,n2,n3,n4):
        self.name=n1
        self.arrivalTime=ar1
        self.burstTime=va1
        self.quantum=n2
        self.IO_Time=n3
        self.next=n4
    def __init__(self,n1,ar1,va1,n2,n3):
        self.name=n1
        self.arrivalTime=ar1
        self.burstTime=va1
        self.quantum=n2
        self.IO_Time=n3
        self.next=0
    def getName(self):
        return self.name
class Queue:
    def __init__(self):
        self.head=self.tail=0
    def getHead(self):
        if self.head!=0:
            return self.head
    def addAtTail(self,v,n,n1,n2,n3):
        if self.head==0:
            self.head=self.tail=Node(v,n,n1,n2,n3)
        else:
            a=Node(v,n,n1,n2,n3)
            self.tail.next=a
            self.tail=self.tail.next
    def removeFromHead(self):
        if self.head==0:
            return False
        self.head=self.head.next
        return True
    def printQueue(self):
        variable=self.head
        while variable!=0:
            print(variable.name,'    ',variable.arrivalTime,'    ',variable.burstTime)
            variable=variable.next
    def empty(self):
        if self.head==0:
            return True
        return False
    def delNode(self,v):
        if self.head!=0:
            if self.head.name==v and self.head.next==0:
                self.head=self.tail=0
            else:
                variable=self.head
                if variable.name==v:
                    self.head=self.head.next
                else:
                    while variable.next!=0:
                        if variable.next.name==v:
                            variable.next=variable.next.next
                            break
                        variable=variable.next
    def getSmallest(self):
        if self.head!=0:
            var = self.head
            node = self.head
            while True:
                if node == 0:
                    return var
                if int(node.burstTime) < int(var.burstTime):
                    var = node
                node = node.next
    def setAllSmall(self,c2,v):
        v1=self.head
        while v1!=0:
            if int(v1.arrivalTime)<=v:
                c2.addAtTail(v1.name,v1.arrivalTime,v1.burstTime,v1.quantum,v1.IO_Time)
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
file=open("File2.txt","r")
arr=file.readline()
arr1=arr.split()
newQueue=Queue()
readyQueue=Queue()
waitingQueue=Queue()
auxillaryQueue=Queue()
for element in file:
    data=element.split()
    print(data)
    newQueue.addAtTail(data[0],data[1],data[2],arr1[0],arr1[1])
value=0
print('|',value)
flag=False
flag1=False
node = newQueue.getEarliest()
v1=int(node.arrivalTime)
if newQueue.empty()==False:
    newQueue.setAllSmall(readyQueue,v1)
while readyQueue.empty()!=True or newQueue.empty()!=True or waitingQueue.empty()!=True:
    if readyQueue.empty()==True:
        if newQueue.empty()==True:
            node=waitingQueue.getEarliest()
            waitingQueue.setAllSmall(readyQueue,int(node.arrivalTime))
        else:
            node=newQueue.getEarliest()
            newQueue.setAllSmall(readyQueue,int(node.arrivalTime))
    node1=readyQueue.getHead()
    a=node1.name
    b=int(node1.arrivalTime)
    c=int(node1.burstTime)
    e=int(node1.quantum)
    f=int(node1.IO_Time)
    while value<b:
        print('.',value)
        value+=1
        flag=True
    if flag==True:
        print('|',a,value,'  ',1)
        flag=False
    while c>0:
        if newQueue.empty()!=True:
            newQueue.setAllSmall(readyQueue,value)
        if waitingQueue.empty()!=True:
            waitingQueue.setAllSmall(auxillaryQueue,value)
        if f<=0:
            print('|',a,value,'  ',2)
            if e<=0:
                waitingQueue.addAtTail(a,value+int(arr1[1]),c,arr1[0],arr1[1])
            else:
                waitingQueue.addAtTail(a,value+int(arr1[1]),c,e,arr1[1])
            readyQueue.removeFromHead()
            while auxillaryQueue.empty()==False:
                node1=auxillaryQueue.getHead()
                a=node1.name
                b = int(node1.arrivalTime)
                c = int(node1.burstTime)
                e = int(node1.quantum)
                f = int(node1.IO_Time)
                while e>0:
                    print('-',value)
                    c-=1
                    e-=1
                    f-=1
                    value+=1
                    if c<=0:
                        print('|',a,value,'  ',3)
                        auxillaryQueue.removeFromHead()
                        break
                    elif f<=0:
                        print('|',a,value,'  ',4)
                        auxillaryQueue.removeFromHead()
                        if e>0:
                            waitingQueue.addAtTail(a,value+int(arr1[1]),c,e,arr1[1])
                        else:
                            waitingQueue.addAtTail(a,value+int(arr1[1]),c,arr1[0],arr1[1])
                            flag1=True
                        break
                if c>0 and e<=0 and f>0:
                    print('|',a,value,'  ',5)
                    auxillaryQueue.removeFromHead()
                    readyQueue.addAtTail(a,value,c,arr1[0],f)
                    flag1=False
            if readyQueue.empty()==False:
                node1=readyQueue.getHead()
                a=node1.name
                b=int(node1.arrivalTime)
                c=int(node1.burstTime)
                e=int(node1.quantum)
                f=int(node1.IO_Time)
            else:
                break
        if e<=0:
            break
        print('-',value)
        c-=1
        e-=1
        f-=1
        value+=1
    print('|',a,value,'  ',6)
    if newQueue.empty()!=True:
        newQueue.setAllSmall(readyQueue,value)
    if waitingQueue.empty()!=True:
        waitingQueue.setAllSmall(auxillaryQueue,value)
    if c<=0:
        readyQueue.removeFromHead()
        while auxillaryQueue.empty() == False:
            node1 = auxillaryQueue.getHead()
            a = node1.name
            b = int(node1.arrivalTime)
            c = int(node1.burstTime)
            e = int(node1.quantum)
            f = int(node1.IO_Time)
            while e > 0:
                print('-', value)
                c -= 1
                e -= 1
                f -= 1
                value += 1
                if c <= 0:
                    print('|',a,value,'  ',7)
                    auxillaryQueue.removeFromHead()
                    break
                elif f <= 0:
                    print('|',a,value,'  ',8)
                    auxillaryQueue.removeFromHead()
                    if e > 0:
                        waitingQueue.addAtTail(a, value + int(arr1[1]), c, e, arr1[1])
                    else:
                        waitingQueue.addAtTail(a, value + int(arr1[1]), c, arr1[0], arr1[1])
                        flag1 = True
                    break
            if c > 0 and e <= 0 and f > 0:
                print('|',a,value,'  ',9)
                auxillaryQueue.removeFromHead()
                readyQueue.addAtTail(a, value, c, arr1[0], f)
                flag1 = False
    elif e<=0 :
        readyQueue.addAtTail(a,value,c,arr[0],f)
        readyQueue.removeFromHead()
        while auxillaryQueue.empty() == False:
            node1 = auxillaryQueue.getHead()
            a = node1.name
            b = int(node1.arrivalTime)
            c = int(node1.burstTime)
            e = int(node1.quantum)
            f = int(node1.IO_Time)
            while e > 0:
                print('-', value)
                c -= 1
                e -= 1
                f -= 1
                value += 1
                if c <= 0:
                    print('|',a,value,'  ',10)
                    auxillaryQueue.removeFromHead()
                    break
                elif f <= 0:
                    print('|',a,value,'  ',11)
                    auxillaryQueue.removeFromHead()
                    if e > 0:
                        waitingQueue.addAtTail(a, value + int(arr1[1]), c, e, arr1[1])
                    else:
                        waitingQueue.addAtTail(a, value + int(arr1[1]), c, arr1[0], arr1[1])
                        flag1 = True
                    break
            if c > 0 and e <= 0 and f > 0:
                print('|',a,value,'  ',12)
                auxillaryQueue.removeFromHead()
                readyQueue.addAtTail(a, value, c, arr1[0], f)
                flag1 = False
print(value)