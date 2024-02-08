import math
from grid import Grid
from graph import Graph, bfs

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def get_sol_naive(self,grid):
        N = 1  # Chiffre que l'on cherche à bien ranger
        l = [] # Liste à laquelle on va ajouter les swaps au fur et à mesure 
        m, n = grid.m, grid.n
        while(not(grid.is_sorted())):
            x1f = math.ceil(N/n)-1  # Calcule les coordonnées dans la grid ou notre dalle N doit finir 
            if(N % n == 0):
                x2f = n-1
            else:
                x2f = (N % n) - 1
            for i in range(m):      # Boucle qui place au bon endroit
                for j in range(n):
                    if grid.state[i][j] == N:
                        x1 = i
                        x2 = j
                        while x1 != x1f:
                            if x1 < x1f:
                                grid.swap((x1,x2),(x1+1,x2))
                                l.append(((x1,x2),(x1+1,x2)))
                                x1 +=1
                            if x1 > x1f:
                                grid.swap((x1,x2),(x1-1,x2))
                                l.append(((x1,x2),(x1-1,x2)))
                                x1 -=1
                        while x2 != x2f:
                            if x2 < x2f:
                                self.swap((x1,x2),(x1,x2+1))
                                l.append(((x1,x2),(x1,x2+1)))
                                x2 +=1
                            if x2 > x2f:
                                self.swap((x1,x2),(x1,x2-1))
                                l.append(((x1,x2),(x1,x2-1)))
                                x2 -=1
            N += 1 # Incrémenter N une fois qu'on a bien rangé la dalle en questions
        return l

        """ Complexité de la solution naïve : 

        Dans le pire des cas, il faut faire une boucle sur tout n <= N soit m*n itérations, à chaque itération, boucles for
        donc aussi une complexité de m*n, si N est le plus éloigné possible il faut le monter m fois et le décaler n fois soit 
        m+n opérations en temps constant donc complexité en O(m*n*m*n*(m+n)) = O((m*n)²(m+n))
        
        
        """
    def get_solution_not_opti(self,grid): # Aucun test de la fonction pour l'instant TODO 
        src, dst = grid.path_to_do() 
        state_graph = grid.graph_from_grid()
        path = state_graph.bfs(src,dst)
        return path

    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

