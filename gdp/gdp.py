# -*- coding: utf-8 -*-
"""gdp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p6xvRtTcouUViQIC_mcdblH6npCmvovh
"""

# import libaries
import pandas as pd
from google.colab import files
import io

pd.options.mode.chained_assignment = None

# upload .csv files from local desktop
uploaded = files.upload()

# read .csv files into dataframes
gdp = pd.read_csv(io.StringIO(uploaded['gdp.csv'].decode('utf-8')))

# pivot longer
gdp = pd.melt(gdp, id_vars='Country Name', value_vars=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969',
                                         '1970','1971','1972','1973','1974','1975','1976','1977','1978','1979',
                                         '1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
                                         '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999',
                                         '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009',
                                         '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019',
                                         '2020','2021'])

# filter to countries in Europe
gdp = gdp[gdp['Country Name'].isin(['Hungary','Belarus','Austria','Serbia','Switzerland','Germany','Holy See','Andorra','Bulgaria','United Kingdom',
                              'France','Montenegro','Luxembourg','Italy','Denmark','Finland','Slovakia','Norway','Ireland','Spain',
                              'Malta','Ukraine','Croatia','Moldova','Monaco','Liechtenstein','Poland','Iceland','San Marino','Bosnia and Herzegovina',
                              'Albania','Lithuania','North Macedonia','Slovenia','Romania','Latvia','Netherlands','Russia','Estonia','Belgium',
                              'Czech Republic','Greece','Portugal','Sweden'])]

# download as csv
gdp.to_csv('gdp.csv')
files.download('gdp.csv')