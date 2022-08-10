
def isSafe(graph, v, colour, c, V):
    
    for i in range(V):
        #checking if the connected nodes to v have same colour as c.
        if (graph[v][i] == 1 and colour[i] == c):
            return False
    
    #returning true if no connected node has same colour.
    return True


def graphColourUtil(graph, m, colour, v, V):

    #if all vertices have been assigned colour then we return true.
    if v == V:
        return True

    for c in range(1, m+1):
        #checking if this colour can be given to a particular node.
        if (isSafe(graph, v, colour, c, V) == True):
            #assigning colour to the node.
            colour[v] = c
            #calling function recursively and checking if other nodes 
            #can be assigned other colours.
            if (graphColourUtil(graph, m, colour, v+1, V) == True):
                #returning true if the current allocation was successful.
                return True
            #if not true, we backtrack and remove the colour for that node.   
            colour[v] = 0
            
    #if no colour can be assigned, we return false.
    return False
    
#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    colour = [0] * V
    
    #checking if colours can be assigned.
    if (graphColourUtil(graph, k, colour, 0, V) == False):
        return False
    return True
    
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1
