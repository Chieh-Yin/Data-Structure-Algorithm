
# coding: utf-8

# In[5]:


# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        state1 = [] 
        state2 = []      
        state2.append(s)
        state1.extend(self.graph[s])  
        
        while state1  :   
            if state1:
                first = state1[0]
                state1 = state1[1:]
                state2.append(first)
            else:
                pass
            for i in self.graph[first]:
                if i not in state1 and i not in state2:
                    state1.append(i)
        return state2
        
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        state1 = []
        state2 = []
        state2.append(s)
        state1.extend(self.graph[s])
     
        while state1:
            top = state1[-1]
            state1 = state1[:-1]
            state2.append(top)
            for i in self.graph[top]:
                if i not in state1 and i not in state2:
                    state1.append(i)
        return state2

