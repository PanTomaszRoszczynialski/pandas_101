import pandas as pd
import tables as tb
import numpy as np
from time import sleep
from datetime import datetime

# Some time format helper for time management
YMD_FORMAT = '%Y_%m_%d'
HMS_FORMAT = '%H%M%S'

# Prepare time markers
_current_time = datetime.now()

class Particle(tb.IsDescription):
    # For each measurement we need timestamps
    # for proper time-dependent analysis (TimeCols suck)
    time_HMS = tb.StringCol(32)

    # Any kind of data 
    momentum = tb.Int64Col()
    velocity = tb.Int64Col()

filename = 'db.h5'
f = tb.open_file(filename, 'w', title='data')
f.close()

# Not related to above:

# Pandas besic series
# for each day I need somethig like this
# only with multiple comments and inside 
# some great database

s = pd.Series()

for it in range(20):
    news = pd.Series(it**2, index = [pd.to_datetime(datetime.now())])
    s = s.append(news)
    sleep(1)
