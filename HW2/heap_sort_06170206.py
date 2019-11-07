
# coding: utf-8

# In[113]:


##### heap_sort_ID.py

class Solution(object):
    
 
    def heap_sort(self,nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
 
        n = len(nums)
        new_list = []
       
    
        for i in range((n//2)-1,-1,-1):
            Solution.heapify(nums,i,n)
            
        for i in range(n,0,-1):
            
            new_list.insert(0,nums[0])
            nums[0]=nums[n-1]
            nums.pop()
            n=n-1
            Solution.heapify(nums,0,n)
        return new_list
            
    def heapify(nums,i,n):
    
        left = 2*i + 1
        right = 2*i + 2
        
        if left < n and nums[left] > nums[i]:
            max = left
            
        else:
            max = i
            
    
        if right < n and nums[right] > nums[max]:
            max = right
            
            
        if max != i:
            nums[i],nums[max] = nums[max],nums[i]
            
            
            Solution.heapify(nums,max,n)


# In[114]:


Solution().heap_sort([3,5,1,2,6,9])

