
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # create new graph
    g = Graph()

    # for each parent and child in ancestors add the vertex
    for (parent, child) in ancestors:
        g.add_vertex(parent)
        g.add_vertex(child)

    # for each parent and child in ancestors add the edges
    for (parent, child) in ancestors:
        g.add_edge(parent, child)

    # Instantiate a new list to store the longest path in the graph
    longest_path = []

    # Iterate through ancestors to find the path to the starting_node
    for (parent, child) in ancestors:
        # Perform a depth-first search to return the path from the current parent node to the starting_node
        path = g.dfs(parent, starting_node)
        # if the current_path is longer than the path stored in longest_path it will replace the path in it
        if path and len(path) > len(longest_path):
            longest_path = path.copy()

    # if longest_path is not empty then return the earliest ancestor
    if len(longest_path) > 1:
        return longest_path[0]
    else:
        # if longest_path is empty then return -1
        return -1

"""
# Instantiate ancestor data
ancestor_data = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

ancestor_1 = earliest_ancestor(ancestor_data, 4)
ancestor_2 = earliest_ancestor(ancestor_data, 5)

print(ancestor_1)  # Should display -1
print(ancestor_2)  # Should display 4
"""