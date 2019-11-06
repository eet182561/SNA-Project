import networkx as nx
import numpy as np
import pandas as pd

<<<<<<< HEAD
loc = 'BasicTablemod.csv'
=======
import xlrd


loc = 'SimulationTable.csv'
>>>>>>> eed0393afc0e6d896c49b2682c698d636b5f340f


def eff(nxg):
    # nxg is a network x graph
    n = len(nxg)
    dist_mat = nx.floyd_warshall_numpy(nxg)
    sum = 0.0
    for i in range(0, n):
        for j in range(i + 1, n):
            sum = sum+ (1/dist_mat[i,j])
    return sum / (n * (n - 1))

def transiteff(network_array):
    #network array is a numpy array
    n,n = network_array.shape
    #dist_mat = nx.floyd_warshall_numpy(nxg)
    sum = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            sum += network_array[i][j]
    return sum / (n * (n - 1))

<<<<<<< HEAD
def df_to_adjmat(df):
    BusStops = list(set(list(df['Source'])))
    Routes = list(set(list(df['RouteNumber'])))
    BBase = np.zeros((len(BusStops), len(BusStops)))
=======
def DeleteEdge():
    loc = ("E:\Sem-3\SNA\Project\\SimulationTable.xlsx")
    sheet = wb.sheet_by_index(0)
    print(sheet.cell_value(0, 0))


    #Read SimulationTable
    #Run for all nodes
     #     Select one node
      #      delete it from table
       #     form a adjacency matrix
        #    Efficency computation

    for i = 1 to NoOfEdges   # We will not consider boundary nodes and nodes having degree more than 2



>>>>>>> eed0393afc0e6d896c49b2682c698d636b5f340f

def read_data(filename):
    df = pd.read_csv(filename)
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
            BBase[bus_index[bs1], bus_index[bs2]] = 1 * (len(BusStopsDict[bs1].intersection(BusStopsDict[bs2])) >= 1)
    return BusRouteDict, BusStopsDict, BusStops, Routes, BBase


# BBase matrix used for detecting presence of node
# PTNadjmat is randomly generated weight matrix for the network

BRD,BSD,BS,R,BB = read_data(loc)
Pgraph = nx.Graph()
Pgraph = nx.from_numpy_matrix(BB)
print(eff(Pgraph))
#Assigning random weights to the graph
PTNadjmat = np.random.random_sample(BB.shape) * 10
np.fill_diagonal(PTNadjmat, 0)

PTNadjmat = np.multiply(PTNadjmat,BB)




