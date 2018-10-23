# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 20:14:23 2018

@author: pouru
"""

import pandas as pd
#
names2017 = pd.read_csv(r"C:\users\pouru\Downloads\names\yob2017.txt",\
                        names = ['name', 'sex', 'births'])
grouped = names2017.groupby(['sex'])
top250 = grouped.apply(get_top250)
girls = top250[top250.sex == 'F']
print(girls['name'].count)
 
def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]

def get_top250(group):
    return group.sort_values(by='births', ascending=False)[:250]


def top250Names():
    names = pd.read_csv(r"C:\users\pouru\Downloads\names\yob1880.txt",\
                            names = ['name', 'sex', 'births'])
    grouped = names.groupby(['sex'])
    top250 = grouped.apply(get_top250)
    girls = top250[top250.sex == 'F']
    
    print('The top 250 girls name were ')
    #print(girls) you can use this to view the whole group
    print(girls.name)
    
  

top250Names()