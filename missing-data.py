import pandas as pd

file_path = 'C:/Users/profAlexandre/Desktop/inteligencia artificial/data-preprocessing/dataset/'
file_name = '2015-building-energy-benchmarking.csv'

df = pd.read_csv( file_path + file_name )

# show head from dataset
print( df.head() )

# show total rows and columns from dataset
print( df.shape )

# get not NaN from dataset
data_without_nan = df.dropna()
print( data_without_nan.shape )

# function to show missing data
def getMissingInfo():
    # get amount missing data
    missing = df.isnull().sum()
    print( missing )
    # get percent missing data
    missing_percent = ( missing / len( df['OSEBuildingID'] ) ) * 100
    print( missing_percent )

getMissingInfo()

# replacing missing data from ENERGYSTARScore by median
df['ENERGYSTARScore'] = df['ENERGYSTARScore'].fillna( df['ENERGYSTARScore'].median() )

getMissingInfo()

# replacing missing data from ENERGYSTARScore by mean
df['ENERGYSTARScore'] = df['ENERGYSTARScore'].fillna( df['ENERGYSTARScore'].mean() )

getMissingInfo()