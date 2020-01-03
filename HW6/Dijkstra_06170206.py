
# coding: utf-8

# In[6]:


from collections import defaultdict 
import math 
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.edge = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        self.edge.append([w,u,v])
    def Dijkstra(self, s): 
        output={}
        picked = []
        distance = []        
        a = [] 
        for i in range(self.V):
            a.append(i)
        for j in a:
            if j == s:
                distance.append(0)
            else:
                distance.append(math.inf)
        new_distance=[]   
        for k in a:                
            new_distance.append(distance[k])
        minimum = min(new_distance)
        picked.append(minimum)
        for m in a:
            if self.graph[minimum][m] != 0:                
                distance[m] = self.graph[minimum][m]
            else:
                if m == s:
                    distance[m] = 0
                else:
                    distance[m] = math.inf
        a.remove(minimum)              
        while a:
            new_distance=[]            
            for k in a:                
                new_distance.append(distance[k])
            minimum = min(new_distance)
            for c in range(len(a)):
                if new_distance[c]==minimum:
                    picked.append(a[c])
                    break
            for n in a: 
                if self.graph[a[c]][n] != 0:
                    if distance[n] > self.graph[a[c]][n]+distance[a[c]]:
                        distance[n] = self.graph[a[c]][n]+distance[a[c]]
                    else:
                        distance[n]=distance[n]
                else:
                    pass
            a.remove(a[c])
        for l in range(self.V):
            output.setdefault(str(l),distance[l])
        return output 
    def Kruskal(self):
        output={}
        i=0
        self.edge.sort()
        parent = [-1]*self.V
        while i < len(self.edge):
            head=self.edge[i][1]
            tail=self.edge[i][2]
            if parent[head] == -1:
                if parent[tail] == -1:
                    parent[tail]=self.edge[i][1]
                else:
                    if parent[tail]==self.edge[i][1]:
                        self.edge[i][0]=0  
                    else:
                        for k in range(self.V):
                            if parent[k]==parent[tail] and k != tail:
                                parent[k]=self.edge[i][1]
                            elif parent[k]==-1 and k==parent[tail]:
                                parent[k]=self.edge[i][1]
                        parent[tail]=self.edge[i][1]
            else:
                if parent[tail]==-1:
                    if parent[head] == self.edge[i][2]: 
                        self.edge[i][0]=0       
                    else:
                        for k in range(self.V):
                            if parent[k]==self.edge[i][2]:
                                parent[k]=parent[head]
                        parent[tail]=parent[head]
                else:
                    if parent[tail] == parent[head]:
                        self.edge[i][0]=0
                    else:
                        for k in range(self.V):
                            if parent[k]==-1:
                                if k==parent[tail]:
                                    parent[k]=parent[head]
                            else:
                                if parent[k]==parent[tail] and k != tail:
                                    parent[k]=parent[head] 
                        parent[tail]=parent[head]
            i+=1
        for num in range(len(self.edge)):
            if self.edge[num][0]!=0:
                path='{}-{}'.format(self.edge[num][1],self.edge[num][2])
                output.setdefault(path,self.edge[num][0])
        return output 

