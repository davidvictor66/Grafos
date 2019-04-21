from Grafos.roteiro4.grafo_adj import *
import unittest

class TestGrafo(unittest.TestCase):

    def setUp(self):

        self.g_p = Grafo([], [])
        for i in range(33):
            self.g_p.adiciona_vertice('V{}'.format(i))
        for i in ['V0-V1', 'V0-V2', 'V0-V3', 'V1-V2', 'V2-V5', 'V1-V4', 'V3-V7', 'V3-V11', 'V4-V5', 'V4-V8', 'V5-V6','V5-V10',
                  'V5-V9', 'V6-V3', 'V6-V10',
                  'V7-V6', 'V8-V12', 'V9-V13', 'V10-V14', 'V10-V11', 'V11-V15', 'V12-V16', 'V13-V17', 'V14-V18','V14-V17',
                  'V14-V16', 'V15-V19', 'V15-V17',
                  'V16-V17', 'V17-V18', 'V17-V20', 'V18-V19', 'V18-V22', 'V19-V23', 'V20-V24', 'V20-V25', 'V21-V17','V22-V26',
                  'V22-V27', 'V23-V28', 'V23-V27',
                  'V25-V21', 'V25-V30', 'V28-V29', 'V29-V30', 'V30-V31', 'V30-V32', 'V31-V32']:
            self.g_p.adiciona_aresta(i)


    def test_dijkstra_drone(self):
        self.assertEqual(self.g_p.dijkstra_drone('V0', 'V32', 5, 5, ['V8', 'V17', 'V23', 'V29']),['V0', 'V3', 'V11', 'V15', 'V17', 'V20', 'V25', 'V30', 'V32'])
        self.assertEqual(self.g_p.dijkstra_drone('V0', 'V32', 3, 5, ['V8', 'V17', 'V23', 'V29']),['V0', 'V1', 'V4', 'V8', 'V12', 'V16', 'V17', 'V20', 'V25', 'V30', 'V32'])
        self.assertEqual(self.g_p.dijkstra_drone('V0', 'V32', 2, 5, ['V8', 'V17', 'V23', 'V29']),'Não é possível chegar')
        self.assertEqual(self.g_p.dijkstra_drone('V0', 'V32', 3, 3,['V8', 'V17', 'V23', 'V29'],),['V0', 'V1', 'V4', 'V8', 'V12', 'V16', 'V17', 'V18', 'V19', 'V23', 'V28', 'V29', 'V30', 'V32'])
        self.assertEqual(self.g_p.dijkstra_drone('V0', 'V32', 4, 3, ['V8', 'V17', 'V23', 'V29']), ['V0', 'V3', 'V11', 'V15', 'V17', 'V18', 'V19', 'V23', 'V28', 'V29', 'V30', 'V32'])
        self.assertEqual(self.g_p.dijkstra_drone('V0', 'V32', 3, 5, ['V10','V16','V19','V27']),['V0', 'V2', 'V5', 'V10', 'V14', 'V16', 'V17', 'V20', 'V25', 'V30', 'V32'])
        self.assertEqual(self.g_p.dijkstra_drone('V0', 'V32', 3, 3, ['V10', 'V16', 'V19', 'V27']),'Não é possível chegar')
        self.assertEqual(self.g_p.dijkstra_drone('V0', 'V32', 5, 5, ['V10', 'V16', 'V19', 'V27']),['V0', 'V3', 'V11', 'V15', 'V19', 'V23', 'V28', 'V29', 'V30', 'V32'])
        self.assertEqual(self.g_p.dijkstra_drone('V0', 'V32', 2, 5, ['V10', 'V16', 'V19', 'V27']),'Não é possível chegar')
        self.assertEqual(self.g_p.dijkstra_drone('V0', 'V32', 8, 8, ['V10', 'V16', 'V19', 'V27']),['V0', 'V3', 'V11', 'V15', 'V17', 'V20', 'V25', 'V30', 'V32'])

