# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from solver import Solver
from grid import Grid

class Test_Solver(unittest.TestCase):
    def test_sol1(self):
        grid = Grid.grid_from_file("input/grid1.in")
        lis = Solver.get_sol_naive(grid)
        grid.swap_seq(lis)
        self.assertEqual(grid.state, [[1,2,3],[4,5,6],[7,8,9]])

if __name__ == '__main__':
    unittest.main()

G = Grid(2,2,[[1,2],[3,4]])

graph = G.graph_from_grid()
print(graph)