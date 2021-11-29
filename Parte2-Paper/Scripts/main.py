from igraph import *
from functools import cache
from DJ import Dijkstra
import time
import random


def update_graph(G):
    
    na = random.randint(0, len(G.es))
    ae = random.sample(list(G.es), na)
    for i in ae:
        i['weight'] = random.randint(0, 100000)
    # g.es[g.get_eid('a', 'b', error=False)]['weight'] = f(t+1)


def loop_update(G, n):
    while 1:
        update_graph(G)
        print('-----------------')
        show_weihtges(G)
        a = random.sample(G.vs['name'], 1)
        #u = input('Nombre del nodo 1: ')
        #v = input('Nombre del nodo 2: ')
        # a = [u, v]
        Dijkstra(G, *a)
        time.sleep(n)


def show_weihtges(G):
    for i in G.es:
        source = G.vs(i.source)['name']
        target = G.vs(i.target)['name']
        weight = i['weight']
        print(f'{source} --> {target}: {weight}')


def full_dijkstra(G, u):
    l = G.vs['name']
    l.remove(u)
    for i in l:
        Dijkstra(G, u, i)


def main():

    # t = [('a', 'b', 0), ('a', 'c', 0), ('a', 'd', 0),
    #     ('b', 'c', 0), ('b', 'd', 0)]
    t = [[32, 29, 2], [29, 22, 15], [32, 43, 3], [43, 45, 7], [29, 33, 7], [45, 24, 5], [33, 17, 10], [43, 38, 11], [24, 21, 9], [17, 34, 8], [22, 47, 13], [29, 15, 13], [33, 25, 10], [17, 30, 4], [24, 16, 2], [22, 28, 5], [22, 31, 15], [43, 36, 8], [34, 37, 2], [34, 23, 9], [21, 20, 13], [29, 27, 14], [33, 46, 12], [15, 18, 1], [
        29, 35, 3], [25, 19, 9], [43, 44, 1], [47, 42, 1], [25, 41, 14], [20, 40, 15], [38, 26, 9], [46, 39, 8], [45, 18, 5], [16, 18, 1], [40, 45, 8], [41, 24, 15], [27, 46, 2], [27, 25, 7], [21, 26, 9], [40, 26, 8], [19, 46, 13], [21, 42, 3], [35, 44, 1], [30, 15, 8], [29, 34, 8], [23, 18, 15], [37, 33, 8], [31, 28, 2]]

    t2 = [(str(i[0]), str(i[1]), i[2]) for i in t]
    g = Graph.TupleList(t2, weights=True)
    loop_update(g, 2)
    # gl = threading.Thread(target=loop_update_update, args=(g, 2))
    # dl = threading.Thread(target=loop_update_Dijkstra, args=(g))

    # gl.start()
    # dl.start()
    # show_weihtges(g)
    # update_graph(g)
    # print('--------')
    # show_weihtges(g)


if __name__ == '__main__':
    main()
