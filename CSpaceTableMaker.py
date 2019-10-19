import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

loc = 'BasicTablemod.csv'

df = pd.read_csv(loc)
BusStops = list(set(list(df['Source'])))
Routes = list(set(list(df['RouteNumber'])))

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
CBase = np.zeros((len(Routes), len(Routes)))

for r1 in Routes:
    for r2 in Routes:
        CBase[route_index[r1], route_index[r2]] = len(BusRouteDict[r1].intersection(BusRouteDict[r2]))

CBase = np.multiply(CBase, 1 - np.eye((len(Routes))))

# Plot Hist
C_max = np.max(CBase, axis=1)
[n, bins, drop] = plt.hist(C_max, 25)
plt.xlabel('Number of Common Bust Stops')
plt.ylabel('Number of routes')

# Uncomment following line to Write image file to Disk
# plt.savefig('CSpaceHist')
