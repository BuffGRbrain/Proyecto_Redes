from igraph import *
from routing import RBNode,RBTree
iteraciones = 0
# def minimums(some_dict):
#    # Tomada de Stackoverflow
#    positions = []  # output variable
#    min_value = float("inf")
#    for k, v in some_dict.items():
#        if v == min_value:
#            positions.append(k)
#        if v < min_value:
#            min_value = v
#            positions = []  # output variable
#            positions.append(k)
#
#    return positions


#Esta funcion nos pide un grafo L en formato diccionario en el cual las llaves son el nombre del nodo y los valores asociados 
#son una lista con el peso y nodo de llegada de la arista. Esta funcion nos halla un camino cualquiera entre u y z.

def get_path(L, u, z, r=[]):
    global iteraciones
    iteraciones +=1
    #print(u)
    #print(z)
    lz = L[z][1] #Selecciono la primera arista de mi nodo de llegada.
    #print(L)
    #print(lz,"---")
    r.append(lz[-1]) #Aqui agrego el nodo anterior a mi nodo de llegada.
    if u in r:
        return r #Termina si el nodo de origen entra en la lista de aristas de la ruta. Retorna el camino de z a u.
    return get_path(L, u, lz[-1], r) #Si el nodo de origen aun no esta en r se repite procedimiento con el nodo obtenido.


#Esta funcion nos pide un grafo G en formato normal de iGraph y 2 nodos con arista en medio. Nos halla el peso de la arista
#entre estos nodos.

def w(G, x, v):
    #print(G.get_eid(v, x))
    #print(list(G.vs))
    try:
    #print(type(x))
        return G.es[G.get_eid(x, v)]["weight"] #Halla el peso directamente si hay una arista entre estos nodos.
    except:
        return float('inf') #Si no hay arista entre ellos entonces el peso es infinito.


"""def full_graph_path(G, u, L):
    l = list(G.vs['name'])
    #print(L)
    l.remove(str(u))
    for i in l:
        path = get_path(L, u, i, [])
        path = path[::-1]
        path.append(i)
        if L[i][0] == float('inf'):
            path = []
        #print(f'{u} -- {i}: {path} w = {L[i][0]}') """

#Nos pide un grafo G, un nodo L y el grafo en formato lista de nodos con sus aristas L y nos halla caminos hacia todos los nodos
#desde u aplicando get_path para cada uno.

def list_graph_path(G, u, L):
    all_paths={}
    l = list(G.vs['name']) #Lista en la cual tenemos los nodos del grafo.
    l.remove(str(u)) #Eliminamos el nodo de inicio de los nodos a revisar.
    for i in l:
        global iteraciones
        iteraciones +=1
        path = get_path(L, str(u), str(i), []) #Hallar caminos de u a todos los nodos con get_path.
        path = path[::-1] #Se invierte el camino al get_path retornar la lista de la ruta al reves.
        path.append(i) #Se agrega el nodo de llegada a la lista ya que get_path hace la lista sin el.
        if L[i][0] == float('inf'):
            path = []
        all_paths[i] = [path,L[i][0]]
    return all_paths

def Dijkstra(G, u, affected_nodes = True, old_S = True, old_L = True):
    # Comprobar cuál es la arista que afecta primero el Dijkstra anterior
    global iteraciones
    if old_S:
        L = {i: [float('inf'), []] for i in G.vs["name"]}
        L[str(u)] = [0, []]
        S = [str(u)]
    else:
        for node in old_S:
            if node in affected_nodes:
                    S = old_S[0:int(old_S.index(node)+1)]
                    L = {i: L[i] for i in S}
    #arbol = RB.Tree()
    start = 1
    while 1:
        L_S = {i: L[i][0] for i in L if i not in S}
        #print(L_S)
        #print(L)
        if not L_S:
            break
        if start:
            x = u
            start = 0
        else:
            x = min(L_S, key=L_S.get)
            S.append(x)

        for v in G.vs["name"]:
            iteraciones +=1
            if v not in S:
                #print("----")
                #print(type(u))
                #print(S)
                #print(v)
                #print(v not in S)
                #print("----")
                if L[str(v)][0] >= L[str(x)][0] + w(G, str(x), str(v)):
                    #print(x,v)
                    #print(w(G, str(x), str(v)))
                    L[str(v)][1].append(str(x))
                    L[str(v)] = [L[str(x)][0] + w(G, str(x), str(v)), L[str(v)][1]]
    #full_graph_path(G, u, L)
    return L,S

def actualizar_Dijkstra():
    pass

def compareGraph():
    pass
