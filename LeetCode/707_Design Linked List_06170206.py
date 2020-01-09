class Node(object):
    def __init__(self,value):
        self.val = value  # 代表Node 的data
        self.next = None # 指向下一個node
        
    
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0 
    
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
        if index < 0 or index>=self.size:
            return -1
        if self.head == None:
            return -1
        a = self.head
        
        for i in range(index):
            a = a.next
        return a.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        #先判斷linked-list 是否存在，用self.size=0 或 self.head= None
        if self.head== None : 
            self.head = Node(val)
        else:
            newHead = Node(val)
            newHead.next = self.head
            self.head = newHead
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        a=self.head
        if a == None:
            self.head = Node(val)
        else:
            while a.next != None:
                a = a.next
        
            a.next = Node(val)
        self.size += 1    
        
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        1. 當index = linked-List 長度 時，加尾巴
        2. 當index > linked-List 長度 時，不動作
        3. 當index < 0 ， 加在頭
        4. 其他就是插入該index ，並將其他node往後推
        """

        if index > self.size:
            pass
        elif index == self.size :
            self.addAtTail(val)
        elif index<=0:
            self.addAtHead(val)
        else:
            a = self.head
            for i in range(index-1):
                a = a.next
            NewNode = Node(val)
            NewNode.next = a.next
            a.next = NewNode
            self.size += 1
                
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        a=self.head
        if index < 0 or index >= self.size :
            pass
        elif index==0:
            self.head=a.next
            self.size-=1
        else:
            for i in range(index-1):
                a = a.next
            a.next=a.next.next
            self.size-=1
                
