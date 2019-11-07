
# coding: utf-8

# In[56]:


###### merge_sort_ID.py

class Solution(object):
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
    
        if len(nums) <= 1:
            return nums
        
        else:
          
            Middle = len(nums)//2
            Left = nums[:Middle]
            Right = nums[Middle:]
            
            Left = self.merge_sort(Left)
            Right = self.merge_sort(Right)
            
            
            Merge = []                   
            i = 0
            j = 0 
            
            while i < len(Left) and j < len(Right):
                if Left[i] <= Right[j]:
                    Merge.append(Left[i])
                    i = i+1
                    
                else:
                    Merge.append(Right[j])
                    j = j+1
                    
            while i < len(Left):
                Merge.append(Left[i])
                i = i+1
                
            while j < len(Right):
                Merge.append(Right[j])
                j = j+1
               
        
        return Merge
    


# In[59]:


Solution().merge_sort([3,5,1,2,7,9])


# In[60]:


Solution().merge_sort([3,5,1,2,7,-9,6])

