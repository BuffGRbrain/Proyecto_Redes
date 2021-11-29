from igraph import *
from functools import cache
from DJ import Dijkstra
import time
import random
import * from randGraph_csv_reader.py

def update_graph(G):
    old_graph_weights = G.es('weight')
    na = random.randint(0, len(G.es))
    ae = random.sample(list(G.es), na)
    for i in ae:
        i['weight'] = random.randint(0, 100000)
    new_graph_weights = G.es('weight')
    return old_graph_weights, new_graph_weights

def loop_update(G, n):#Falta criterio de parada
    a = random.sample(G.vs['name'], 1)
    while 1:
        old, new = update_graph(G)
        #comparar
        indices_diferencias = [i for i in len(old)-1 if old[i]!=new[i]] #Da el indice donde los pesos son diferentes
        #edges = [G.es[i] for i in indices_diferencias] #Para tener las aristas que se cambiaron
        print(edges) #Esto debe imprimir objetos de igraph
        vertices_afectados = set({})
        for i in indices_diferencias:#Para tener los vertices que se cambiaron
            vertices_afectados.add(G.es[i].source)
            vertices_afectados.add(G.es[i].target)



        vertices_afectados2 = set(vertices_afectados)
        print('-----------------')
        show_weihtges(G)
        #u = input('Nombre del nodo 1: ')
        #v = input('Nombre del nodo 2: ')
        # a = [u, v]
        Dijkstra(G, *a,vertices_afectados) #Este terecer input da los vertices afectados
        time.sleep(n)


def show_weihtges(G):
    for i in G.es:
        source = G.vs(i.source)['name']
        target = G.vs(i.target)['name']
        weight = i['weight']
        print(f'{source} --> {target}: {weight}')

'''
def full_dijkstra(G, u):
    l = G.vs['name']
    l.remove(u)
    for i in l:
        Dijkstra(G, u, i)
'''

def main():

    # t = [('a', 'b', 0), ('a', 'c', 0), ('a', 'd', 0),
    #     ('b', 'c', 0), ('b', 'd', 0)]
    #t = [[32, 29, 2], [29, 22, 15], [32, 43, 3], [43, 45, 7], [29, 33, 7], [45, 24, 5], [33, 17, 10], [43, 38, 11], [24, 21, 9], [17, 34, 8], [22, 47, 13], [29, 15, 13], [33, 25, 10], [17, 30, 4], [24, 16, 2], [22, 28, 5], [22, 31, 15], [43, 36, 8], [34, 37, 2], [34, 23, 9], [21, 20, 13], [29, 27, 14], [33, 46, 12], [15, 18, 1], [
        #29, 35, 3], [25, 19, 9], [43, 44, 1], [47, 42, 1], [25, 41, 14], [20, 40, 15], [38, 26, 9], [46, 39, 8], [45, 18, 5], [16, 18, 1], [40, 45, 8], [41, 24, 15], [27, 46, 2], [27, 25, 7], [21, 26, 9], [40, 26, 8], [19, 46, 13], [21, 42, 3], [35, 44, 1], [30, 15, 8], [29, 34, 8], [23, 18, 15], [37, 33, 8], [31, 28, 2]]
     #Usa dijkstra y cada cierto tiempo modifica el grafo
    # gl = threading.Thread(target=loop_update_update, args=(g, 2))
    # dl = threading.Thread(target=loop_update_Dijkstra, args=(g))

    # gl.start()
    # dl.start()
    # show_weihtges(g)
    # update_graph(g)
    # print('--------')
    # show_weihtges(g)
    if int(input('0 - Cargar Grafo \n1 - Generar Grafo \n Seleccion: ')):
        n = int(input("Porfavor ingrese el numero de nodos del grafo de 15 a 50"))
        print(n)
        t  = gen_graph(n)
        t2 = [(str(i[0]), str(i[1]), i[2]) for i in t]
        g = Graph.TupleList(t2, weights=True)
        loop_update(g, 2)
        #t = Conex_graph_generator(n)
        print(t)
        graph2csv(t)
    else:
        a = input('Porfavor ingrese el nombre del archivo de donde se generara el grafo')
        b = a + '.csv'
        t = import_graph(b)
    #Visualización
    g = Graph.TupleList(t, weights=True)
    g.vs["label"] = g.vs["name"]
    g.es["label"] = g.es["weight"]

    layout = g.layout("kk")
    plot(g, layout=layout)


if __name__ == '__main__':
    main()
