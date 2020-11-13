"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print('That vertex already exists!')
        else:
            # Adds the vertex to the graph if it does not exist
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Stretch: Checks if v1 and v2 exist in the graph
        if v1 in self.vertices and v2 in self.vertices:
            # if both add a directed edge to the graph by connecting v1 to v2
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist!')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Instantiate an empty queue then enqueue the starting_vertex to it
        q = Queue()
        q.enqueue(starting_vertex)
        # Create a node to track the nodes visited in the graph
        visited = set()
        # loop through the graph as long as the queue is not empty
        while q.size() > 0:
            vertex = q.dequeue()
            # Check if the vertex is in visited
            if vertex not in visited:
                # if the vertex is not in visited then print vertex
                print(vertex)
                # also add vertex to visited
                visited.add(vertex)
                # for each edge of the vertex
                for next_vertex in self.get_neighbors(vertex):
                    # Add the next edge to the queue
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Instantiate an empty stack and then push the starting_vertex onto it
        s = Stack()
        s.push(starting_vertex)
        # Create a node to track the nodes visited in the graph
        visited = set()
        # loop through the graph as long as the stack is not empty
        while s.size() > 0:
            # Pop the node off the top of the stack
            vertex = s.pop()
            # Check if visited contains the current contents of vertex
            if vertex not in visited:
                # if visited does not contain the current contents of vertex then print vertex
                print(vertex)
                # also add vertex to visited_node
                visited.add(vertex)
                # for each edge of the vertex
                for next_vertex in self.get_neighbors(vertex):
                    # Push the next edge onto the stack
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if current visited is None make it an empty set
        if not visited:
            visited = set()

        # Then add the starting_vertex to the visited and then print the starting_vertex
        visited.add(starting_vertex)
        print(starting_vertex)

        # Iterate through the edges
        for vertex in self.vertices[starting_vertex]:
            if vertex not in visited:
                # make a recursive call
                self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Instantiate an empty queue
        q = Queue()
        # enqueue a list initialized with the starting_vertex and this will hold the path
        q.enqueue([starting_vertex])

        # Create a node to track the nodes visited in the graph
        visited = set()

        # loop through the graph as long as the queue is not empty
        while q.size() > 0:
            # dequeue the next item from the queue and set it to the path
            path = q.dequeue()
            # Set vertex the last item in the path
            vertex = path[-1]
            # check if vertex is contained in visited node
            if vertex not in visited:
                # if vertex is not contained in visited node the check it against the destination_vertex
                if vertex == destination_vertex:
                    # if these values are the same then the search ends and return the path to the destination_vertex
                    return path
                # if vertex does not equal destination_vertex then add it to visited
                visited.add(vertex)
                # loop through each edge
                for next_vertex in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vertex)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Instantiate an empty stack and then push the starting_vertex onto it
        s = Stack()
        # push a list initialized with the starting_vertex and this will hold the path
        s.push([starting_vertex])
        # Create a node to track the nodes visited in the graph
        visited = set()

        # loop through the graph as long as the stack is not empty
        while s.size() > 0:
            # pop the top item from the stack and set it to the path
            path = s.pop()
            # Set vertex the last item in the path
            vertex = path[-1]
            # check if vertex is contained in visited node
            if vertex not in visited:
                # if vertex is not contained in visited node the check it against the destination_vertex
                if vertex == destination_vertex:
                    # if these values are the same then the search ends and return the path to the destination_vertex
                    return path
                # if vertex does not equal destination_vertex then add it to visited
                visited.add(vertex)
                # loop through each edge
                for next_vertex in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vertex)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

"""
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('1', '0')
graph.add_edge('0', '3')
graph.add_edge('3', '0')
print(graph.vertices)
"""


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
