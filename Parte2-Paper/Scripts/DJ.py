from igraph import *
from routing import RBNode,RBTree

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
def get_path(L, u, z, r=[]):
    lz = L[z][1]
    r.append(lz[-1])
    if u in r:
        return r
    return get_path(L, u, lz[-1], r)


def w(G, x, v):
    try:
        return G.es[G.get_eid(x, v)]["weight"]
    except:
        return float('inf')


def full_graph_path(G, u, L):
    l = list(G.vs['name'])
    print(L)
    l.remove(u)
    for i in l:
        path = get_path(L, u, i, [])
        path = path[::-1]
        path.append(i)
        if L[i][0] == float('inf'):
            path = []
        print(f'{u} -- {i}: {path} w = {L[i][0]}')


def Dijkstra(G, u, affected_nodes = True, old_S = True, old_L = True):
    # Comprobar cuál es la arista que afecta primero el Dijkstra anterior
    if old_S:
        L = {i: [float('inf'), []] for i in G.vs["name"]}
        L[u] = [0, []]
        S = [u]
    else:
        for node in old_S:
            if node in affected_nodes:
                    S = old_S[0:int(old_S.index(node)+1)]
                    L = {i: L[i] for i in S}
    #arbol = RB.Tree()
    while 1:
        L_S = {i: L[i][0] for i in L if i not in S}
        print(L_S)
        print(L)
        if not L_S:
            break
        x = min(L_S, key=L_S.get)
        S.append(x)

        for v in G.vs["name"]:
            # print(v)
            if v not in S:
                if L[v][0] >= L[x][0] + w(G, x, v):
                    L[v][1].append(x)
                    L[v] = [L[x][0] + w(G, x, v), L[v][1]]
    full_graph_path(G, u, L)
    return L,S

def actualizar_Dijkstra():
    pass

def compareGraph():
    pass

t = [[21, 18, 11], [21, 24, 8], [18, 28, 12], [28, 29, 4], [29, 25, 12], [24, 20, 11], [20, 30, 4], [29, 16, 11], [21, 27, 11], [16, 22, 8], [25, 26, 13], [28, 15, 12], [28, 19, 8], [27, 23, 10], [19, 17, 7], [19, 18, 2], [22, 29, 13], [29, 26, 12], [19, 24, 14], [20, 25, 1], [16, 25, 14], [17, 26, 14]]
g = Graph.TupleList(t, weights=True)
L,S = Dijkstra(g,21)
#full_graph_path(g,21,L)
#print(tree)
