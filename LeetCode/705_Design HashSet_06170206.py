class MyHashSet:

    def __init__(self,capacity=10):
        """
        Initialize your data structure here.
        """
        self.capacity = capacity
        self.data = [None] * capacity
        

    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
               
        i = key % self.capacity
        head = self.data[i]
        if head == None:
            head = ListNode(key)
            self.data[i] = head #######
        else:
            while head.val != key:
                if head.next != None:
                    head = head.next
                else: #找到最後都還沒加過這個值         
                    head.next = ListNode(key)  
            pass

    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """       
        i = key % self.capacity
        head = self.data[i]
        
        if head == None:
            return None
        else:     #head != None
            if head.val == key:  #如果head = a
                head = head.next          #他的下一個值要取代他
                self.data[i] = head    #同時下一個值會變成新的頭
        if head:
            while head.next:
                if head.next != None:       #如果要刪除的值不在頭
                    if head.next.val != key:
                        head = head.next    #要往後找
                    else: #如果找到最後沒找到
                        head.next = head.next.next #回傳
                else:
                    return None
    
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        
        i = key % self.capacity
        head = self.data[i]
        if head == None:
            return False
        else:  #head != None
            while head.val != key:
                head = head.next
                if head == None:
                    return False            
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
