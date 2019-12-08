import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'measles.csv'

#df = pd.read_csv(filename)

#rate = df['2010']

#years = []
#itercol = iter(df.columns)
#next(itercol)
#next(itercol)
#for col in itercol:
    #print(col)
    #years.append(col)
#print(years)
    
    #for row in df.iterrows():
        #print(row[1], col)

#columns=['Country', 'W', 'species'])
#ax1 = df.plot.scatter(x='', y='World_Bank_Income_Level', c='Country')

series = pd.read_csv(filename, header=0, index_col=0)
series.plot()
plt.show()