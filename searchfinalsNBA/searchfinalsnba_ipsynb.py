# -*- coding: utf-8 -*-
"""searchfinalsNBA.ipsynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T_XXntgCkp_YNaFbc_jutk3k0ayQtp_X
"""

# import libaries
import pandas as pd
from google.colab import files
import io

pd.options.mode.chained_assignment = None

# upload .csv files from local desktop
uploaded = files.upload()

# read .csv files into dataframes
nba2010 = pd.read_csv(io.StringIO(uploaded['nba2010.csv'].decode('utf-8')))
nba2011 = pd.read_csv(io.StringIO(uploaded['nba2011.csv'].decode('utf-8')))
nba2012 = pd.read_csv(io.StringIO(uploaded['nba2012.csv'].decode('utf-8')))
nba2013 = pd.read_csv(io.StringIO(uploaded['nba2013.csv'].decode('utf-8')))
nba2014 = pd.read_csv(io.StringIO(uploaded['nba2014.csv'].decode('utf-8')))
nba2015 = pd.read_csv(io.StringIO(uploaded['nba2015.csv'].decode('utf-8')))
nba2016 = pd.read_csv(io.StringIO(uploaded['nba2016.csv'].decode('utf-8')))
nba2017 = pd.read_csv(io.StringIO(uploaded['nba2017.csv'].decode('utf-8')))
nba2018 = pd.read_csv(io.StringIO(uploaded['nba2018.csv'].decode('utf-8')))
nba2019 = pd.read_csv(io.StringIO(uploaded['nba2019.csv'].decode('utf-8')))
nba2020 = pd.read_csv(io.StringIO(uploaded['nba2020.csv'].decode('utf-8')))
nba2021 = pd.read_csv(io.StringIO(uploaded['nba2021.csv'].decode('utf-8')))
nba2022 = pd.read_csv(io.StringIO(uploaded['nba2022.csv'].decode('utf-8')))

nba2010['year'] = 2010
nba2011['year'] = 2011
nba2012['year'] = 2012
nba2013['year'] = 2013
nba2014['year'] = 2014
nba2015['year'] = 2015
nba2016['year'] = 2016
nba2017['year'] = 2017
nba2018['year'] = 2018
nba2019['year'] = 2019
nba2020['year'] = 2020
nba2021['year'] = 2021
nba2022['year'] = 2022

def simplifyName(dfs):
  for df in dfs:
    df.columns = df.columns.str.split(':').str[0]

def addTopSearch(dfs):
  for df in dfs:
    df.iloc[:,1] = df.iloc[:,1].astype(str).str.rstrip('%').astype('float')
    df.iloc[:,2] = df.iloc[:,2].astype(str).str.rstrip('%').astype('float')
    df['topsearch'] = df.iloc[:,1:3].idxmax(axis=1)

def addWinner(dfs):
  for df in dfs:
    df['winner'] = df.columns[1]

def renameColumn(dfs):
  for df in dfs:
    df.columns = ['state','team1','team2','year','topsearch','winner']

def appendAll(dfs):
  if len(dfs)==1:
    return dfs
  else:
    return dfs[0].append(appendAll(dfs[1:]))

dfs = [nba2010,nba2011,nba2012,nba2013,nba2014,nba2015,nba2016,nba2017,nba2018,nba2019,nba2020,nba2021,nba2022]

simplifyName(dfs)
addTopSearch(dfs)
addWinner(dfs)
renameColumn(dfs)

searches = appendAll(dfs)

searches.to_csv('searches.csv')

files.download('searches.csv')