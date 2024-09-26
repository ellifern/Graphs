import Stack
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

stack_obj = Stack()
visited_list = []

current_node = "J"

stack_obj.push(current_node)

while not stack_obj.getsize() > 0:
    temp_current = current_node

    for neighbour in sorted(adj_list[current_node]):
        if neighbour not in visited_list:
            current_node = neighbour
            stack_obj.push(current_node)
            visited_list.append(current_node)
            break

    if temp_current == current_node:
        current_node = stack_obj.pop()
