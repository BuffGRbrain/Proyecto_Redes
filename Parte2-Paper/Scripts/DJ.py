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

#Input: G graph from iGraph, u an origin node and some boolean parameters that idk.
#Output: l a list of lists that represent the graph using the sparse matrix nodeA||nodeB||weight where A and B are adjacent nodes.

def Dijkstra(G, u, affected_nodes = True, old_S = True, old_L = True):
    global iteraciones
    if old_S:
        L = {i: [float('inf'), []] for i in G.vs["name"]} #Initializes all distances from u to any node in infinite.
        L[str(u)] = [0, []] #Changes value of distance from u to u to 0.
        S = [str(u)] #Now we append u to the list of checked nodes.
    else:
        for node in old_S:
            if node in affected_nodes:
                    S = old_S[0:int(old_S.index(node)+1)]  #IDFK No fucking idea whats happening here but this is for the dynamic case.
                    L = {i: L[i] for i in S}
    start = 1
    while 1:
        L_S = {i: L[i][0] for i in L if i not in S} #Append to L_S all the nodes in L that have not been checked.
        if not L_S: #If all nodes have been checked, it breaks, if not it continues.
            break 
        if start: #If we are in the first node, we asign u to x. 
            x = u #x will be the node whose edges will be checked.
            start = 0 #Changing start to 0 because we will no longer be in the first node.
        else:
            x = min(L_S, key=L_S.get) #Minimum of the weights
            S.append(x)

        for v in G.vs["name"]: #For all the nodes in G.
            iteraciones +=1
            if v not in S: #If v hasn't been checked.
                if L[str(v)][0] > L[str(x)][0] + w(G, str(x), str(v)) and L[str(v)][0]!= float('inf') and L[str(x)][0] != float('inf'): #Mirar el caso de nodos no conectados al origen.
                    L[str(v)][1].append(str(x))
                    #L[str(v)] = [L[str(x)][0] + w(G, str(x), str(v)), L[str(v)][1]]#Updates weight of the edge and adds the route
                    L[str(v)][0] = L[str(x)][0] + w(G, str(x), str(v))
    return L,S

def actualizar_Dijkstra():
    pass

def compareGraph():
    pass
