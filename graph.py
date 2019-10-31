"""
Implement connected_components.
Implement mst_prim.
"""
from utils import (
    np,
    infinity,
    argmin,
    PriorityQueue,
    distance

)
import pickle


class Graph:

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed

        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """Make a digraph into an undirected graph by adding symmetric edges."""
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)

    def connect(self, A, B, distance=1):
        """Add a link from A and B of given distance, and also add the inverse
        link if the graph is undirected."""
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)

    def connect1(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.graph_dict.setdefault(a, {})

        if b is None:
            return links
        return links.get(b)  # else

    def nodes(self):
        """Return a list of nodes in the graph."""
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values()
                  for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

    def edges(self, unique=False):
        """Return a list of edges in the graph."""
        edges = []
        for node in self.nodes():
            for neighbor in self.get(node):
                if (neighbor, node) not in edges:
                    edges.append((node, neighbor))
        return edges

    def unique_edges(self):
        """Return a list of edges in one direction only."""
        return self.edges(unique=True)

    def save_graph(self, filename):
        """Save the graph object in the filename."""
        with open(filename + '.pickle','wb') as handle:
            pickle.dump(self, handle)


def SavedGraph(filename):
    """Return a graph object stored in the filename."""
    with open(filename + '.pickle','rb') as handle:
        return pickle.load(handle)


def UndirectedGraph(graph_dict=None):
    """Build a Graph where every edge (including future ones) goes both ways."""
    return Graph(graph_dict=graph_dict, directed=False)


def RandomGraph(nodes=list(np.arange(10)), min_links=2, width=400, height=300,
                curvature=lambda: np.random.uniform(1.1, 1.5)):
    """Construct a random graph, with the specified nodes, and random links.
    The nodes are laid out randomly on a (width x height) rectangle.
    Then each node is connected to the min_links nearest neighbors.
    Because inverse links are added, some nodes will have more connections.
    The distance between nodes is the hypotenuse times curvature(),
    where curvature() defaults to a random number between 1.1 and 1.5."""
    g = UndirectedGraph()
    g.locations = {}
    # Build the nodes
    for node in nodes:
        g.locations[node] = (np.random.randint(
            width), np.random.randint(height))
    # Build edges from each node to at least min_links nearest neighbors.
    for _ in range(min_links):
        for node in nodes:
            if len(g.get(node)) < min_links:
                here = g.locations[node]

                def distance_to_node(n):
                    if n is node or g.get(node, n):
                        return infinity
                    return distance(g.locations[n], here)

                neighbor = argmin(nodes, key=distance_to_node)
                d = distance(g.locations[neighbor], here) * curvature()
                g.connect(node, neighbor, int(d))
    return g


def ConnectedGraph(nodes=list(np.arange(10)), min_links=2, width=400, height=300,
                   curvature=lambda: np.random.uniform(1.1, 1.5)):
    """Construct a random connected graph."""
    g = RandomGraph(nodes, min_links, width, height, curvature)
    c_cs = connected_components(g)
    for i in range(len(c_cs)-1):
        # Pick two random node from different components
        # and then connect them
        g.connect(np.random.choice(c_cs[i]), np.random.choice(c_cs[i+1]))
    return g


def connected_components(graph):
    """Return the connected components in a graph.
    Implemented by DFS."""
    visited = set()

    def depth_first_search(v):
        vs = set([v])
        component = []
        while vs:
            v = vs.pop()
            visited.add(v)
            vs |= set(graph.get(v)) - visited
            component.append(v)
        return component
    components = []
    for v in graph.nodes():
        if v not in visited:
            d = depth_first_search(v)
            components.append(d)
    return components


def mst_prim(graph, r):
    """The MST PRIM algorithm implementation based on PriorityQueue """
    frontier = PriorityQueue('min')
    frontier.fill([v for v in graph.nodes()], infinity)
    frontier.update(r, 0)

    precedessor = {v: None for v in graph.nodes()}
    # it's more similar to the [CLRS] pseudocode
    weight = graph.get

    while frontier:
        node = frontier.pop()
        for neighbor in graph.get(node):
            if neighbor in frontier and weight(node, neighbor) < frontier[neighbor]:
                precedessor[neighbor] = node
                frontier.update(neighbor, weight(node, neighbor))
    return precedessor
