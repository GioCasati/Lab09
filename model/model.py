import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._all_nodes = set()
        self._all_edges = []

    def _build_graph(self, minimum_mean_distance):
        airports = DAO.getAllAirports()
        airportsMap = {}
        for airport in airports:
            airportsMap[airport.ID] = airport
        routes = DAO.getAllRotte()
        for route in routes:
            if route.a1 in airportsMap and route.a2 in airportsMap and route.avgDistance > minimum_mean_distance:
                self._all_nodes.add(airportsMap[route.a1])
                self._all_nodes.add(airportsMap[route.a2])
                self._all_edges.append(route)
                self._graph.add_edge(airportsMap[route.a1], airportsMap[route.a2], weight= route.avgDistance)
        return len(self._graph.nodes), len(self._graph.edges)

    def _get_graph_edges(self):
        return self._graph.edges(data=True)