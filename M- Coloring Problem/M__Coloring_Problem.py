'''
    Given an undirected graph and an integer M.
    The task is to determine if the graph can be colored with at most M colors 
    such that no two adjacent vertices of the graph are colored with the same color. 
    Here coloring of a graph means the assignment of colors to all vertices. 
    Print True if it is possible to colour vertices and False otherwise.
'''
print('''Function to determine if graph can be coloured with at most M colours such
that no two adjacent vertices of graph are coloured with same colour.
''')
def graphColoring(graph, N, M):
    
    #your code here
    color = []
    while len(color) < N:
        for i in range(1,M+1):
            color.append(i)

    for i in range(N):
        for j in range(i+1, N):
            if graph[i][j] & color[j] == color[i]:
                result = False
            else:
                result = True
    #print(graph)
    return result
    

if __name__ == "__main__":
    print('Enter the number of test (t=1)')
    t = int(input())
    while(t>0):
        print('Nodes(N = 14)')
        N = int(input())
        print('Color(M = 4)')
        M = int(input())
        print('Edges(E=65)')
        E = int(input())
        print('Edges[]= 3 6 1 8 2 8 9 14 4 14 13 14 1 6 4 6 11 14 2 7 3 10 10 11 4 5 2 3 8 13 10 13 12 14 6 8 4 9 5 6 1 13 10 12 8 14 1 10 12 13 3 7 6 14 6 12 10 14 4 11 1 14 9 11 5 9 6 7 7 10 7 8 9 13 5 14 8 10 5 8 3 12 6 13 1 12 2 11 1 2 9 10 4 7 8 12 11 12 5 12 2 12 5 10 6 9 7 13 4 10 4 12 5 11 8 11 3 13 7 11 5 7 7 14 1 7 1 4 7 12')
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(N)] for j in range(N)]
        cnt = 0
        for i in range(E):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        #print(graph)
        print(graphColoring(graph, N, M))
        t = t-1
