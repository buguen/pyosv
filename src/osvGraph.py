import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

#fd = open('../stp/TabbyEvo_4.stp')
fd = open('../stp/TABBY_EVO_step_asm.stp')
lis = fd.readlines()
lis2 = []
for k,li in enumerate(lis):
    lin = li.replace('\r\n','')
    if (lin[0]=='#') and ('=' in lin):
        lis2.append(lin)
    else:
        if len(lis2)>0:
            lis2[-1]=lis2[-1]+lin
        else:
            print lin
# add \n
lis2n = map(lambda x : x+'\n',lis2)
fd.close()
fd=open('../stp/Tabby3.csv',"w")
fd.writelines(lis2n)
fd.close()
#Sosv = pd.Series()
#for k,li in enumerate(lis2):
#    if np.mod(k,10000)==0:
#        print k,'/',len(lis2)
#    lhs=li.split('=')[0]
#    rhs=li.split('=')[1]
#    Sosv[lhs]=rhs
#Sosv.to_pickl('t4.pkl')
##        tc.append(li)
