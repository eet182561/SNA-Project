import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('BasicTablemod.csv')
print(df.head())
temp = np.array(df[['Source', 'Target']])
g = nx.Graph()
g.add_edges_from(temp)
pos = nx.spring_layout(g, iterations=500)
nx.draw_networkx(g, pos=pos, node_size=10, with_labels=False)
plt.show()
