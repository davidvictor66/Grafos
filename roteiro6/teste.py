from Grafos.roteiro6.grafo_adj import *

g_p = Grafo([], [])
for i in range(1,7):
    g_p.adiciona_vertice('V{}'.format(i))
for i in ['V1-V2','V6-V1','V6-V3','V6-V4','V2-V3','V2-V4','V4-V3','V4-V5']:
    g_p.adiciona_aresta(i)
for i in[['V6-V1',1],['V6-V3',9],['V6-V4',4],['V1-V2',3],['V2-V3',4],['V2-V4',7],['V4-V3',1],['V4-V5',8]]:
    g_p.adiciona_peso(i[0],i[1])

g_p.adiciona_peso('V6-V9',2)
print(g_p)
print(g_p.quak())