
# coding: utf-8

# In[3]:


from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def BFS(self, s): 
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

