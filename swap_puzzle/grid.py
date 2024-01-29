"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
import graph

class IllegalMove(Exception):
    pass

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        m, n = self.m, self.n
        for i in range(m):
            for j in range(n):
                if j < n-1:
                    if self.state[i][j] + 1 != self.state[i][j+1]:
                        return False
                elif i < m-1:
                    if self.state[i][j] + 1 != self.state[i+1][0]:
                        return False
        return True

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        if abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1]) == 1:  # teste si on swap bien deux cases distinctes et adjacentes
            buff = self.state[cell1[0]][cell1[1]]
            self.state[cell1[0]][cell1[1]] = self.state[cell2[0]][cell2[1]]
            self.state[cell2[0]][cell2[1]] = buff
        else:
            raise IllegalMove

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for swap in cell_pair_list:
            self.swap(swap[0],swap[1])

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid

    def id(self,l): # Injection des états de la grid dans N, représentation en base m*n+1
        m = self.m
        n = self.n
        base = m*n+1
        return sum(l[i]*(base)**i for i in range(len(l))) # Identifiant unique hashable

    def flatten(self): # Permet de convertir la grid de base en une seule list de taille m*n et de calculer ses permutations 
        l = []
        m = self.m
        for i in range(m):
            for j in self.state[i]:
                l.append(j)
        return l

    def copy(self):
        cpy_state = []
        for l in self.state:
            cpy_state.append(l.copy())
        g = Grid(self.m,self.n,cpy_state)
        return g

    def permutations(self,l):
        if len(l) <= 1:
            yield l
            return
        for perm in self.permutations(l[1:]):
            for i in range(len(l)):
                yield perm[:i] + l[0:1] + perm[i:]

    def nextperm(self,i,j): # Renvoie les grids que l'on peut obtenir en permutant la case i,j de la grid 
        swaps = []
        m,n = self.m, self.n
        if(i<n-1):
            g = self.copy()
            g.swap((i,j),(i+1,j))
            swaps.append(g.flatten())
        if(i>0):
            g = self.copy()
            g.swap((i,j),(i-1,j))
            swaps.append(g.flatten())
        if(j<m-1):
            g = self.copy()
            g.swap((i,j),(i,j+1))
            swaps.append(g.flatten())
        if(j>0):
            g = self.copy()
            g.swap((i,j),(i,j-1))
            swaps.append(g.flatten())
        l_ = [self.id(l) for l in swaps]
        return l_
        

    def adj_grids(self): # Renvoie tous les états de la grid (sous forme d'entiers) qu'on obtient à partir d'une permutation 
        allswaps = []    # depuis l'état actuel de la grid, permet de déterminer les arêtes à créer dans le graphe
        m,n = self.m, self.n
        for i in range(m):
            for j in range(n):
                s = self.nextperm(i,j)
                for p in s:
                    if p not in allswaps:
                        allswaps.append(p)
        return allswaps

    def graph_from_grid(self):
        m = self.m
        n = self
        vertex_list = self.flatten()