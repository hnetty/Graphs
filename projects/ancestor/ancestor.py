
from util import Queue, Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        graph.add_edge(pair[0], pair[1])

        #DFS
        q = Queue()
        q.enqueue([starting_node])

        earliest_ancestor = -1
        max_path_len = 1

        while q.size() > 0:
            path = q.dequeue()
            last_vert = path[-1]

            if (len(path) >= max_path_len and last_vert < earliest_ancestor) or len(path) > max_path_len:
                earliest_ancestor = last_vert
                max_path_len = len(path)

                for neighbor in graph.vertices[last_vert]:
                    path_copy = list(path)
                    path_copy.append(neighbor)

                    q.enqueue(path_copy)

    return earliest_ancestor