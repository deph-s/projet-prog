# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph

g = Graph([1,2,3,4,5,6,7]) # Création d'un graph de test
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,4)
g.add_edge(3,5)
g.add_edge(3,7)
g.add_edge(6,7)

class Test_Shortest_Path(unittest.TestCase):
    def test1(self):
        path = g.bfs(1,6)
        self.assertEqual(path, [1,3,7,6])

if __name__ == '__main__':
    unittest.main()
