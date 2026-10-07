node_conn = {
    "A": ["B", "C"],
    "B": ["D", "goal"],
    "D": ["I", "J"],
    "C": ["F", "G"],
    "G": ["H"],
}

stack = []
visited = []

initial_node = "A"
stack.append(initial_node)

while len(stack) != 0:

    current_node = stack.pop()

    if current_node not in visited:
        visited.append(current_node)

        for neighbor in node_conn.get(current_node, []):
            if neighbor not in visited:
                stack.append(neighbor)

    print("Stack:", stack)
    print("Current Node:", current_node)
    print("Visited:", visited)
    