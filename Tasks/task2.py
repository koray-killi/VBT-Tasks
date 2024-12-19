#   2. Veri Temizleme
#   Görev: Eksik değerler ve aykırı değerleri temizleme.

import pandas as pd
import numpy as np
from scipy.stats import zscore

data = {
    'Ad': ['Ali', 'Ayşe', 'Fatma', None],
    'Yaş': [25, 140, None, 22],
    'Şehir': ['Ankara', 'Konya', 'İstanbul', 'İzmir']
}

df = pd.DataFrame(data) # For creating dataframe.

# To find empty values.
null_values = df[df.isnull().any(axis=1)]
print(f"The lines that includes the null values:\n{null_values}")

# To fill empty values with mean, mod or median.
df['Yaş'] = df['Yaş'].fillna(df['Yaş'].mean()) # fills with mean.
'''
df['Yaş'] = df['Yaş'].fillna(df['Yaş'].mod()) # fills with mod.
df['Yaş'] = df['Yaş'].fillna(df['Yaş'].median()) # fills with median.
'''
print(df) # Checking...

# To find outlier with calculating z-score.
num_values = df.select_dtypes(include=[np.number])
z_scores = zscore(num_values)
print(z_scores)
outlier = (np.abs(z_scores) > 1)
print("Detecting Outlier Values (True means outlier):")
print(outlier)
''' # This code-block gives error and i don't know why. Chat-GPT couldn't solve it.
#To change outlier values
for column in num_values.columns:
    median = df[column].median()  # Column's median
    df.loc[outlier[:, num_values.columns.get_loc(column)], column] = median

print("\n The dataframe that has changed outlier values:")
print(df)
'''