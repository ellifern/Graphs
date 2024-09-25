adj_list = {
    'A': ['C', 'B'],
    'B': ['A', 'D', 'K'],
    'C': ['A', 'D', 'F'],
    'D': ['C', 'F', 'G', 'H', 'E'],
    'E': ['D', 'H', 'K'],
    'F': ['C', 'G', 'J', 'D'],
    'G': ['D', 'F', 'H', 'J'],
    'H': ['E', 'D', 'G'],
    'K': ['B', 'E', 'D'],
    'J': ['G', 'F']
}

def check_neigh(adj_list, node):
    print(adj_list[node])

def connected(adj_list, node1, node2):
    if node1 in adj_list[node2]:
        print (True)
    else:
        return (False)

check_neigh(adj_list, 'A')

