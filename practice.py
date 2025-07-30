import polars as pl
import matplotlib.pyplot as plt

data = [{"species": "setosa", "petal_length": 1.4}, 
        {"species": "virginica", "petal_length": 5.1},
        {"species": "versicolor", "petal_length": 4.5}]
        
df = pl.from_dicts(data)

# Extract columns
species = df['species']
lengths = df['petal_length']

# Plot bar chart
fig, ax = plt.subplots()
ax.bar(species, lengths)
ax.set_ylabel('Petal Length') 
ax.set_title("Petal Length by Species")
plt.show()