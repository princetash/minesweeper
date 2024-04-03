import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


myarray = np.array([[10,30,20], [50,40,60],[1000,2000,3000]])

rownames = ['apples', 'oranges', 'beer']
colnames = ['January', 'February', 'March']


mydf = pd.DataFrame(myarray, index=rownames, columns=colnames)

# print(mydf)
# print(mydf.describe())

scatter_matrix(mydf)
plt.show()




df1 = pd.DataFrame(np.random.randn(10, 4),columns=['A','B','C','D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A','B','C'])
df3 = df1 + df2

# print(df3)

names = pd.Series(['SF', 'San Jose', 'Sacramento'])
sizes = pd.Series([852469, 1015785, 485199])
df = pd.DataFrame({ 'Cities': names, 'Size': sizes })
#df = pd.DataFrame({ 'City name': names,'sizes': sizes })
#print(df)






