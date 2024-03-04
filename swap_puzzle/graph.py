"""
This is the graph module. It contains a minimalistic Graph class.
"""

import heapq
import grid

class Graph:
    """
    A class representing undirected graphs as adjacency lists. 

    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [neighbor1, neighbor2, ...]
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    edges: list[tuple[NodeType, NodeType]]
        The list of all edges
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 

        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes 
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.edges = []
        
    def __str__(self):
        """
        Prints the graph as a list of neighbors for each node (one per line)
        """
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the graph with number of nodes and edges.
        """
        return f"<graph.Graph: nb_nodes={self.nb_nodes}, nb_edges={self.nb_edges}>"

    def add_edge(self, node1, node2):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 
        When adding an edge between two nodes, if one of the ones does not exist it is added to the list of nodes.

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        self.nb_edges += 1
        self.edges.append((node1, node2))

    def bfs_aux(self, src, dst): #Fonction "auxiliaire" qui fait le bfs et crée la liste prev pour reconstruire le chemin
        queue = []
        prev = [-1 for i in range(self.nb_nodes)]
        explored = [False for i in range(self.nb_nodes)] 
        explored[src-1] = True
        queue.append(src)
        while not(len(queue) == 0):
            v = queue.pop(0)
            if v == dst:
                return prev
            for n in self.graph[v]:
                if not(explored[n-1]):
                    explored[n-1] = True
                    prev[n-1] = v
                    queue.append(n)
        return []

    def get_path(self,src,dst,prev): #Fonction qui reconstruit le chemin le plus court à partir du bfs déjà effectué
        path = [dst]
        cur_node = dst-1
        while not(prev[cur_node] == -1 or prev[cur_node] == src):
            cur_node = prev[cur_node]-1
            path.append(cur_node+1)
        path.append(src)
        path.reverse()
        return path

    def bfs(self, src, dst): 
        """
        Finds a shortest path from src to dst by BFS.  

        Parameters: 
        -----------
        src: NodeType
            The source node.
        dst: NodeType
            The destination node.

        Output: 
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """ 
        prev = self.bfs_aux(src,dst)
        if prev != []:
            return self.get_path(src,dst,prev)
        else:
            print("Pas de chemin entre les deux sommets entrés")

    @classmethod
    def graph_from_file(cls, file_name):
        """
        Reads a text file and returns the graph as an object of the Graph class.

        The file should have the following format: 
            The first line of the file is 'n m'
            The next m lines have 'node1 node2'
        The nodes (node1, node2) should be named 1..n

        Parameters: 
        -----------
        file_name: str
            The name of the file

        Outputs: 
        -----------
        graph: Graph
            An object of the class Graph with the graph from file_name.
        """
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            graph = Graph(range(1, n+1))
            for _ in range(m):
                edge = list(map(int, file.readline().split()))
                if len(edge) == 2:
                    node1, node2 = edge
                    graph.add_edge(node1, node2) # will add dist=1 by default
                else:
                    raise Exception("Format incorrect")
        return graph
    
    def fact(self,n): # Pour calculer la taille maximale du graphe et la taille des listes des parents et des sommets explorés
        if n == 0:
            return 1
        else:
            return n*self.fact(n-1)

    def bfs_generate_graph(self,src,dst,m,n):
        maxsize = (m*n+1)**(m*n+1)
        g = Grid(m,n)
        queue = []
        prev = [-1 for i in range(maxsize)]
        explored = []
        explored.append(src-1)
        queue.append(src)
        while not(len(queue) == 0):
            v = queue.pop(0)
            if v == dst:
                return prev
            cur_grid = g.id_to_grid(v,m,n) # Calcul de la grid actuelle
            neighbours = cur_grid.adj_grids() # Calcul des grids voisines de la grid actuelle
            neighbours = [g.id_to_grid(v,m,n) for v in neighbours] # Rend les états voisins hashable
            for ne in neighbours:
                if not(g.id(ne.flatten()) in explored):
                    explored.append(g.id(ne.flatten()))
                    queue.append(g.id(ne.flatten()))
                    prev[g.id(ne.flatten())-1] = v
        return []

    def get_neighbours(self,v,m,n):
        g = Grid(m,n)
        cur_grid = g.id_to_grid(v,m,n) # Calcul de la grid actuelle
        neighbours = cur_grid.adj_grids() # Calcul des grids voisines de la grid actuelle
        neighbours = [(1,v) for v in neighbours] # Rend les états voisins hashable, coût de 1 entre sommets adj
        return neighbours

    def manhattan_distance(g1,g2):
        acc = 0 
        m,n = g1.m, g1.n
        for i in range(m):
            for j in range(n):
                acc += abs(g1.state[i][j] - g2.state[i][j])
        return acc

    def bfs_a_star(self,src,dst,m,n,h): # h est l'heuristique à utiliser
        open_list = [(0,src)] # Création de la liste des sommets à considérer (file de prio) avec le sommet initial (distance 0)
        prev = {}
        cost = {src: 0}
        g = Graph([])
        while(open_list):
            cur_cost, cur_node = heapq.heappop(open_list)
            if cur_node == dst:
                path = [dst]
                while cur_node in prev: # Permet de faire une boucle de manière intelligente sur le dictionnaire puisque  on va automatiquement s'arrêter quand on atteint src parce qu'il n'a pas de parent
                    cur_node = prev[cur_node]
                    path.append(cur_node)
                path.reverse()
                return path
            neighbours = g.get_neighbours(cur_node,m,n) # voisins du sommet qu'on récupère sous une forme de liste déjà hash
            for cost, ne in neighbours:
                new_cost = cost[cur_node] + cost
                if ne not in cost or new_cost < cost[ne]:
                    cost[ne] = new_cost
                    h_score = new_cost + h(ne,dst)
                    heapq.heappush(open_list,(h_score,ne)) # On utilise le h_score donné par l'heuristique pour classer
                    prev[ne] = cur_node
        return None

    def path_to_swap(self,path,m,n):
        g = Grid(1,1)
        swap_list = []
        for i in range(len(path)-1):
            swap = g.findswap(path[i],path[i+1],m,n)
            swap_list.append(swap)
        return swap_list