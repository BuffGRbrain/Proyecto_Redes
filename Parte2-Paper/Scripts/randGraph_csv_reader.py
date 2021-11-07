from igraph import *
import pandas as pd
from random import randint


def gen_graph(n: int) -> list:
    l = [] #Lista de listas que representan el grafo en forma de la matriz dispersa, nodoA||nodoB||peso
    lp = []#||Lista para evitar arístas múltiples
    for i in range(int(n+n/2)):
        while True:#pensar como optimizar esto pues lo hace hasta que encuentra uno que pueda agregar
            n1 = randint(15, 50)
            n2 = randint(15, 50)
            tp = [n1, n2]
            tp.sort() #como ya metimos n1.n2 no queremos que este n2.n1 pues sería una arísta múltiple
            t = [n1, n2, randint(1, 15)]
            #Se me ocurre
            if n1 != n2 and tp not in lp: #Los numeros deben ser diferentes para evitar bucles
                l.append(t)
                lp.append(tp)
                break
    return l


def graph2csv(t) -> None: #Saca el grafo creado en un csv
    df = pd.DataFrame(t)
    df = df.set_axis(['Node A', 'Node B', 'Cost'], axis=1, inplace=False)
    df.to_csv('graph.csv', index=False)


def import_graph(name='graph.csv'):#A partir de un csv crea el grafo
    df = pd.read_csv(name)
    return df.values.tolist()


def main():
    if int(input('0 - Cargar Grafo \n1 - Generar Grafo \n Seleccion: ')):
        n = randint(15, 50)
        t = gen_graph(n)
        graph2csv(t)
    else:
        t = import_graph()
    #No entendi com funciona esto del layout
    g = Graph.TupleList(t, weights=True)
    g.vs["label"] = g.vs["name"]
    g.es["label"] = g.es["weight"]

    layout = g.layout("kk")
    plot(g, layout=layout)


main()
