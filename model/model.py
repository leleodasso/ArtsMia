import networkx as nx

from database.DAO import DAO


class Model:


    def __init__(self):
        self.grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self):
        # nodi
        listaNodi = DAO.getAllObjects()
        self.grafo.add_nodes_from(listaNodi)
        print(len(listaNodi))

        # mappa
        for nodo in listaNodi:
            print(f"fsdghsdiughsguihdgo ____ {nodo.object_id}")
            self._idMap[nodo.object_id] = nodo

        # archi
        listaArchi = DAO.getAllEdges(self._idMap)
        for arco in listaArchi:
            self.grafo.add_edge(arco[0], arco[1], weight=arco[2])


    def getNumeriGrafo(self):
            return self.grafo.number_of_nodes(), self.grafo.number_of_edges()

    def getCompConn(self, obj):
        return list(nx.node_connected_component(self.grafo, self._idMap[int(obj)]))