# This is only work for positive cost.
from collections import defaultdict
from queue import PriorityQueue


def dijkstra(source, nodes, goal):
    for i in range(1, nodes+1):  # make all distance to infinity
        dist[i] = 1e9 + 10

    dist[source] = 0             # distance of source node is 0

    pq = PriorityQueue()

    pq.put((0, source))  #(cost, node)

    while not pq.empty():
        pair = pq.get()
        cost = pair[0]
        u = pair[1]

        if u == goal: # checking for goal
            return 1

        if dist[u] != cost:
            continue

        for adj_pair in adj_lst[u]:
            adj_cost = adj_pair[0]
            adj_node = adj_pair[1]

            if cost + adj_cost < dist[adj_node]:
                dist[adj_node] = cost + adj_cost
                link[adj_node] = u
                pq.put((dist[adj_node], adj_node))


#-----------------------------------------------------
adj_lst = defaultdict(list)
dist = [0] * int(1e5)
link = [0] * int(1e5)

nodes = int(input("Enter the number of nodes: "))
edges = int(input("Enter the number of edges: "))

# Taking the edges with cost
print("Give input like node1 node2 cost-")
for i in range(edges):
    u, v, cost = input().split(' ')
    u = int(u)
    v = int(v)
    cost = int(cost)

    # For undirected graph
    adj_lst[u].append((cost, v))
    adj_lst[v].append((cost, u))

strt = 1
goal_node = int(input("Enter the goal node: "))

found = 0
found = dijkstra(strt, nodes, goal_node)
    

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




'''from collections import defaultdict
from queue import PriorityQueue


def dijkstra(source, nodes):
    # make all distance to infinity
    for i in range(1, nodes+1):
        dist[i] = 1e9 + 10

    # make source distance 0
    dist[source] = 0

    pq = PriorityQueue()

    pq.put((0, source))  #(cost, node)

    while not pq.empty():
        pair = pq.get()
        cost = pair[0]
        u = pair[1]

        if dist[u] != cost:
            continue

        for adj_pair in adj_lst[u]:
            adj_cost = adj_pair[0]
            adj_node = adj_pair[1]

            if cost + adj_cost < dist[adj_node]:
                dist[adj_node] = cost + adj_cost
                pq.put((dist[adj_node], adj_node))


#-----------------------------------------------------
adj_lst = defaultdict(list)
dist = [0] * int(1e5)

nodes = int(input())
edges = int(input())

# Taking the edges with cost
for i in range(edges):
    u, v, cost = input().split(' ')
    u = int(u)
    v = int(v)
    cost = int(cost)

    # For undirected graph
    adj_lst[u].append((cost, v))
    adj_lst[v].append((cost, u))


dijkstra(1, nodes)

for v in range(1, nodes+1):
    print("Distance from 1"," to ", v, "= ", dist[v])'''