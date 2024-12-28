import heapq
import networkx as nx
import matplotlib.pyplot as plt

class TransportGraph:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}

    def add_route(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, source, target):
        dist = {i: float('inf') for i in range(len(self.graph))}
        dist[source] = 0
        prev = {i: None for i in range(len(self.graph))}
        pq = [(0, source)]

        while pq:
            current_dist, current_node = heapq.heappop(pq)
            if current_node == target: break
            for neighbor, weight in self.graph[current_node]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor], prev[neighbor] = distance, current_node
                    heapq.heappush(pq, (distance, neighbor))

        path, current_node = [], target
        while current_node is not None:
            path.insert(0, current_node)
            current_node = prev[current_node]
        return path, dist[target]

def visualize_graph(graph, path=None):
    G = nx.Graph()
    for node in graph.graph:
        for neighbor, weight in graph.graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    if path:
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')
    plt.title("Graph with Shortest Path")
    plt.show()

if __name__ == "__main__":
    graph = TransportGraph(8)
    routes = [(0, 1, 10), (1, 2, 20), (2, 3, 15), (0, 4, 5), (4, 5, 2), (5, 6, 3), (6, 7, 7), (2, 5, 6), (3, 7, 8)]
    for u, v, w in routes: graph.add_route(u, v, w)

    station_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    print("Stations:", ", ".join(station_names))

    source = int(input("Enter the source bus station (0-A, 1-B, ...): "))
    target = int(input("Enter the destination bus station (0-A, 1-B, ...): "))

    path, travel_time = graph.dijkstra(source, target)
    if path:
        print(f"Shortest path: {' -> '.join(station_names[node] for node in path)} with travel time {travel_time} minutes.")
        visualize_graph(graph, path)
    else:
        print(f"No route found from station {station_names[source]} to station {station_names[target]}.")
