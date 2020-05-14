import pandas as pd
pd.set_option( 'display.max_columns', 24 )

file_path = 'C:/Users/profAlexandre/Desktop/inteligencia artificial/data-preprocessing/dataset/'
file_name = 'traffic-collision-data-from-2010-to-present.csv'

df = pd.read_csv( file_path + file_name )

# show head from dataset
#print( df.head() )

# show total rows and columns from dataset
#print( df.shape )

# encoding 'Area Name'
encoding = pd.get_dummies( df['Area Name'] )

#print( encoding.head() )

# concat encoding to dataset
concat = pd.concat( [df, encoding], axis = 1 )

# remove column Area Name
concat.drop( 'Area Name', axis = 1 )

print( concat.head() )