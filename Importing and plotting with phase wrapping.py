import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read and store content
# of an excel file

read_file = pd.read_excel (r'C:\Users\COMSOL\Desktop\test.xlsx')
x = []
y = []

# Write the dataframe object
# into csv file
read_file.to_csv ("Test.csv",
				index = None,
				header=True)

# read csv file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_csv("Test.csv"))

# show the dataframe
print (df)

#choose the respective x- and y-axes
x = df.loc[:,"x"]
y = df.loc[:,"y"]

#plot
#plt.plot(x,y)
#plt.show()
y = (y + np.pi) % (2 * np.pi) - np.pi
plt.plot(x,y)
plt.show()
