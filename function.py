import numpy as np
import pandas as pd
import os
#FUNCTIONS

def menu():
    os.system('clear')

    striscia()
    print('S C O M M E S S E')
    striscia()
    print('1 - aggiungi nuova squadra')
    print('2 - ')
    print('3 - ESCI')
    print('')

def striscia(n=1):
    print('')
    for i in range(n):
        print('############################')
    print('')



def aggiungi_squadra(val):
    file='data/squadre.csv'
    df=pd.read_csv(file)
    new_id=1+max(df.id.values)
    if val not in df.nome.values:
        new=pd.DataFrame([[val,new_id]],columns=['nome','id'])
        df=df.append(new)
        df.to_csv(file,index=False) 
    return


