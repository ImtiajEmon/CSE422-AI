from collections import defaultdict

def dfs(u, goal):
    visited[u] = 1
    if u == goal:
        return 1

    for v in adj_list[u]:
        if visited[v]:
            continue
        #print(f"Going {u} to {v}") #To see what actually happend (aditional line)
        link[v] = u
        if(dfs(v, goal)):
            return 1


#-----------------------------------------------------
adj_list = defaultdict(list)  #TO represent the graph with adjacency list method
visited = dict()    #To trac wheather a node is visited or not
link = dict()         #To trac the parent node

node = int(input("Enter the number of nodes: "))
edge = int(input("Enter the number of edges: "))

nodes = set()
# Taking the edges
for i in range(edge):
    u, v = input().split(' ')
    nodes.add(u)
    nodes.add(v)
    visited[u] = 0
    visited[v] = 0

    # For undirected graph
    adj_list[u].append(v)
    adj_list[v].append(u)

strt_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

found = 0
found = dfs(strt_node, goal_node)

path = []

if found:
    while goal_node != strt_node:  #Discovering the path
        path.append(goal_node)
        goal_node = link[goal_node]
    path.append(strt_node)

    path.reverse()
    print("The goal node is found. The path is ")
    for node in path:
        print(node, end = ' ')

else:
    print("Goal not fond!!")
