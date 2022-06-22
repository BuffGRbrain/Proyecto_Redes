from igraph import *
errorss = 0
iteraciones = 0

#Input: Graph L in dictionary format, initial node u, destiny node z.
#Ouput: r a list of the nodes form the origin to the destiny node.

def get_path(L, u, z, r=[]):

    lz = L[z][1] #It selects the first edge of the destiny node.
    r.append(lz[-1]) #Here it appends the previous node of the destiny node.
    if u in r:
        return r #It ends if the origin node enters in the list of the route edges. Returns the path from z to u.
    return get_path(L, u, lz[-1], r) #If the origin node isn't in r, the procedure repeats with the obtained node.




#Input: Graph G in iGraph format, node x and node v of the graph.
#Output: The weight of the edge between these nodes.

def w(G, x, v):
    try:
        return G.es[G.get_eid(x, v)]["weight"] #If an edge exists between the nodes this finds the weight of it.
    except:
        return float('inf') #If there is no edge exists between the nodes this returns infinite.



#Input:G graph from igraph, u a node in L and L is a dictionary in which the keys are the nodes and the values are a weight and destiny node of the edge.
#Output: Path from U to each node in the graph using the function get_path in a dictionary where keys are the name of the nodes
#and the values are a list of 2 elements: 1.List of the path from u to z. 2 .Total weight of going from u to z using the given path.

def list_graph_path(G, u, L):
    all_paths={} #Dictionary with keys as the name of the node and values the path from u top that node.
    l = list(G.vs['name']) #List in which we have all the nodes of the graph.
    l.remove(str(u)) #Delete the initial node from the nodes to check.

    for i in l:
        path = get_path(L, str(u), str(i), []) #Find paths from u to all the nodes with get_path.
        path = path[::-1] #It inverse the path, this because geth_path returns the route list backwards.
        path.append(i) #Appends the destiny node to the list because get_path makes the list without him.
        # if L[i][0] == 0: #Float(inf). If the weight of the path is 0 is because there isn't any.
        #    path = []

        all_paths[i] = [path,L[i][0]] #Assign a path and a weight to their respective nodes.
    return all_paths

#Input: G graph from iGraph, u an origin node and some boolean parameters that idk.
#Output: l a list of lists that represent the graph using the sparse matrix nodeA||nodeB||weight where A and B are adjacent nodes.

def Dijkstra(G, u, affected_nodes = [], old_S = [], old_L = {}):
    #print(f"------------------------------------------dij")
    print(affected_nodes)
    print(old_S)
    global iteraciones
    global errorss
    L = {i: [float('inf'), []] for i in G.vs["name"]}  # Initializes all distances from u to any node in infinite.
    if not old_S:
        L[str(u)] = [0, []] #Changes value of distance from u to u to 0.
        S = [str(u)] #Now we append u to the list of checked nodes.
    else:
        affected_nodes = [str(i) for i in affected_nodes]

        #When we have to recalculate due to changes we use this case in which affected nodes is a set({}) of the affected nodes
        for node in old_S: #For each node in the past revision in the past dijkstra
            if node in affected_nodes:#for each affected node we make the recalculation
                    S = old_S[0:int(old_S.index(node)+1)]  #Creates the S list of checked nodes, usign slices and "cutting off" the affected nodes to be checked again
                    # L = {i: old_L[i] for i in S} #Saves the past weights that where not affected by the update in the graph, reducing calculations
                    for i in S:
                        L[i] = old_L[i]
                    break

    if 'S' in locals():
        start = 1
        while 1:
            L_S = {i: L[i][0] for i in L if i not in S} #Append to L_S all the nodes in L that have not been checked.
            #print(L_S)
            if not L_S: #If all nodes have been checked, it breaks, if not it continues.
                break 
            if start: #If we are in the first node, we asign u to x. 
                x = u #x will be the node whose edges will be checked.
                start = 0 #Changing start to 0 because we will no longer be in the first node.
            else:
                x = min(L_S, key=L_S.get) #Selects the minimum of the weights and select that node to move to him.
                S.append(x) #Indicates that this node is checked now.

            for v in G.vs["name"]: #For all the nodes in G.
                iteraciones +=1
                if v not in S: #If v hasn't been checked.
                    if L[str(v)][0] > L[str(x)][0] + w(G, str(x), str(v)): #If the weight that are in L is greater than the route for a node we replace that.
                        L[str(v)][1].append(str(x)) #If they are connected, we append in the predecessor list of v x.
                        L[str(v)][0] = L[str(x)][0] + w(G, str(x), str(v)) #Updates weight of the edge and adds the route
        return L,S

    else:
        errorss += 1
        print("Grafo picho")
        return old_L,old_S
