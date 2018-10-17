# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:23:10 2018

@author: HDSom
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

imp = pd.read_csv('FIFA18 - Ultimate Team players.csv', header = 0)
df = pd.DataFrame(imp)

#Question: Who are the top-rated players at each position?

#Create mini dataframes with all the top players in each position
def Find_Top_At_Pos(df, Pos):
    return df[df[Pos]==df[Pos].max()][['player_name','position',Pos]]

CBs = Find_Top_At_Pos(df, 'cb')
RBs = Find_Top_At_Pos(df, 'rb')
LBs = Find_Top_At_Pos(df, 'lb')
CDMs = Find_Top_At_Pos(df, 'cdm')
CMs = Find_Top_At_Pos(df, 'cm')
LWs = Find_Top_At_Pos(df, 'lw')
RWs = Find_Top_At_Pos(df, 'rw')
STs = Find_Top_At_Pos(df, 'st')

#I need some different mechanism for gk because it doesn't have its own column



#Now let's select the top_n for each position that we need
"""Want 4-3-3
        1 gk
        2 cb
        1 rb
        1 lb
        1 cdm
        2 cm
        1 lw
        1 rw
        1 st
"""
def Select_Top1_At_Pos(Plyrs,Pos):
    return Plyrs.iloc[0][['player_name',Pos]]




