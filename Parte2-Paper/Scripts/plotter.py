import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('nodevit.csv')
df = df.sort_values(by=["# Nodes"])
print(df)
nodes = df["# Nodes"].to_numpy()
changes = df["# Cambios"].to_numpy()
time = df["Tiempo"].to_numpy()
iterations = df["Iteraciones"].to_numpy()
plt.plot(nodes, time)
plt.title("Nodos vs. Tiempo de ejecucion")
plt.xlabel("Nodos")
plt.ylabel("Tiempo (Segs)")
plt.savefig('./plots/nodevtime.png')
