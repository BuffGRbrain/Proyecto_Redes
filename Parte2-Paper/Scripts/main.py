#!/usr/bin/python3
from tokenize import Double
from matplotlib.pyplot import plot
from igraph import *
from functools import cache
from DJ import Dijkstra, get_path, list_graph_path,iteraciones
import time
import json
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

#Input: G graph from igraph, n time sleep till the next change, changes int number of random updates in the graph
#Output: None in python. 
def loop_update(G:Graph, n:Double, changes:int)->None:
    global iteraciones
    iteraciones +=1
    a = random.sample(G.vs['name'], 1) #Picks a random node in the graph
    old_L, old_S = Dijkstra(G,a[0]) #First dijkstra to know the state of the graph
    print_route_tables(G,old_L,a[0])
    count = 0
    while count<changes:#Here the graph is updated and the routing tables are recalculeted
        iteraciones += 1
        G, old, new = update_graph(G) #Changes the weights on some of the edges of the graph and saves the old and the new weights.
        #From here we detect the changes on the graph and make the correspondent calculations
        indices_diferencias = [i for i in range(len(old)) if old[i]!=new[i]] #Compare the old and the new weights to find the indices of the weights that changed and using this, we can find what edges changed
        #edges = [G.es[i] for i in indices_diferencias] #Para tener las aristas que se cambiaron
        #print(edges) #Esto debe imprimir objetos de igraph
        #Now we use the indices to find the correspondent edges and with them we save both of the nodes connected to that edge to the a set to know whitch vertices route should be recalculated
        vertices_afectados = set({})
        for i in indices_diferencias:#Finding the vertices that where affected
            iteraciones += 1
            vertices_afectados.add(G.es[i].source)
            vertices_afectados.add(G.es[i].target)

        print('-----------------')
        #show_weihtges(G)
        #u = input('Nombre del nodo 1: ')
        #v = input('Nombre del nodo 2: ')
        # a = [u, v]
        old_L, old_S = Dijkstra(G, a[0],vertices_afectados,old_L,old_S) #Uses DIjkstra but keeping the past calculations that where not affected by the update. Only recalculating on the affected vertices.
        count +=1 #Another recalculation was made
        print_route_tables(G,old_L,a[0],count)
        time.sleep(n)#Sleep time till next update/change in the graph

#Input: g graph in igraph format, L a list of lists that represent the graph using the sparse matrix nodeA||nodeB||weight where A and B are adjacent nodes, u name of a node of the graph
#and count a str to know in which table the data goes? check
#Output: None in python, but it shows the routing tables in the console.

def print_route_tables(g,L,u,count='inicial'): 
    global iteraciones
    grafo = g
    print(f"--- Tabla de enrutamiento {count}-----")
    print("|Origen| Destino | Remitir paquete a | Peso| ")
    all_paths = list_graph_path(grafo,u,L) #paths from u to all nodes in a dictionary.
    for path in all_paths: #For each node in the graph different from u.
        iteraciones += 1
        print(f"|{u}    |{path}       |         {all_paths[path][0][1]}        |  {all_paths[path][1]} |") #The last two elements of this print are: the first node in the path from  u to z and second is the total weight of that path.
    al = list(all_paths.values()) #Lists of lists with each list containing the path from u to z in a list and the total weight of the path.
    paths = [i[0] for i in al] #A list of lists with each list having a path from u to any node in the graph
    ##Creates png of the route in a reduced graph
    AU = []
    for i in paths:
        for j in range(len(i)-1): #Taking the nodes of each route
            iteraciones += 1
            AU.append(grafo.get_eid(str(i[j]), str(i[j+1]))) #Toma cada ruta y va agregando a AU los ids de las aristas que se usan en cada ruta.
    AU = list(set(AU)) #Eliminan ids repetidos.
    AU = [grafo.es[i] for i in AU] #Using the id we get the object edge from igraph
    NU = [i for i in grafo.es if i not in AU]
    grafo.delete_edges(NU)
    ##Creates png of the route in a reduced graph
    layout = grafo.layout("kk")
    g.vs["label"] = g.vs["name"]
    g.es["label"] = g.es["weight"]
    plot(grafo, layout=layout,target= f"Este es el camino más corto en la actualización {count}.png")


def main():
    with open("config.json", 'r') as f:
        config = json.loads(f.read())

    print("Bienvenido a este algoritmo. A partir de una red y mediante el uso de grafos, se hallarán las tablas de enrutamiento dinámicamente. \n Atención: Se guardarán imágenes de los grafos y caminos calculados en la misma carpeta.")
    if bool(config["generate_graph"]):
        n = config["nodes"]
        # changes = int(input("Ingrese el número de cambios a realizar"))#Falta pasarselo al loop_update 
        t  = radngraph.gen_graph(n)
        t2 = [(str(i[0]), str(i[1]), i[2]) for i in t]
        radngraph.graph2csv(t)
    else:
        # a = input('Por favor ingrese el nombre del archivo de donde se generara el grafo(sin ".csv"): ')
        # b = a + '.csv'
        t = radngraph.import_graph(config["filename"] +".csv")
        t2 = [(str(i[0]), str(i[1]), i[2]) for i in t]

    g = Graph.TupleList(t2, weights=True)
    g.vs["label"] = g.vs["name"]
    g.es["label"] = g.es["weight"]
    layout = g.layout("kk")
    plot(g, layout=layout,target="Estado de la red inicial.png")
    loop_update(g, 2, config["changes"])
    print(f"Total iteraciones = {iteraciones}")
    print("--- %s seconds ---" % (time.time() - start_time-4*2)) #Se restan 4*2 segundos porque ese fue el tiempo de espera para cambiar la información de las aristas.

if __name__ == '__main__':
    main()
