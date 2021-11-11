from igraph import *
import pandas as pd
from random import *

def vecinos(graph, node: int) ->list:
    vecindad = []
    for i in graph:
        if i[0] == node:
            vecindad.append(i[1])
        elif i[1] == node:
            vecindad.append(i[0])
    print("Nodo" + str(node))
    print("vecindad" + str(vecindad))
    return vecindad

def DFS(graph, visitados: list,  node: int) ->list:
    if node not in visitados:
        visitados.append(node)
        print(node)
        for i in vecinos(graph, node):
            DFS(graph, visitados,i)
            print("Visitados en nodo"+str(i) + "Visitados" +str(visitados))
        visitados = eliminar_repetidos(visitados)
        return visitados
    visitados = eliminar_repetidos(visitados)
    return visitados

def is_conexo(graph,v: list):
    visitados = []
    connected_nodes = DFS(graph,visitados,(graph[0])[0])
    if connected_nodes == v:
        print("IM CONECTED MFFFFFF")
        return True
    else:
        print("Conexos"+str(connected_nodes)+"\n")
        print("Vertices"+str(v)+"\n")
        print("fuuuck otro que no es conexo")
        return False

def gen_graph(n: int) -> list:
    l = [] #Lista de listas que representan el grafo en forma de la matriz dispersa, nodoA||nodoB||peso
    lp = []#||Lista para evitar arístas múltiples
    v = list(range(15,n+16))
    root = choice(v)
    v.remove(root)
    pred = [root]

    while len(v) != 0: #Se genera un grafo conexo con n-1 aristas
        print("while 1")
        print(v)
        n1 = choice(pred)
        n2 = choice(v) # Nodo desconectado
        tp = [n1, n2]
        tp.sort() #como ya metimos n1.n2 no queremos que este n2.n1 pues sería una arísta múltiple
        t = [n1, n2, randint(1, 15)]
        if tp not in lp:
            l.append(t)
            lp.append(tp)
            pred.append(n2) #n2 ya no es un nodo desconectado
            v.remove(n2)
    while len(l) != int(n+n/2): #Este for agrega las aristas restantes
        print("while 2: ")
        print(len(l))
        n1 = choice(pred)
        n2 = choice(pred)
        tp = [n1, n2]
        tp.sort() #como ya metimos n1.n2 no queremos que este n2.n1 pues sería una arísta múltiple
        t = [n1, n2, randint(1, 15)]
        if n1 != n2 and tp not in lp and t not in l: #Ed es uno de los dos en el grafo
            l.append(t)
            lp.append(tp)

    #print("-----------------------------------------------------------------------------------------------------------")
    #print(v)
    #print("-----------------------------------------------------------------------------------------------------------")
    #v3 = eliminar_repetidos(pred)
    #print("-----------------------------------------------------------------------------------------------------------")
    #print(v3)
    #print("-----------------------------------------------------------------------------------------------------------")
    return l

def eliminar_repetidos(v: list):
    v2 = []
    for i in v:
        if i not in v2:
            v2.append(i)
    v1 = v.sort()
    print("VERTICES SIN REPETIDOS" + str(v2))
    return v2 #Debo quitar los repetidos de la lista de vertices que supongo que por DFS se aumenta not sure

def Conex_graph_generator(n: int): #Genera el grafo hasta que sea conexo
    vert = []
    while True:
        (graph, vert)  = gen_graph(n)
        vert2 = eliminar_repetidos(vert)
        if is_conexo(graph, vert2) == True:
            return graph
#-------------------------------------------GRAFO Y CSV------------------------------------------------------
def graph2csv(t) -> None: #Saca el grafo creado en un csv
    df = pd.DataFrame(t)
    df = df.set_axis(['Node A', 'Node B', 'Cost'], axis=1, inplace=False)
    df.to_csv('graph.csv', index=False)


def import_graph(name='graph.csv'):#A partir de un csv crea el grafo falta poner que el usuario meta el nombre con un input
    df = pd.read_csv(name)
    return df.values.tolist()

#-------------------------------------------GRAFO Y CSV------------------------------------------------------

def main():
    if int(input('0 - Cargar Grafo \n1 - Generar Grafo \n Seleccion: ')):
        n = randint(0, 36)
        print(n)
        t = gen_graph(n)
        graph2csv(t)
    else:
        a = input('Porfavor ingrese el nombre del archivo de donde se generara el grafo')
        b = a + '.csv'
        t = import_graph(b)
    #No entendi com funciona esto del layout
    g = Graph.TupleList(t, weights=True)
    g.vs["label"] = g.vs["name"]
    g.es["label"] = g.es["weight"]

    layout = g.layout("kk")
    plot(g, layout=layout)


main()
