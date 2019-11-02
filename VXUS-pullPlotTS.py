# With this code snippet, we are pulling and plotting VXUS ETF daily closing price data via
# the Alpha Vantage API. The below was adapted from code I found online by a Medium contributor
# and Alpha Vantage dev advocate. It has been cleaned up and enhanced.

# Import the software libraries whose functionality we will rely on
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

# Input your unique Alpha Vantage API key on the next line
key = 'INPUT YOUR KEY HERE'

# Choose your output format (pandas tabular), or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')

# Get the data, which returns a tuple of 100 records
# vxus_data is a pandas dataframe, vxus_meta_data is a dict
vxus_data, vxus_meta_data = ts.get_daily(symbol='VXUS')

# Visualizing the data by determining the plot size and style
figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
vxus_data['4. close'].plot()
plt.gca().invert_xaxis()
plt.tight_layout()
plt.grid()
plt.show()
