from tkinter import W
from igraph import *
import pandas as pd
from random import *

def gen_graph(n: int) -> list:
    l = [] #Lista de listas que representan el grafo en forma de la matriz dispersa, nodoA||nodoB||peso
    lp = []#||Lista para evitar arístas múltiples
    v = list(range(15,n+16))
    root = choice(v)
    v.remove(root)
    pred = [root]

    while len(v) != 0: #Se genera un grafo conexo con n-1 aristas
        #print("while 1")
        #print(v)
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
        #print("while 2: ")
        #print(len(l))
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
        #print(n)
        t = gen_graph(n)
        #t = Conex_graph_generator(n)
        graph2csv(t)
    else:
        a = input('Porfavor ingrese el nombre del archivo de donde se generara el grafo')
        b = a + '.csv'
        t = import_graph(b)
    #No entendi com funciona esto del layout
    g = Graph.TupleList(t, weights=True)
    g.vs["label"] = g.vs["name"]
    g.es["label"] = g.es["weight"]
    #print(list(g.es))
    layout = g.layout("kk")
    #plot(g, layout=layout)


#main()
