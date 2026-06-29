import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._allRating=DAO.getAllRating()
        self._allActor=DAO.getAllActor()
        self._idMapActor = {}
        for a in self._allActor:
            self._idMapActor[a.id] = a
        self._graph = nx.Graph()


    def buildGraphPesato(self,minimo,massimo):
        self._graph.clear()
        nodes = DAO.getAllNodes(minimo,massimo,self._idMapActor)
        self._graph.add_nodes_from(nodes)
        self.addEdges()


    def addEdges(self):
        allActor = DAO.getAllEdgesv1(self._idMapActor)
        for a in allActor:
            if a.id in self._graph and a.id2 in self._graph:
                self._graph.add_edge(a.id, a.id2, weight=a.peso)


    def getAllRating(self):
        return self._allRating







    def getNumNodi(self):
        return len(self._graph.nodes)
    def getNumArchi(self):
        return len(self._graph.edges)
