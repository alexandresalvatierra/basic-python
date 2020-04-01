import pandas as pd
pd.set_option('display.max_columns', 5)

file_path = 'C:/Users/profAlexandre/Desktop/inteligencia artificial/data-preprocessing/dataset/2015-building-energy-benchmarking.csv'
data = pd.read_csv(file_path, encoding = "UTF-8")

# show head from dataset
print( data.head() )

# show total rows and columns from dataset
print( data.shape )

# get not NaN from dataset
data_without_nan = data.dropna()
print( data_without_nan.shape )

# function to show missing data
def getMissingInfo():
    # get amount missing data
    missing = data.isnull().sum()
    print( missing )
    # get percent missing data
    missing_percent = ( missing / len( data['OSEBuildingID'] ) ) * 100
    print( missing_percent )

getMissingInfo()

# replacing missing data from ENERGYSTARScore by median
data['ENERGYSTARScore'] = data['ENERGYSTARScore'].fillna( data['ENERGYSTARScore'].median() )

getMissingInfo()

# replacing missing data from ENERGYSTARScore by mean
data['ENERGYSTARScore'] = data['ENERGYSTARScore'].fillna( data['ENERGYSTARScore'].mean() )

getMissingInfo()