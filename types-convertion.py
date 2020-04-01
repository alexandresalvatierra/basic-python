import pandas as pd
pd.set_option('display.max_columns', 5)

file_path = 'C:/Users/profAlexandre/Desktop/inteligencia artificial/data-preprocessing/dataset/forest-fires-in-brazil.csv'
data = pd.read_csv(file_path, encoding = "ISO-8859-1")

# show head from dataset
print( data.head() )

# show total rows and columns from dataset
print( data.shape )

# show types of columns
print( data.dtypes )

# change type of column as object
data['year'] = data['year'].astype(object)

print( data.dtypes )

# change type of column as int
data['year'] = data['year'].astype(int)

print( data.dtypes )