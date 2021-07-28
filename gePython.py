import pandas as pd
import geopandas
from geopandas.io.file import read_file

x = geopandas.read_file('gpp-test-area.shp')

print(x)

y = x.loc[x['ELEVATION']>= 70]

# b = x.loc[x['NAME'].str.contains('gpp-test-area') ]
b = x.loc[x['NAME'] == 'gpp-test-area']
y = y.append(b)

print(y)

y.to_file('xyz.shp')

# xx  = geopandas.read_file('xyz.shp')
# xx.to_excel('xx.xlsx')
# xx.describe()

xx2 = pd.read_excel('xx.xlsx')
print(xx2)

# xx2.to_file('xx2.shp')


