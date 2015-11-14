import pandas as pd
import tables as tb
import numpy as np
from time import sleep
from datetime import datetime

# Some time format helper for time management
YMD_FORMAT = '%Y-%m-%d'
HMS_FORMAT = '%H:%M:%S'
TIME_FORMAT= YMD_FORMAT + ' ' + HMS_FORMAT

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
# f = tb.open_file(filename, 'w', title='data')
# f.close()

# Initialize dataframe
columns = ['red', 'green', 'blue',
           'hue', 'saturation', 'value',
           'movement']
df = pd.DataFrame(np.zeros([1,len(columns)]),
                  index = [pd.to_datetime(_current_time)],
                  columns = columns)

# Not related to above:

# Open base
store = pd.HDFStore(filename)

# Write data
store['sacredata'] = df

# Close file
store.close()
