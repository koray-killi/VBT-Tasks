'''
1. Veri Manipülasyonu ve Keşif
Görev: Pandas kullanarak bir CSV dosyasini yükleyin ve veri keşfi yapin.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

table = pd.read_csv('Data Science Community\VBT-Tasks\Tasks\Iris.csv')

'''
print(table.head)
print(table.tail)
'''

'''
print(table.isnull()) # Has no missing value.
#print(table.isna()) - Same thing with upper one.
'''
'''
print(table.mean()) # This ones gives..
print(table.median()) # me some error..
print(table.std())# I don't know why.

# Çeyrekler (Quarters) : Each one of quarter divides the graph to 1/4.

print(table.describe()) # It gives us to mean, std, min, max in one time.
'''


# Visualization with MatPlotLib
plt.bar(table['Id'],table[2])
plt.title("Id versus SepalLenghtCm")
plt.xlabel("ID")
plt.ylabel("Sepal Lenght (cm)")
plt.show()
