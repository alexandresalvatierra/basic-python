import pandas as pd
pd.set_option( 'display.max_columns', 5 )

file_path = 'C:/Users/profAlexandre/Desktop/inteligencia artificial/data-preprocessing/dataset/'
file_name = 'forest-fires-in-brazil.csv'

df = pd.read_csv( file_path + file_name, encoding = 'ISO-8859-1' )

# show head from dataset
print( df.head() )

# show total rows and columns from dataset
print( df.shape )

# show types of columns
print( df.dtypes )

# change type of column as object
df['year'] = df['year'].astype( object )

print( df.dtypes )

# change type of column as int
df['year'] = df['year'].astype( int )

print( df.dtypes )