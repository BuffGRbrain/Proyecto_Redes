from igraph import *



iteraciones = 0



#This function request an L graph in dictionary format in which the keys are the node name, and the values are a list with the
#weight and destiny node of the edge. This function finds a path between u and z.

def get_path(L, u, z, r=[]):
    global iteraciones
    iteraciones +=1
    
    
    lz = L[z][1] #It selects the first edge of the destiny node.
    r.append(lz[-1]) #Here it appends the previous node of the destiny node.
    if u in r:
        return r #It ends if the origin node enters in the list of the route edges. Returns the path from z to u.
    return get_path(L, u, lz[-1], r) #If the origin node isn't in r, the procedure repeats with the obtained node.


#This function asks for a graph G in iGraph normal format and 2 nodes with and edge between them (adjacent). 
#This finds the weight of the edge between the nodes.

def w(G, x, v):
    try:
        return G.es[G.get_eid(x, v)]["weight"] #If an edge exists between the nodes this finds the weight of it.
    except:
        return float('inf') #If there is no edge exists between the nodes this returns infinite.


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

#Input:G graph from igraph, u a node in L and L is a list of lists each one with the node and its connected edges.
#Output: Path from U to each node in the graph using the function get_path.

def list_graph_path(G, u, L):
    all_paths={}
    l = list(G.vs['name']) #List in which we have all the nodes of the graph.
    l.remove(str(u)) #Delete the initial node from the nodes to check.
    for i in l:
        global iteraciones
        iteraciones +=1
        path = get_path(L, str(u), str(i), []) #Find paths from u to all the nodes with get_path.
        path = path[::-1] #It inverse the path, this because geth_path returns the route list backwards.
        path.append(i) #Appends the destiny node to the list because get_path makes the list without him.
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
    start = 1
    while 1:
        L_S = {i: L[i][0] for i in L if i not in S}
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
