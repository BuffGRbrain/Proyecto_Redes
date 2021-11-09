from igraph import *
import pandas as pd
from random import randint

def vecinos(graph, node: int) ->list:
    vecindad = []
    for i in graph:
        if i[0] == node:
            vecindad.append(i[1])
        elif i[1] == node:
            vecindad.append(i[0])
    print(node)
    print(vecindad)
    return vecindad

def DFS(graph, visitados: list,  node: int) ->list:
    if node not in visitados:
        visitados.append(node)
        print(node)
        for i in vecinos(graph, node):
            DFS(graph, visitados,i)
            #print("visitados")
            #print(visitados)
        return visitados
    return visitados

def is_conexo(graph,v: list):
    visitados = []
    connected_nodes = DFS(graph,visitados,(graph[1])[1])
    if connected_nodes == v:
        print("IM CONECTED MFFFFFF")
        return True
    else:
        print("fuuuck otro que no es conexo")
        return False

def gen_graph(n: int) -> list:
    l = [] #Lista de listas que representan el grafo en forma de la matriz dispersa, nodoA||nodoB||peso
    lp = []#||Lista para evitar arístas múltiples
    v = []
    a = True
    for i in range(int(n+n/2)):
        while True:#pensar como optimizar esto pues lo hace hasta que encuentra uno que pueda agregar
            n1 = randint(15, 50)
            n2 = randint(15, 50)
            tp = [n1, n2]
            tp.sort() #como ya metimos n1.n2 no queremos que este n2.n1 pues sería una arísta múltiple
            t = [n1, n2, randint(1, 15)]
            if a == True and n1 != n2 and tp not in lp:
                l.append(t)
                lp.append(tp)
                a == False
                break
            if n1 != n2 and tp not in lp and n1 or n2 in v: #Los numeros deben ser diferentes para evitar bucles creo que el and sobra
                l.append(t)
                lp.append(tp)
                v.append(n1)
                v.append(n2)
                break
    return (l,v)

def Conex_graph_generator(n: int): #Genera el grafo hasta que sea conexo
    vert = []
    while True:
        (graph, vert)  = gen_graph(n)
        if is_conexo(graph, vert) == True:
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
        n = randint(15, 50)
        print(n)
        t = Conex_graph_generator(n)
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
