import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# plt.plot(nodes, time)
# plt.title("Nodos vs. Tiempo de ejecucion")
# plt.xlabel("Nodos")
# plt.ylabel("Tiempo (Segs)")
# plt.savefig('./plots/nodevtime.png')

def nodevit(ccdf : pd.DataFrame):
    nodes = ccdf["# Nodes"].to_numpy()
    iterations = ccdf["Iteraciones"].to_numpy()

    plt.plot(nodes, iterations)
    plt.title("Nodos vs. Iteraciones. (10 cambios)")
    plt.xlabel("Nodos")
    plt.ylabel("Iteraciones")
    plt.savefig('./plots/nodevit.png')

def nodevtime(ccdf : pd.DataFrame):
    nodes = ccdf["# Nodes"].to_numpy()
    time = ccdf["Tiempo"].to_numpy()

    plt.plot(nodes, time)
    plt.title("Nodos vs. Tiempo de ejecucion. (10 cambios)")
    plt.xlabel("Nodos")
    plt.ylabel("Tiempo (Segs)")
    plt.savefig('./plots/nodevtime.png')

def changesvtime(cndf : pd.DataFrame):
    changes = cndf["# Cambios"].to_numpy()
    time = cndf["Tiempo"].to_numpy()
    plt.plot(changes, time)
    plt.title("Cambios vs. Tiempo de ejecucion. (200 nodos)")
    plt.xlabel("Cambios")
    plt.ylabel("Tiempo (Segs)")
    plt.savefig('./plots/changesvtime.png')

def main():
    df = pd.read_csv('Data.csv')
    ccdf = df[df['# Cambios'] == 10]
    cndf = df[df['# Nodes'] == 200]
    nodevit(ccdf)
    plt.clf()
    nodevtime(ccdf)
    plt.clf()
    changesvtime(cndf)
    # print(sum(df['Tiempo']))

if "__main__" == __name__:
    main()
