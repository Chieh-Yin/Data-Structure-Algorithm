
# coding: utf-8

# In[1]:


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def encoding(self,key):
        from Cryptodome.Hash import MD5 
        h = MD5.new()
        h.update(key.encode("utf-8"))
        output = int(h.hexdigest(),16)
        return output
    
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        a = MyHashSet.encoding(self,key)
        i = a % self.capacity
        head = self.data[i]
        if head == None:
            head = ListNode(a)
            self.data[i] = head
        else:
            while head.val != a:
                if head.next != None:
                    head = head.next
                else:     
                    head.next = ListNode(a)  
            pass
        
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        a = MyHashSet.encoding(self,key)        
        i = a % self.capacity
        head = self.data[i]
        if head == None:
            return None
        else:    
            if head.val == a: 
                head = head.next         
                self.data[i] = head    
        if head:
            while head.next:
                if head.next != None:       
                    if head.next.val != a:
                        head = head.next    
                    else: 
                        head.next = head.next.next
                else:
                    return None
                           
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        a = MyHashSet.encoding(self,key)
        i = a % self.capacity
        head = self.data[i]
        if head == None:
            return False
        else:  
            while head.val != a:
                head = head.next
                if head == None:
                    return False            
            return True          

