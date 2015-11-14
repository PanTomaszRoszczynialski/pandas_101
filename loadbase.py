import pandas as pd
import tables as tb
import numpy as np
from time import sleep
from datetime import datetime
import matplotlib.pyplot as plt


# Load database
store = pd.HDFStore('db.h5', 'r')

# Get DataFrame
sacredata = store['sacredata']

# Get movement series
move_series = sacredata.loc[:, 'red']
t = move_series.index.tolist()
y = move_series.values

# plot data retrieved from the base
plt.plot(t,y, 'c')
plt.show()

# Great time gettings
# print df['2015-11-13 14:55']

store.close()
