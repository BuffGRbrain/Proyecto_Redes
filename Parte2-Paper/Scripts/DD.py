import random


class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False

    # rotate left at node x
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)



def print_tree(node, lines, level=0):
    if node.val != 0:
        print_tree(node.left, lines, level + 1)
        lines.append('-' * 4 * level + '> ' +
                     str(node.val) + ' ' + ('r' if node.red else 'b'))
        print_tree(node.right, lines, level + 1)



#def main():
#    tree = RBTree()
#    for x in range(1, 51):
#        tree.insert(x)
#    print(tree)


#main()



def get_weight_from_list(G,v1,v2):
    try:
        return G.es[G.get_eid(v1, v2)]["weight"]
    except:
        return float('inf')

def get_path(L, pini, pfin, current_path=[]):
    lpfin = L[pfin][1]
    current_path.append(lpfin[0])
    if pini in current_path:
        return current_path
    return get_path(L, pini, lpfin[0], current_path)

def dijkstra(graph, pini, pfin):
    L = {i: [float('inf'), []] for i in graph.vs["name"]}
    L[pini] = [0, []]
    S = []

    while pfin not in S:
        vertices_not_in_S = {i: L[i][0] for i in L if i not in S}
        v_min = min(vertices_not_in_S, key=vertices_not_in_S.get)
        # S = list(set().union(S, [x]))
        S.append(v_min)
        # print(L)
        for v in graph.vs["name"]:
            # print(v)
            if v not in S:
                if L[v][0] < L[v_min][0] + get_weight_from_list(graph, v_min, v):
                    L[v] = [L[v][0], L[v][1]]
                else:
                    L[v][1].append(v_min)
                    L[v] = [L[v_min][0] +
                            get_weight_from_list(graph, v_min, v), L[v][1]]
    path = get_path(L, pini, pfin, [])
    path = path[::-1]
    path.append(pfin)
    if L[pfin][0] == float('inf'):
        path = []
    print(f"peso: {L[pfin][0]}")
    return path

def show_path(path):
    print(f'Camino desde {path[1]} hasta {path[-1]}:')
    for i in path:
        print(i, end=' --> ')


#Se podrian meter los cambios como una lista de listas en la cual las listas internas esta conformadas por una arista, el peso a el
#se actualiza y el tiempo en que lo hace.

#Falta el implementar los 2 arboles rojinegros

cambios = []
def dyn_dijkstra(graph, pini, pfin, cambios):
    t = 0
    tiempos = []
    for i in cambios:
        tiempos.append(i[3])

    L = {i: [float('inf'), []] for i in graph.vs["name"]}
    L[pini] = [0, []]
    S = []
    while t not in tiempos:
        while pfin not in S:
            vertices_not_in_S = {i: L[i][0] for i in L if i not in S}
            v_min = min(vertices_not_in_S, key=vertices_not_in_S.get)
            # S = list(set().union(S, [x]))
            S.append(v_min)
            # print(L)
            for v in graph.vs["name"]:
                # print(v)
                if v not in S:
                    if L[v][0] < L[v_min][0] + get_weight_from_list(graph, v_min, v):
                        L[v] = [L[v][0], L[v][1]]
                        t += 1
                    else:
                        L[v][1].append(v_min)
                        L[v] = [L[v_min][0] + get_weight_from_list(graph, v_min, v), L[v][1]]
                        t += 1
        path = get_path(L, pini, pfin, [])
        path = path[::-1]
        path.append(pfin)
        if L[pfin][0] == float('inf'):
            path = []
        print(f"peso: {L[pfin][0]}")
        return path

    for i in cambios:
        if i[3] == t:
            #Empezar procedimiento y cuando se llegue a exit se suma 1 a t.
            if ("no se ha calculado distancia por esa arista"):
                t += 1
            else:
                if i not in s:
                    if ("Valor viejo - valor nuevo") > 0:
                        ("Actualizar valor del vertice en la lista not S y volver a verificar cambios")

                    else:
                        t += 1
                else:
                    ("Retroceder las listas a el t anterior a que la arista pasara de not s a s y verificar cambios")                
        else:
            continue
