import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Calculate mean
mean_value = df['A'].mean()

# Filter
filtered_df = df[df['A'] > mean_value]
print(filtered_df)
#=================================


import pandas as pd
import numpy as np

# Sample DataFrame
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# Combine filters
filtered_df = df[(df['A'] > 2) & (df['B'] < 4)]
print(filtered_df)
