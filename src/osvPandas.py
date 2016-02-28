import pandas as pd
import numpy as np
import networkx as nx
import re

tabby=pd.read_csv('../stp/Tabby2.csv',sep=';')
points = tabby[tabby['txt'].str.contains("CARTESIAN_POINT")==True]
points['txt'] = points['txt'].str.replace("CARTESIAN_POINT\('',",'')
points['txt'] = points['txt'].str.replace("\)\)",')')
pattern = '#[0-9]*'
tabby['nodes']=map(lambda x : re.findall(pattern,x),tabby['txt'].values)
pt = map(lambda x : eval(x),points['txt'].values)
G = nx.Graph()
G.add_nodes_from(tabby['#ID'].values)
du = dict(zip(tabby["#ID"],tabby['nodes']))
for k in du:
    for n in du[k]:
        G.add_edge(k,n)

