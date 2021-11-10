# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:58:05 2021

@author: MosaTech
"""

adj_list={
           'A':['B','C'],
           'B':['D','E'],
           'C':['B','F'], 
           'D':[],
           'E':['F'],
           'F':[] 
        }
color={}
parent={}
trav_time={}
dfs_trav_out_put=[]

for node in adj_list.keys():
    color[node]='w(white)'
    parent[node]=None
    trav_time[node]=[-1,-1]
    
    
print('======inital======')   
print(color)
print(parent)     
print(trav_time)
print()  

   
time=0


def dfs(u):
    global time
    color[u]='g (grey)'
    trav_time[u][0]=time
    dfs_trav_out_put.append(u)
    for v in adj_list [u]:
        if color[v]=='w(white)':
          parent[v]=u
          dfs(v)
          
    color[u]="b(black)"
    trav_time[u][1]=time
    time+=1
          
          
dfs('A')
print("===output===")          
print()


for node in adj_list.keys():
     print(node,"=>", trav_time[node])

print()
print(color)
print(parent)
print(trav_time)
print ("traverse")
print(dfs_trav_out_put)
print()




       