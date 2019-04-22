from copy import *
from math import *

class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class MatrizInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, N=[], M=[]):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''
        for v in N:
            if not(Grafo.vertice_valido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = N

        if len(M) != len(N):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(N):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(N)):
            for j in range(len(N)):
                aresta = N[i] + Grafo.SEPARADOR_ARESTA + N[j]
                if not(self.aresta_valida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = M

    def aresta_valida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not(self.existe_vertice(aresta[:i_traco])) or not(self.existe_vertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def vertice_valido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existe_vertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.vertice_valido(vertice) and self.N.count(vertice) > 0

    def primeiro_vertice_aresta(self, a: str):
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def segundo_vertice_aresta(self, a: str):
        return a[a.index(Grafo.SEPARADOR_ARESTA)+1:]

    def indice_primeiro_vertice_aresta(self, a: str):
        return self.N.index(self.primeiro_vertice_aresta(a))

    def indice_segundo_vertice_aresta(self, a: str):
        return self.N.index(self.segundo_vertice_aresta(a))

    def existe_aresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.aresta_valida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.indice_primeiro_vertice_aresta(a)][self.indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adiciona_vertice(self, v):
        if self.vertice_valido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)
            self.M.append([])
            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0)
                self.M[self.N.index(v)].append(0)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adiciona_aresta(self, a):
        if self.aresta_valida(a):
            self.M[self.indice_primeiro_vertice_aresta(a)][self.indice_segundo_vertice_aresta(a)] += 1
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def warshall(self):
        aresta=deepcopy(self.M)
        for i in range(len(aresta)):
            for a in range(len(aresta)):
                if aresta[a][i]>0:
                    for j in range(len(aresta)):
                        if max(aresta[a][j],aresta[i][j])>0:
                         aresta[a][j]=1
        return aresta

    def dijkstra(self,inicial,final):
        vertices=self.N
        aresta=self.M
        prede={}
        peso={}
        fechado={}
        caminho=[final]
        vez=inicial
        posivel=self.warshall()
        terminou=False

        for i in range(len(vertices)): #inicializa os valores
            prede['{}'.format(vertices[i])]='null'
            peso['{}'.format(vertices[i])]=inf
            fechado['{}'.format(vertices[i])]=0
        peso['{}'.format(inicial)] = 0

        if posivel[vertices.index(inicial)][vertices.index(final)]==1: #verifica se o caminho é possível
            while terminou==False:
                for i in range(len(vertices)):
                    if vertices[i] == vez:
                        fechado['{}'.format(vertices[i])] = 1
                        menor = inf
                        chave='null'
                        for a in range(len(vertices)): #faz a estimativa dentre os vertices adjacentes
                            if aresta[i][a]>1:
                                aresta[i][a]=1
                            if aresta[i][a]==1 and peso['{}'.format(vertices[a])]>peso['{}'.format(vertices[i])]+1:
                                prede['{}'.format(vertices[a])] = vertices[i]
                                peso['{}'.format(vertices[a])] = peso['{}'.format(vertices[i])]+1
                            if aresta[i][a]==1 and peso['{}'.format(vertices[a])]<menor and fechado['{}'.format(vertices[a])]==0: #verifica qual vertice tem peso menor na adjacencia
                                menor=peso['{}'.format(vertices[a])]
                                chave=vertices[a]

                        if chave=='null': # caso não tenha caminho na adjacencia verifica qual vertice tem peso menor no grafo todo
                            for j in range(len(vertices)):
                                if peso['{}'.format(vertices[j])]<menor and fechado['{}'.format(vertices[j])]==0:
                                    menor=peso['{}'.format(vertices[j])]
                                    chave=vertices[j]
                        vez=chave

                for b in range(len(aresta)): # verifica ainda existe algum vertice aberto e diferente de infinito
                    if peso['{}'.format(vertices[b])]!=inf and fechado['{}'.format(vertices[b])]==0:
                        terminou=False
                        break
                    terminou=True

            prox=prede['{}'.format(final)]
            while True: #forma o caminho
                caminho+=[prox]
                if prox==inicial:
                    break
                prox=prede['{}'.format(prox)]
            caminho = caminho[::-1]
            return caminho,len(caminho)-1
        else:
            return "Não é possível chegar"

    def drone(self,ponto,recargas,cargaM,final): #essa função recebe como parâmetro um dos pontos de recarga e retorna o menor caminho possível até o final
        caminho=self.dijkstra(ponto,final)
        tamanho = []
        vetices = []
        distancias_final=[]
        distancias_inicial=[]
        if caminho == "Não é possível chegar":
            return 0, [ponto]
        elif caminho[1]<=cargaM:
            return caminho[1],[ponto,final]
        else:
            for a in range(len(recargas)):
                if recargas[a]!=ponto: #verifica se existe algum ponto que chegue até o final
                    if (self.dijkstra(recargas[a], final) != "Não é possível chegar" and self.dijkstra(ponto,recargas[a])!= "Não é possível chegar"):
                        distancias_final+=[self.dijkstra(recargas[a],final)[1]]
                        distancias_inicial+=[self.dijkstra(ponto,recargas[a])[1]]

            if len(distancias_inicial)>0 and len(distancias_final)>0: #se existir
                if min(distancias_final)<=cargaM and min(distancias_inicial)<=cargaM:
                    for i in range(len(recargas)): #procura outro ponto que chegue ao final
                        if recargas[i]!=ponto and i>recargas.index(ponto): #verifica se não é o mesmo ponto ou se se já verificou ele antes
                            s=self.drone(recargas[i],recargas,cargaM,final)
                            tamanho+=[s[0]+self.dijkstra(ponto,recargas[i])[1]]
                            vetices+=[s[1]]

                    for a in range(len(tamanho)):
                        if vetices[a][-1]==final: #verifica se este caminho chega até o final
                            while True:
                                if vetices[tamanho.index(min(tamanho))][-1]==final: #se for o caminho mais curto
                                    return min(tamanho), vetices[tamanho.index(min(tamanho))]
                                else: #apaga caso o caminho mais curto não chegue até o final 
                                    del vetices[tamanho.index(min(tamanho))]
                                    del tamanho[tamanho.index(min(tamanho))]
                    return min(tamanho), vetices[tamanho.index(min(tamanho))]
            return 0, [ponto]

    def dijkstra_drone(self,inicial,final,cargaI,cargaM,recarga):
        caminho=[]
        trajeto=[]
        peso=[]
        prime=[]
        if self.dijkstra(inicial,final)=="Não é possível chegar":
            return "Não é possível chegar"
        elif self.dijkstra(inicial,final)[1]<=cargaI:
            return self.dijkstra(inicial,final)[0]

        for i in range(len(recarga)):
            peso1 = self.dijkstra(inicial, recarga[i])[1]
            if peso1 <= cargaI: #se for possível chegar até este ponto
                peso+=[self.drone(recarga[i],recarga,cargaM,final)[0]+peso1] #guarda a distância desse ponto
                trajeto+=[self.drone(recarga[i],recarga,cargaM,final)[1]] #guarda os pontos de recarga que vai usar de até o final
                prime+=[recarga[i]] #guarda o primeiro ponto de recarga desse caminho

        if len(trajeto)==0:
            return "Não é possível chegar"
        for i in range(len(trajeto)): #verifica se algum caminho chega até o final
            if trajeto[i][-1]==final:
                break
            elif len(trajeto)-1==i:
                return "Não é possível chegar"
        for i in range(len(trajeto)): #adiciona o primeiro ponto de recarga no trajeto se necessário
            if trajeto[i][0]==prime[i]:
                continue
            trajeto[i].insert(0, prime[i])
        ini = inicial
        for i in trajeto[peso.index(min(peso))]: #forma o caminho
            caminho+=self.dijkstra(ini,i)[0]
            ini=i
        for a in range(len(caminho)): #verifica se existe alguma aresta repetida
            if a==len(caminho)-1:
                break
            if caminho[a]==caminho[a+1]:
                del caminho[a]
        return caminho

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' '*(self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str
