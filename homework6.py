# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 01:09:05 2018

@author: pouru
"""
import pandas as pd
#
names1900 = pd.read_csv(r"C:\users\pouru\Downloads\names\yob1900.txt",\
                        names = ['name', 'sex', 'births'])
#Gives you the top name 
def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]
# Gives you the top 25 names
def get_top25(group):
    return group.sort_values(by='births', ascending=False)[:25]
#
grouped = names1900.groupby(['sex'])
top1000 = grouped.apply(get_top1000)
topBoyName = top1000[top1000.sex =='M']
print('The most common boys name in 1900 were')
print(topBoyName.name)
#
def top25Names():
    text = input("Enter the year to find 25 popular boy and girl names for that year")
    names = pd.read_csv(r"C:\users\pouru\Downloads\names\yob" + text + ".txt",\
                            names = ['name', 'sex', 'births'])
    grouped = names.groupby(['sex'])
    top25 = grouped.apply(get_top25)
    girls = top25[top25.sex == 'F']
    
    print('The top 25 girls name were ')
    #print(girls) you can use this to view the whole group
    print(girls.name)
    
    boys = top25[top25.sex =='M']
    print('The top 25 boys name were ')
    #print(boys) you can use this to view the whole group
    print(boys.name)
    
top25Names()

nameInput = input('Enter the name ')
gender = input('Enter the gender ')

years = range(1880,2018)
pieces = []
columns = ['name','sex','births']
for year in years:   
    path = r'C:\users\pouru\Downloads\names\yob%d.txt' %year   
    frame = pd.read_csv(path,names=columns)    
    frame['year'] = year #adding the column year in the dataframe
    pieces.append(frame) #appending that column to the pieces list
#Concatenate into one DataFrame
names = pd.concat(pieces, ignore_index=True)


total_births = names.pivot_table('births', index= 'year',columns='sex', aggfunc=sum)

#def get_top1000(group):    
#    return group.sort_values(by=['births'],ascending=False)[:1000]

grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
#Drop the group index, not needed
top1000.reset_index(inplace=True,drop=True)

boys = top1000[top1000.sex=='M']
girls = top1000[top1000.sex=='F']
total_births = top1000.pivot_table('births',index = 'year',
                                   columns = 'name',
                                   aggfunc=sum)
total_births.info()
subset = total_births[[nameInput]]
subset.plot(subplots=True, figsize=(10,10), grid=False,\
title = "number of births per year")





#    girls = top25[top25.sex=='F']
#    if(boys.name == nameInput):
#        previousBirths = totalBirths;
#        totalBirths = boys.births
#    grouped = frame.groupby(['sex'])
#    top25 = grouped.apply(get_top25)
##Drop the group index, not needed
#    top25.reset_index(inplace=True,drop=True)
#    boys = top25[top25.sex=='M']
#        if(totalBirths > previousBirths):
#            maxYear = year
    
#print(boys)
#print(year)


    
#print(year)
#print(top25)
    



