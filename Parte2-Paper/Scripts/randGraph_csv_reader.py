#from igraph import *
import igraph
import pandas as pd
from random import randint

def vecinos(graph: df, node: int) ->list:
    vecindad = []
    for i in graph:
        if i[1] == node or i[2] == node:
            vecindad.append(i)
    return vecindad

def DFS(graph: df, revisados: list,  node: int) ->list: #Esta funci[on me suena raro  creo que deberia modificarla como return y la funcion como debe ser una recursvisa
    if node not in visitados:
        visitados.append(node)
        for i in vecinos(graph, node):
            DFS(graph, revisados,i)
    return visitados

def is_conexo(graph: df,v: list):
    visitados = []
    connected_nodes = DFS(graph,visitados,graph[1][1])
    if connected_nodes == v:
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
            #Se me ocurre que si uno de los dos a agregar ya estaentonces agreguelos
            if a == True and n1 != n2 and tp not in lp:
                l.append(t)
                lp.append(tp)
                a == False
                break
            if n1 != n2 and tp not in lp and n1 or n2 in v: #Los numeros deben ser diferentes para evitar bucles
                l.append(t)
                lp.append(tp)
                v.append(n1,n2)
                break
    return l

def Conex_graph_generator(n: int): #Genera el grafo hasta que sea conexo
    while True:
        graph = gen_graph(n)
        if is_conexo(gen_graph(n)) == True:
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
