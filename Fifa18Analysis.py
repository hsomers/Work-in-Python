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
df.loc[df['cb'].idxmax()]

#Create mini dataframes with all the top players in each position
CBs = df[df['cb']==df['cb'].max()][['player_name','position','cb']]
RBs = df[df['rb']==df['rb'].max()][['player_name','position','rb']]
LBs = df[df['lb']==df['lb'].max()][['player_name','position','lb']]
CDMs = df[df['cdm']==df['cdm'].max()][['player_name','position','cdm']]
CMs = df[df['cm']==df['cm'].max()][['player_name','position','cm']]
RWs = df[df['rw']==df['rw'].max()][['player_name','position','rw']]
LWs = df[df['lw']==df['lw'].max()][['player_name','position','lw']]
STs = df[df['st']==df['st'].max()][['player_name','position','st']]

def Find_Top_At_Pos(df, Pos):
    return df[df[Pos]==df[Pos].max()][['player_name','position',Pos]]

def Select_Top1_At_Pos(Plyrs,Pos):
    return Plyrs.iloc[0][['player_name',Pos]]

CBs = Find_Top_At_Pos(df, 'cb')
CB1 = Select_Top1_At_Pos(CBs, 'cb')
