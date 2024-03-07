# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from solver import Solver
from grid import Grid
from graph import Graph

class Test_Solver(unittest.TestCase): # La sol naïve fait aussi les swaps d'elle même donc on teste 2 paramètres
    def test_g1_naif(self):
        s = Solver()
        grid = Grid.grid_from_file("input/grid1.in")
        lis = s.get_sol_naive(grid)
        self.assertEqual((grid.state, lis), ([[1,2],[3,4],[5,6],[7,8]], [((3,1),(3,0))])) 

'''class Test_Solver(unittest.TestCase): # La sol naïve fait aussi les swaps d'elle même donc on teste 2 paramètres
    def test_g2_naif(self):
        s = Solver()
        grid = Grid.grid_from_file("input/grid2.in")
        lis = s.get_sol_naive(grid)
        self.assertEqual((grid.state, lis), ([[1,2],[3,4],[5,6],[7,8]], [((3,1),(3,0))])) 

class Test_Solver(unittest.TestCase): # La sol naïve fait aussi les swaps d'elle même donc on teste 2 paramètres
    def test_g3_naif(self):
        s = Solver()
        grid = Grid.grid_from_file("input/grid3.in")
        lis = s.get_sol_naive(grid)
        self.assertEqual((grid.state, lis), ([[1,2],[3,4],[5,6],[7,8]], [((3,1),(3,0))])) 

class Test_Solver(unittest.TestCase): # La sol naïve fait aussi les swaps d'elle même donc on teste 2 paramètres
    def test_g4_naif(self):
        s = Solver()
        grid = Grid.grid_from_file("input/grid4.in")
        lis = s.get_sol_naive(grid)
        self.assertEqual((grid.state, lis), ([[1,2],[3,4],[5,6],[7,8]], [((3,1),(3,0))])) 

if __name__ == '__main__':
    unittest.main()

class Test_Solver(unittest.TestCase):
    def test_sol2(self):
        G = Grid(2,2,[[1,2],[3,4]])
        graph = G.graph_from_grid()
        self.assertEqual(graph.nb_nodes, 24) # Tester qu'on a bien créé tous les sommets (4! = 24 états de la grid possible)
        self.assertEqual(graph.nb_edges, 96) # Chaque sommet a 4 arêtes ici

class Test_Solver(unittest.TestCase):
    def test_sol_bfs(self):
        grid = Grid(2,2,[[1,3],[2,4]])
        g = Graph([])
        src, dst = grid.path_to_do()
        path = g.bfs_generate_graph(src,dst,2,2)
        swap_list = g.path_to_swap(path,2,2)
        grid.swap_seq(swap_list)
        self.assertEqual(grid.state, [[1,2],[3,4]])'''