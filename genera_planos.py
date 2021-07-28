# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:24:25 2021

@author: Adrian
"""
from geopandas.io.file import to_file
import numpy as np
import pandas as pd
from shapely import geometry
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))

# shp_path = "./DATA/gpp-test-area.shp"
shp_path = "gpp-test-area.shp"
sf = shp.Reader(shp_path)

#Convierte ShapeFile a Pandas DataFrame 
def read_shapefile(sf):
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df

#Devuelve un Dataframe filtrado por un minimo de elevacion
# y con el nombre del perimetro
def get_obstaculos(df, perimetro, minimo = 0):
    a = df.loc[df['ELEVATION'] > minimo]
    b = df.loc[df['NAME'].str.contains(perimetro)]
    return a.append(b)

def plot_map(data, sf, x_lim = None, y_lim = None, figsize = (11,9)):
    plt.figure(figsize = figsize)
    for d in data.iterrows():
        shape = sf.shape(d[0])
        x = [i[0] for i in shape.points[:]]
        y = [i[1] for i in shape.points[:]]
        plt.plot(x, y,'k')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('GPP TEST AREA: Monte Mario - Italy')
        '''
        if (x_lim == None) & (y_lim == None):
            x0 = np.mean(x)
            y0 = np.mean(y)
            plt.text(x0, y0, id, fontsize=10)
        id = id+1
        '''
    if (x_lim != None) & (y_lim != None):     
        plt.xlim(x_lim)
        plt.ylim(y_lim)
    

d = read_shapefile(sf)
data = get_obstaculos(read_shapefile(sf),  'gpp-test-area', 30)

plot_map(data, sf, x_lim = None, y_lim = None, figsize = (11,11))
plt.show()

# Additional lines to save results in a shapefile 

data_o= data 

data.to_excel('XYZ_ge30.xlsx') 

import geopandas 

from geopandas import GeoDataFrame
 
data_o = geopandas.GeoDataFrame(data_o, geometry='geometry')
     
data_o.to_file('XYZ_ge30.shp')#, driver='ESRI_Shapefile')

