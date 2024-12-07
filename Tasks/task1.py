
#   1. Veri Manipülasyonu ve Keşif
#   Görev: Pandas kullanarak bir CSV dosyasini yükleyin ve veri keşfi yapin.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

table = pd.read_csv('Data Science Community\VBT-Tasks\Tasks\Iris.csv')

'''
table.info() # Get Info about the data set.
print(table.to_string()) # Prints csv table to mainframe.
print(table.head)
print(table.tail)
'''

'''
print(table.isnull()) # Has no missing value.
#print(table.isna()) - Same thing with upper one.
'''
'''
# This ones gives error for Iris dataset.
print(table.mean()) 
print(table.median()) 
print(table.std())

# Çeyrekler (Quarters) : Each one of quarter divides the graph to 1/4.

print(table.describe()) # It gives us to mean, std, min, max in one time - clearly.
'''


# Visualization with MatPlotLib
species_colors = {"Iris-setosa": "red", "Iris-versicolor": "blue", "Iris-virginica": "green"}
table["Color"] = table["Species"].map(species_colors)

plt.figure(figsize=(8, 6))
for species in species_colors:
    subset = table[table["Species"] == species]
    plt.scatter(
        subset["SepalLengthCm"],
        subset["SepalWidthCm"],
        label=species,
        color=species_colors[species],
        alpha=0.7
    )
    
plt.title("Iris Dataset: Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.legend()
plt.grid(True)
plt.show()

