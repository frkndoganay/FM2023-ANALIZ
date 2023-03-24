
import pandas as pd 
import numpy as np 
import os
from tabulate import tabulate
 

df=pd.read_csv("FM 2023.csv")
df.rename(columns = {'Position.1':'Positions','Left Foot':'LeftFoot','Right Foot':'RightFoot','ca':'CurrentAbility','pa':'PotentialAbility'}, inplace = True)




#HEDEF HIZLI BİR KANAT OYUNCUSU 
fWP=df[(df.Crossing >12)&(df.Dribbling >12)&(df.Acceleration >15)&(df.Technique >10)&(df.Stamina >11)&(df.Age<25)&(df.Values<15000000)]



with open('fWP.html','w',encoding='utf8') as f:
    f.write(tabulate(fWP,headers="keys",tablefmt="html",stralign="center",numalign="center"))

#HEDEF OFANSIF YONU YUKSEK SOL BEK


lB=df[(df.Dribbling>12)&(df.Tackling>10)&(df.Technique>13)&(df.Vision>12)&(df.Flair>13)&(df.LeftFoot>15)&(df.WBL>8)]

with open('lB.html','w',encoding='utf8') as f:
    f.write(tabulate(lB,headers="keys",tablefmt="html",stralign="center",numalign="center"))
 
 
#HEDEF POTANSIYEL GENC YETENEK

pA=df[(df.Age<19)&(df.Stability>14)&((df.PotentialAbility>150)|(df.PotentialAbility==-8)|(df.PotentialAbility==-85)|(df.PotentialAbility==-9)|(df.PotentialAbility==-95)|(df.PotentialAbility==-10))]  
with open('pA.html','w',encoding='utf8') as f:
    f.write(tabulate(pA,headers="keys",tablefmt="html",stralign="center",numalign="center"))