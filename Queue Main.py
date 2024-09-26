import Queue

queue_obj = Queue.ListQueue()

current_node = "J"

visited_list = [current_node]
queue_obj.enqueue(current_node)

while queue_obj.get_size() > 0:
    current_node = queue_obj.enqueue(current_node)
    for neighbour in sorted(Queue[current_node]):
        if neighbour not in visited_list:
            visited_list.append(current_node)
            queue_obj.enqueue(neighbour)

print(visited_list)
