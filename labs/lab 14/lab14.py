

def find_adj_matrix1():

    matrix1 = [[0, 0, 1, 0, 0, 0],
               [0, 0, 0, 1, 1, 1],
               [1, 0, 0, 1, 0, 1],
               [0, 1, 1, 0, 0, 0],
               [0, 1, 0, 0, 1, 1],
               [0, 1, 1, 0, 1, 0]]
            
    return matrix1

def find_adj_matrix2():
    matrix2 = [[0, 1, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]]
            
    return matrix2

def find_adj_list1():
    list1 = {'A': {'C'},
            'C': {'A', 'D', 'F'},
            'D': {'C', 'B'},
            'F': {'C', 'B', 'E'},
            'B': {'D', 'F', 'E'},
            'E': {'B', 'F', 'E'}}
    
    return list1
            
def find_adj_list2():
    list2 = {'1': {'2', '3'},
            '2': {'4'},
            '3': {'4'},
            '4': {'5'}}
    
    return list2
            

    

def bfs(adjacency_list, start_vertex):

    visited = set()  #Initialize list to keep track of visited nodes
    queue = [] #Initialize queue
    queue.append(start_vertex) #Enqueue starting node
    bfs_order = [] #Initialize list to record the order in which vertices are visited
    
    while not len(queue) <= 0:
        #Dequeue the first node in the queue
        current_vertex = queue.pop(0)
        
        #Print the current node
        print(current_vertex, end=' ')

        
        if current_vertex not in sorted(list(visited)):
            bfs_order.append(current_vertex)
            visited.add(current_vertex)
            for neighbour in sorted(list(adjacency_list[current_vertex])):
                if neighbour not in sorted(list(visited)): #Add all unvisited neighbors to the queue
                    queue.append(neighbour)

        print("\nqueue: " + str(queue)) 
    
    print(bfs_order)
    return bfs_order


def topological_sort_util(node, visited, stack, adjacency_list):
    print("Node: ")
    print(node)
    visited.add(node)
    if node in adjacency_list:
        for neighbour in sorted(adjacency_list[node])[::-1]:
            print(sorted(adjacency_list[node]))
            if neighbour not in sorted(list(visited)): #Call util function on all unvisited neighbors
                print("Neighbour: ")
                print(neighbour)
                topological_sort_util(neighbour, visited, stack, adjacency_list)

    stack.append(node)
    print("Stack: ")
    print(stack)


djacency_list = {
            '1': {'2', '3'},
            '2': {'4'},
            '3': {'4'},
            '4': {'5'}
        }

def topological_sort(adjacency_list):
    visited = set()
    stack = []
    for node in adjacency_list:
        if node not in sorted(list(visited)):
            topological_sort_util(node, visited, stack, adjacency_list)

    return stack[::-1]




