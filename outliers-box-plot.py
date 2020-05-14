import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option( 'display.max_columns', 20 )

file_path = 'C:/Users/profAlexandre/Desktop/inteligencia artificial/data-preprocessing/dataset/'
file_name = 'houses_to_rent_v2.csv'

df = pd.read_csv( file_path + file_name )

# show head from dataset
# print( df.head() )

# show total rows and columns from dataset
# print( df.shape )


# function to calc Outliers IRQ method
def getIRQ( column ):
    # arrange data in increasing order
    sort_column = column.sort_values(ascending=True)

    # find first quartile and third quartile
    q1, q3 = sort_column.quantile( [ 0.25, 0.75 ] )

    # find IQR - difference between third and first quartile
    iqr = q3 - q1

    # find lower and upper bound
    lower_bound = q1 - ( 1.5 * iqr ) 
    upper_bound = q3 + ( 1.5 * iqr ) 

    return lower_bound, upper_bound

lb, ub = getIRQ( df['rent amount (R$)'] )

# Show lower and upper bounds
print("Lower bound ", lb, " Upper bound ", ub)

# Show total of Uppers Outliers
print( "Total Uppers Outliers: ", df[  df['rent amount (R$)'] > ub  ].count()['rent amount (R$)'] )

# Show total of Lowers Outliers
print( "Total Lowers Outliers: ", df[  df['rent amount (R$)'] < lb  ].count()['rent amount (R$)'] )

df.boxplot( column = ['rent amount (R$)'] )
plt.show()