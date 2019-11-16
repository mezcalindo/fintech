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

# Get the full set of daily price data available via the Alpha Vantage API
# for the tickers of interest
# vgtsx_dataD is a pandas dataframe, vgtsx_meta_dataD is a dict
vgtsx_dataD, vgtsx_meta_dataD = ts.get_daily(symbol='VGTSX', outputsize='full')
vtsmx_dataD, vtsmx_meta_dataD = ts.get_daily(symbol='VTSMX', outputsize='full')
# Do the same for monthly data
# vtsmx_dataM is a pandas dataframe, vtsmx_meta_dataM is a dict
vgtsx_dataM, vgtsx_meta_dataM = ts.get_monthly(symbol='VGTSX')
vtsmx_dataM, vtsmx_meta_dataM = ts.get_monthly(symbol='VTSMX')

# Combine the key columns of daily closing prices from the two individual dataframes
# containing data on each fund into one shiny new dataframe called vgtsx_vtsmx_dataD
vgtsx_vtsmx_dataD = pd.concat([vgtsx_dataD['4. close'], vtsmx_dataD['4. close']], axis=1).reindex(vgtsx_dataD.index)
# Do the same for monthly pricing into a new dataframe called vgtsx_vtsmx_dataM
vgtsx_vtsmx_dataM = pd.concat([vgtsx_dataM['4. close'], vtsmx_dataM['4. close']], axis=1).reindex(vgtsx_dataM.index)

# Let’s double-check to verify that our concatenate operations worked properly
vgtsx_vtsmx_dataD
vgtsx_vtsmx_dataM

# Rename the columns in these new dataframes with more descriptive names
# and sort the data in ascending order by date
vgtsx_vtsmx_dataD.columns = ['VGTSX daily close', 'VTSMX daily close']
vgtsx_vtsmx_dataD = vgtsx_vtsmx_dataD.sort_values(by=['date'], ascending=True)
vgtsx_vtsmx_dataM.columns = ['VGTSX monthly close', 'VTSMX monthly close']
vgtsx_vtsmx_dataM = vgtsx_vtsmx_dataM.sort_values(by=['date'], ascending=True)

# Visualize the daily closing price data by determining the plot size and style
figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
# vgtsx_dataD['4. close'].plot()
# vtsmx_dataD['4. close'].plot()
vgtsx_vtsmx_dataD['VGTSX daily close'].plot()
vgtsx_vtsmx_dataD['VTSMX daily close'].plot()
# plt.gca().invert_xaxis()
plt.tight_layout()
plt.grid()
plt.show()

# Find the percentage change of the day's closing price over the previous day's
# for both funds and store the results in a new dataframe, then check our results
pctDelta_dataD = vgtsx_vtsmx_dataD.pct_change()
pctDelta_dataD
# Do the same for the monthly data
pctDelta_dataM = vgtsx_vtsmx_dataM.pct_change()
pctDelta_dataM

# Find the correlation coefficient for the daily returns of the funds over the entire period
corr_dataD = pctDelta_dataD['VGTSX daily close'].corr(pctDelta_dataD['VTSMX daily close'])
corr_dataD
# Do the same for monthly data
corr_dataM = pctDelta_dataM['VGTSX monthly close'].corr(pctDelta_dataM['VTSMX monthly close'])
corr_dataM
