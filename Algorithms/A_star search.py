# This is only work for positive cost.
from collections import defaultdict
from queue import PriorityQueue


def dijkstra(source, goal):
    for i in nodes:  # make all distance to infinity
        dist[i] = 1e9 + 10

    dist[source] = 0             # distance of start node is the heuristic cost of that node

    pq = PriorityQueue()

    pq.put((h[source], source))  #(cost, node)

    while not pq.empty():
        pair = pq.get()
        cost = pair[0]
        u = pair[1]

        if u == goal: # checking for goal
            return 1

        #if dist[u] != cost:
            #ontinue

        for adj_pair in adj_lst[u]:
            adj_cost = adj_pair[0]
            adj_node = adj_pair[1]

            if cost - h[u] + adj_cost + h[adj_node] < dist[adj_node]:
                dist[adj_node] = cost - h[u] + adj_cost + h[adj_node]
                link[adj_node] = u
                pq.put((dist[adj_node], adj_node))


#-----------------------------------------------------
adj_lst = defaultdict(list)
dist = dict()
link = dict()

node = int(input("Enter the number of nodes: "))
edge = int(input("Enter the number of edges: "))

nodes = set()

# Taking the edges with cost
print("Give input like node1 node2 cost-")
for i in range(edge):
    u, v, cost = input().split(' ')
    cost = int(cost)

    #To store all nodes
    nodes.add(u) 
    nodes.add(v)
    # For undirected graph
    adj_lst[u].append((cost, v))
    adj_lst[v].append((cost, u))

h = dict()
print("Enter the Heuristic cost like node cost -")
for i in range(node):
    n, cost = input().split(' ')
    cost = int(cost)
    h[n] = cost

strt = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

found = 0
found = dijkstra(strt, goal_node)
    

path = []

if found:
    current = goal_node
    while current != strt:
        path.append(current)
        current = link[current]
    path.append(strt)

    path.reverse()

    print("The goal node is found.")
    print(f"The total cost to go to goal node is: {dist[goal_node]}")
    print("The path is: ")
    for node in path:
        print(node, end = " ")

else:
    print("Goal not found!!")
