# Pulling data, concatenating closing daily price series of VGTSX and VTSMX,
# and calculating their correlation of returns (daily, weekly, monthly???)

# Import the software libraries whose functionality we will rely on
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Input your unique Alpha Vantage API key on the next line
key = 'INPUT YOUR KEY HERE'

# Choose your output format (pandas tabular), or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')

# Get the full set of data available via the Alpha Vantage API for the tickers of interest
# vgtsx_data is a pandas dataframe, vgtsx_meta_data is a dict
# vtsmx_data is a pandas dataframe, vtsmx_meta_data is a dict
vgtsx_data, vgtsx_meta_data = ts.get_daily(symbol='VGTSX', outputsize=’full’)
vtsmx_data, vtsmx_meta_data = ts.get_daily(symbol=’VTSMX’, outputsize=’full’)

# Combine the key columns of daily closing prices from the two individual dataframes
# containing data on each fund into one shiny new dataframe called vgtsx_vtsmx_data
vgtsx_vtsmx_data = pd.concat([vgtsx_data['4. close'], vtsmx_data['4. close']], axis=1).reindex(vgtsx_data.index)

# Let’s double-check to see that our concatenate operation worked properly
vgtsx_vtsmx_data

# Rename the columns in this new dataframe with more descriptive names
vgtsx_vtsmx_data.columns = ['VGTSX close', 'VTSMX close']

# Visualize the data by determining the plot size and style
figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
vgtsx_data['4. close'].plot()
vtsmx_data[‘4. close’].plot()
plt.gca().invert_xaxis()
plt.tight_layout()
plt.grid()
plt.show()
