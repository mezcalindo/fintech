# Pulling, viewing, and exporting VXUS ETF price data

# Import the software libraries whose functionality we will rely on
from alpha_vantage.timeseries import TimeSeries

# Input your unique Alpha Vantage API key on the next line
key = 'INPUT YOUR KEY HERE'

# Choose your output format (pandas tabular), or default to JSON (python dict)
ts = TimeSeries(key, output_format='pandas')

# Get the data, which returns a tuple of 100 records
# vxus_data is a pandas dataframe, vxus_meta_data is a dict
vxus_data, vxus_meta_data = ts.get_daily(symbol='VXUS')

# View the data to verify it's utility and accuracy
# Print directly in the terminal window
print(vxus_data.to_string())
