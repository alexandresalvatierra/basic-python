import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

pd.set_option( 'display.width', 1000 )

file_path = 'C:/Users/profAlexandre/Desktop/inteligencia artificial/data-preprocessing/dataset/'
file_name = 'diabetes.csv'

columns = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']

df = pd.read_csv( file_path + file_name, names = columns, header = 0 )

print( df.head() )

# show types of columns
print( df.dtypes )

# show correlation
print( df.corr( method = 'pearson' ) )


# set plot setup
plt.figure( figsize = (10, 10) )

# set heatmap setup
sb.heatmap( df.corr() )

# show image
plt.show()
