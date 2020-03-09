import random
import time
import matplotlib.pyplot as plt
import numpy as np


# !!!!!    phase 1    !!!!!


# implementation of insertion sort
def insertionSort(lon): # lon ==>> list of numbers
    for i in range(1, len(lon)):
        key = lon[i]
        j = i-1

        while (j>=0 and lon[j]>key):
            lon[j+1] = lon[j]
            j -= 1
        
        lon[j+1] = key




# generating list of random numbers

def numberGenerator(a, b, c): # a, b, c ==>> length of the numbers in three lists
    firstList = []
    secondList = []
    thirdList = []

    for f in range(a):
        firstList.append(random.randint(10 ** 3, 10 ** 4))
    
    for s in range(b):
        secondList.append(random.randint(10 ** 3, 10 ** 4))

    for t in range(c):
        thirdList.append(random.randint(10 ** 3, 10 ** 4))
    
    mainList = []
    mainList.append(firstList)
    mainList.append(secondList)
    mainList.append(thirdList)
    return mainList


# implementing the insert method

def insert(number, array): # inserting a number in its sorted position in the given sorted list(array)
    a = 0
    b = 1
    if array[0] == number:
        array.insert(0, number)
        return

    for i in range(len(array)):
        if array[i] == number:
            array.insert(i, number)
            return
        elif array[i] > number:
            array.insert(i, number)
            return





# !!!!!!!   phase 2   !!!!!!!!!!





# implementing doubly linked list(dll) 
# implementing doubly linked list(dll) 

class Node:

    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class dll:
    
    counter = 0 

    def __init__(self):
        self.head = None

    # adding a node at first
    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        
        if self.head is not None:
            self.head.prev = newNode
        
        self.head = newNode
        self.counter += 1

    # adding node at the end
    def append(self, newData):
        newNode = Node(newData)
        newNode.next = None
        
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            self.counter += 1
            return

        lastNode = self.head
        while (lastNode.next is not None):
            lastNode = lastNode.next
            
        lastNode.next = newNode

        newNode.prev = lastNode
        self.counter += 1
        return

    # adding a node after a given node
    def insertAfter(self, prevNode, newData):
        newNode = Node(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        
        if (newNode.next is not None):
            newNode.next.prev = newNode

    def delete(self, targetNode):
        if self.head is None:
            return
        
        temp = self.head
        while (temp.next is not targetNode):
            temp = temp.next

        if (temp.next.next is None):
            temp.next = None
            return
        temp.next.next.prev = temp
        temp.next = temp.next.next

    

    # finding a number in the linked list if it exists
    def crawler(self, number):
        temp = self.head
        i = 0
        while (i != number and temp.next is not None):
            temp = temp.next
            i += 1
        return temp

    # inserting a node with binary search
    def inserting(self, number):
        firstIndex = 0
        lastIndex = self.counter

        if (self.counter is 0):
            self.append(number)
            return

        while (firstIndex <= lastIndex):
            middle = firstIndex + (lastIndex - firstIndex) / 2
            helpNode = self.crawler(middle)

            if ((helpNode.data > number and helpNode.prev is None)):
                self.push(number)
                self.counter += 1
                return
            
            elif ((helpNode.data < number and helpNode.next is None)):
                self.append(number)
                self.counter += 1
                return

            elif ((helpNode.data == number) or (helpNode.data < number and helpNode.next.data > number)):
                self.insertAfter(helpNode, number)
                self.counter += 1
                return

            elif (helpNode.data < number and helpNode.next is not None):
                firstIndex = middle + 1
            elif (helpNode.data > number and helpNode.prev is not None):
                lastIndex = middle - 1


    # insertion sort with linked list

    def insertionSort(self):
        sortedLL = dll()
        temp = self.head
        sortedLL.append(temp.data)
        while(temp.next is not None):
            sortedLL.inserting(temp.next.data)
            temp = temp.next
        self.head = sortedLL.head

    def toList(self):
        numbers = [] 
        temp = self.head
        while (temp is not None):
            numbers.append(temp.data)
            temp = temp.next
        return numbers

    def printer(self, node):
        while (node is not None):
            print(node.data)
            node = node.next




# comparing...




def simple(pl, sl):
    timeList = [0, 0, 0]
    
    a0 = 0
    for e in pl:
        start = time.clock()
        insertionSort(e)
        end = time.clock()
        timeList[a0] += (end - start)
        a0 += 1
    pl.sort(key = lambda s:len(s))

    f = pl[0]
    a0 = 0
    for i in sl:
        
        start = time.clock()
        e = 0
        for j in i:
            insert(j, pl[e])
        e += 1
        end = time.clock()
        timeList[a0] += (end - start)
        a0 += 1
    pl.sort(key = lambda s:len(s))
    return timeList

def complicated(pl, sl):
    timeList = [0, 0, 0]

    result1 =[]
    t = 0
    for a0 in pl:
        start = time.clock()
        ll = dll()
        for a1 in a0:
            ll.append(a1)
        ll.insertionSort()
        result1.append(ll.toList())
        end = time.clock()
        timeList[t] += (end - start)
        t += 1


    result1.sort(key = lambda s:len(s))
    result2 = []
    t = 0
    for b0 in [0, 1, 2]:
        start = time.clock()
        ll2 = dll()
        for b1 in result1[b0]:
            ll2.append(b1)
        for c1 in sl[b0]:
            ll2.inserting(c1)
        result2.append(ll2.toList())
        end = time.clock()
        timeList[t] += (end - start)
    result2.sort(key = lambda s:len(s))
    return timeList



# time 

a = int(input("Enter the lowest test case number: "))
b = int(input("Enter the medium test case number: "))
c = int(input("Enter the highest test case number: "))

primaryList = numberGenerator(a, b, c)
secondaryList = numberGenerator(a, b, c)


simpleTimesList = simple(primaryList, secondaryList)
complicatedTimesList = complicated(primaryList, secondaryList)

l1 = []
l2 = []
for i in (simpleTimesList):
    l1.append(round(i, 5))
for i in (complicatedTimesList):
    l2.append(round(i, 5))
print(l1, l2)


# plotting...
row1 = (a, b, c)
col1 = (l1)
row2 = row1
col2 = (l2)

ind = np.arange(3) 
width = 0.5

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, col1, width, yerr=col1,
                color='SkyBlue', label='simple')
rects2 = ax.bar(ind + width/2, col2, width, yerr=col2,
                color='IndianRed', label='linked list')

ax.set_ylabel('Time')
ax.set_title('Time Table for Linked List and Simple Insertion Sort')
ax.set_xticks(ind)
ax.set_xticklabels(('Test Case 1', 'Test Case 2', 'Test Case 3'))
ax.legend()


def autolabel(rects, xpos='center'):


    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()