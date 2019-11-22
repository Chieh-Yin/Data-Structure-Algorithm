
# coding: utf-8

# In[1]:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    
    def __init__(self):
        self.root = None
    
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root == None:
            root = TreeNode(val) 
        else:
            if val <= root.val:
                if root.left == None:
                    root.left = TreeNode(val)
                    return root.left
                else:                      #root.left != None
                    return Solution.insert(self,root.left,val)
            else: 
                if root.right == None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    return Solution.insert(self,root.right,val)
                    
    def delete(self,root,target):
        new_list = []
        Solution.pre_order_mode(self,root,new_list,target)
        for i in range(len(new_list)):
            Solution.delete_term1(self,root,target)
        return root
    
    def delete1(self,root,target,new_val):
        new_list = []
        Solution.pre_order_mode(self,root,new_list,target)
        for i in range(len(new_list)):
            Solution.delete_term1(self,root,target)
            return root
    
    def delete_term1(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """  
        if root == None:
            return None
        elif target == root.val:
            return Solution.delete_term2(self,root)
        elif target < root.val:
            root.left = Solution.delete_term1(self,root.left,target)
        else:
            root.right = Solution.delete_term1(self,root.right,target)
        return root
                
    
    def delete_term2(self,root):
        if root.left != None and root.right != None:           #有左節點跟右節點
            p = Solution.get_left_max(self,root.left)
            root.val = p.val
            root.left = Solution.delete_term1(self,root.left,p.val)
            return root
        elif root.left != None:                              #只有左節點
            return root.left
        elif root.right != None:                             #只有右節點
            return root.right
        else:                                                #沒有其他節點
            return None
        return delete_term1(self,root,target)
    
    def get_left_max(self,root):
        if root.right == None:
            return root
        else:
            Solution.get_left_max(self,root.right,target)
            
    def pre_order_mode(self,root,new_list,target):             #使用pre_order走訪        
        if root != None:
            if root.val==target:
                new_list.append(root.val)
            Solution.pre_order_mode(self,root.left,new_list,target)
            Solution.pre_order_mode(self,root.right,new_list,target)
        return new_list
            
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        
        if root == None:
            return None
        else:

            if target < root.val:   #target<root.val往左邊找
                if l != None:     #如果左邊有節點存在
                    if root.left.val != target:      #如果左邊節點的值不等於target
                        return Solution.search(self,root.left,target)         #繼續往下找
                    else:           #如果左節點=target，回傳root.left
                        return root.left 
                else:           #如果左邊沒有節點存在
                    return None  #回傳NONE
                
            elif target > root.val:   #target >root.val往右邊找
               
                if root.right != None:
                    if root.right.val != target:
                        return Solution.search(self,root.right,target)                 
                    else:
                        return root.right
                else:
                    return None
                
            else:                    #target=root.val直接回傳
                return root
                            
        
        
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
        """
        new_list = []
        Solution.pre_order_mode(self,root,new_list,target)
        Solution.delete(self,root,target)
        for k in range (int(len(new_list))):
            Solution.insert(self,root,new_val)
        return root
    

