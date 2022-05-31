from matplotlib.pyplot import plot
from igraph import *
from functools import cache
from DJ import Dijkstra, get_path, list_graph_path,iteraciones
import time
import random
import randGraph_csv_reader as radngraph
import time


#This code requieres igraph 0.9.8

start_time = time.time() #Starts the stopwatch to see how much time it took to execute and get the desired result

#Input: G a graph from igraph
#Output: G a graph from igraph updated, old_graph_weights and new_graph_weights to see the changes CHECK
def update_graph(G):
    global iteraciones #Number of total iterations in the code till the desired ouput was obtained
    iteraciones += 1
    old_graph_weights = G.es['weight'] #Saves the old weights of the graph
    na = random.randint(0, len(G.es)) #random number  between 0 and the number of nodes the graph has
    ae = random.sample(list(G.es), na) #list->random size sample of edges of the graph 
    for i in ae: #Changes the weights randomly of the random sized sample created in ae
        i['weight'] = random.randint(0, 15) 
    new_graph_weights = G.es['weight'] #Saves the new weights of the graph
    return G, old_graph_weights, new_graph_weights

#Input: G graph from igraph, n number of nodes
#Output: None in python, 
def loop_update(G, n):#Falta criterio de parada
    global iteraciones
    iteraciones +=1
    a = random.sample(G.vs['name'], 1)
    old_L, old_S = Dijkstra(G,a[0]) #Dijkstra inicial
    print_route_tables(G,old_L,a[0])
    count = 0
    while count<3:
        iteraciones += 1
        G, old, new = update_graph(G) #
        #comparar
        indices_diferencias = [i for i in range(len(old)) if old[i]!=new[i]] #Da el indice donde los pesos son diferentes
        #edges = [G.es[i] for i in indices_diferencias] #Para tener las aristas que se cambiaron
        #print(edges) #Esto debe imprimir objetos de igraph
        vertices_afectados = set({})
        for i in indices_diferencias:#Para tener los vertices que se cambiaron
            iteraciones += 1
            vertices_afectados.add(G.es[i].source)
            vertices_afectados.add(G.es[i].target)

        print('-----------------')
        #show_weihtges(G)
        #u = input('Nombre del nodo 1: ')
        #v = input('Nombre del nodo 2: ')
        # a = [u, v]
        old_L, old_S = Dijkstra(G, a[0],vertices_afectados,old_L,old_S) #Este terecer input da los vertices afectados
        count +=1
        print_route_tables(G,old_L,a[0],count)
        time.sleep(n)

#Input:
#Output:
def print_route_tables(g,L,u,count='inicial'): 
    global iteraciones
    grafo = g
    print(f"--- Tabla de enrutamiento {count}-----")
    print("|Origen| Destino | Remitir paquete a | Peso| ")
    all_paths = list_graph_path(grafo,u,L)
    for path in all_paths:
        iteraciones += 1
        print(f"|{u}    |{path}       |         {all_paths[path][0][1]}        |  {all_paths[path][1]} |")
    al = list(all_paths.values())
    paths = [i[0] for i in al]
    AU = []
    for i in paths:
        for j in range(len(i)-1):
            iteraciones += 1
            AU.append(grafo.get_eid(str(i[j]), str(i[j+1])))
    AU = list(set(AU))
    AU = [grafo.es[i] for i in AU]
    NU = [i for i in grafo.es if i not in AU]
    grafo.delete_edges(NU)
    layout = grafo.layout("kk")
    g.vs["label"] = g.vs["name"]
    g.es["label"] = g.es["weight"]
    plot(grafo, layout=layout,target= f"Este es el camino más corto en la actualización {count}.png")

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
    print("Bienvenido a este algoritmo. A partir de una red y mediante el uso de grafos, se hallarán las tablas de enrutamiento dinámicamente. \n Atención: Se guardarán imágenes de los grafos y caminos calculados en la misma carpeta.")
    if int(input('0 - Cargar Grafo \n1 - Generar Grafo \n Seleccion: ')):
        n = int(input("Por favor ingrese el numero de nodos del grafo de 15 a 50: "))
        #print(n)
        t  = radngraph.gen_graph(n)
        t2 = [(str(i[0]), str(i[1]), i[2]) for i in t]
        #t = Conex_graph_generator(n)
        #print(t)
        radngraph.graph2csv(t)
    else:
        a = input('Por favor ingrese el nombre del archivo de donde se generara el grafo(sin ".csv"): ')
        b = a + '.csv'
        t = radngraph.import_graph(b)
        t2 = [(str(i[0]), str(i[1]), i[2]) for i in t]

    g = Graph.TupleList(t2, weights=True)
    g.vs["label"] = g.vs["name"]
    g.es["label"] = g.es["weight"]
    layout = g.layout("kk")
    plot(g, layout=layout,target="Estado de la red inicial.png")
    loop_update(g, 2)
    print(f"Total iteraciones = {iteraciones}")
    print("--- %s seconds ---" % (time.time() - start_time-4*2)) #Se restan 4*2 segundos porque ese fue el tiempo de espera para cambiar la información de las aristas.

if __name__ == '__main__':
    main()
