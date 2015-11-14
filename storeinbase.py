import pandas as pd
import tables as tb
import numpy as np
from time import sleep
from datetime import datetime

# Pandas besic series
# for each day I need somethig like this
# only with multiple comments and inside 
# some great database

s1 = pd.Series()
s2 = pd.Series()

for it in range(20):
    now = pd.to_datetime(datetime.now())
    olds = pd.Series(it*3,  index = [now])
    news = pd.Series(it**2, index = [now])
    s1 = s1.append(news)
    s2 = s2.append(olds)
    print it
    sleep(2)

d = {'red' : s1, 'hue' : s2}
df = pd.DataFrame(d)

# Open database
filename = 'db.h5'
store = pd.HDFStore(filename, 'a')

store['sacredata'] = store['sacredata'].append(df)

store.close()
