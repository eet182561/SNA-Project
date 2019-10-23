import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import networkx as nx

loc = 'BasicTablemod.csv'

df = pd.read_csv(loc)
BusStops = list(set(list(df['Source'])))
Routes = list(set(list(df['RouteNumber'])))
Routes_ar = np.array(Routes)

BusStopsDict = {}
for bs in BusStops:
    BusStopsDict[bs] = set(list(df[df.values == bs]['RouteNumber']))

BusRouteDict = {}
for r in Routes:
    BusRouteDict[r] = set(list(df[df.values == r]['Source']))

route_index = {}
index = 0
for r in Routes:
    route_index[r] = index
    index = index + 1

index = 0
bus_index = {}
for bs in BusStops:
    bus_index[bs] = index
    index = index + 1

BBase = np.zeros((len(BusStops), len(BusStops)))

for bs1 in BusStopsDict:
    for bs2 in BusStopsDict:
        BBase[bus_index[bs1],bus_index[bs2]] = 1*(len(BusStopsDict[bs1].intersection(BusStopsDict[bs2])) >= 1)

dfm = pd.DataFrame(BBase)

Pgraph = nx.Graph()
Pgraph = nx.from_numpy_matrix(BBase)
fwnp = nx.floyd_warshall_numpy(Pgraph)
#dia = nx.diameter(Pgraph)
#assert (dia == max(fwnp))
dict_fwnp ={0:0,1:0,2:0,3:0,4:0}
for m in range(0,len(BusStops)):
    for n in range(0,len(BusStops)):
        dict_fwnp[fwnp[m,n]] = dict_fwnp[fwnp[m,n]]+1

fwnp_bar = [dict_fwnp[1]/2,dict_fwnp[2]/2,dict_fwnp[3]/2,dict_fwnp[4]/2]
label = ["1","2","3","4"]
index = np.arange(len(label))
plt.bar(index, fwnp_bar)
plt.xlabel('Shortest Distance', fontsize=5)
plt.ylabel('No of Pairs having that distance', fontsize=5)
plt.xticks(index, label, fontsize=10, rotation=0)
plt.title('Route changes to reach from one city to another')
plt.show()
plt.savefig('Hops')
