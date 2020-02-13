# An Iterative Python program to do DFS traversal from  
# a given source vertex. DFS(int s) traverses vertices  
# reachable from s.  
  
# This class represents a directed graph using adjacency  
# list representation  
class Graph:  
    def __init__(self,V): # Constructor  
        self.V = V        # No. of vertices  
        self.adj  = [[] for i in range(V)]  # adjacency lists  
  
    def addEdge(self,v, w):     # to add an edge to graph 
        self.adj[v].append(w)    # Add w to v’s list.  
  
  
    # prints all not yet visited vertices reachable from s  
    def DFS(self,s):            # prints all vertices in DFS manner from a given source. 
                                # Initially mark all verices as not visited  
        visited = [False for i in range(self.V)]  
  
        # Create a stack for DFS  
        stack = [] 
  
        # Push the current source node.  
        stack.append(s)  
  
        while (len(stack)):  
            # Pop a vertex from stack and print it  
            s = stack[-1]  
            stack.pop() 
  
            # Stack may contain same vertex twice. So  
            # we need to print the popped item only  
            # if it is not visited.  
            if (not visited[s]):  
                print(s,end=' ') 
                visited[s] = True 
  
            # Get all adjacent vertices of the popped vertex s  
            # If a adjacent has not been visited, then push it  
            # to the stack.  
            for node in self.adj[s]:  
                if (not visited[node]):  
                    stack.append(node)  
                  
if __name__ =="__main__":
  # Create a graph given  
  # in the above diagram 
  g = Graph(4) 
  g.addEdge(0, 1) 
  g.addEdge(0, 2) 
  g.addEdge(1, 2) 
  g.addEdge(2, 0) 
  g.addEdge(2, 3) 
  g.addEdge(3, 3) 

  print("Following is DFS from (starting from vertex 0)") 
  g.DFS(0) 
  
