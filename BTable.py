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

#plt.hist(np.flatten(fwnp))
dict_fwnp ={1:0,2:0,3:0,4:0}
for n in fwnp.flatten().astype(int):
    dict_fwnp[n] = dict_fwnp[n]+1