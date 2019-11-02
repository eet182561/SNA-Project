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

f = open("bip.gexf",'w+')
f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
f.write("<gexf xmlns=\"http://www.gexf.net/1.2draft\" version=\"1.2\">\n")
f.write("    <meta lastmodifieddate=\"2009-03-20\">\n")
f.write("        <creator>Gexf.net</creator>\n")
f.write("        <description>A hello world! file</description>\n")
f.write("    </meta>\n")
f.write("    <graph mode=\"static\" defaultedgetype=\"directed\">\n")
f.write("        <nodes>")
for key, item in BusStopsDict.items():
    f.write('           <node id=\"'+key+'\" label = "2" />\n')
for key ,item in BusRouteDict.items():
    f.write('           <node id=\"' + key + '\" label = "1" />\n')

f.write('        </nodes>\n')
f.write('        <edges>\n')
c = 0
for key,item in BusRouteDict.items():
    for i in item:
        f.write('           <edge id=\"'+str(c)+'\" source=\"' +key +'\" target=\"'+i+'\" />\n')
        c = c +1

f.write('       </edges>\n')
f.write('   </graph>\n')
f.write('</gexf>')
f.close()