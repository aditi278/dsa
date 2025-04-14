class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for source, destination in self.edges:
            if source not in self.graph_dict.keys():
                self.graph_dict[source] = [destination]
            else:
                self.graph_dict[source].append(destination)

    def get_paths(self, source, destination, path=[]):
        path = path + [source]
        if source == destination:
            return [path]
        if source not in self.graph_dict.keys():
            return []

        paths = []
        for node in self.graph_dict[source]:
            if node not in path:
                remainingPaths = self.get_paths(node, destination, path)
                for p in remainingPaths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, source, destination, path=[]):
        path = path + [source]
        if source == destination:
            return path
        if source not in self.graph_dict.keys():
            return None

        shortest_path = None
        for node in self.graph_dict[source]:
            if node not in path:
                remainingPath = self.get_shortest_path(node, destination, path)
                if remainingPath:
                    if shortest_path is None or len(shortest_path) > len(remainingPath):
                        shortest_path = remainingPath
        return shortest_path

if __name__ == "__main__":
    routes = {
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    }

    route_graph = Graph(routes)
    print(route_graph.graph_dict)
    print(route_graph.get_paths("Mumbai", "New York"))
    print(route_graph.get_shortest_path("Mumbai", "New York"))
