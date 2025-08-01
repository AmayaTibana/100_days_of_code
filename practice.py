# USCG Search and Rescue Stats Analysis

# ========== POLARS ========== #
import polars as pl

# Load dataset with Polars
df = pl.read_csv("USCG.Search.Rescue.Stats.csv")

# Show basic summary stats
print("=== Polars Summary ===")
print(df.describe())

# Filter rows where 'Cases' are greater than the mean
mean_cases = df.select(pl.col("Cases").mean()).item()
df_high_cases = df.filter(pl.col("Cases") > mean_cases)
print("=== Rows with Cases > Mean ===")
print(df_high_cases)

# Optional: Save filtered result to CSV
# df_high_cases.write_csv("filtered_cases.csv")


# ========== NUMPY ========== #
import numpy as np

# Convert to NumPy array
np_array = df.to_numpy()
print("=== NumPy Array Shape Before Reshape ===")
print(np_array.shape)

# Reshape to 4 x 13 x 9
reshaped_array = np_array.reshape(4, 13, 9)
print("=== NumPy Reshaped Array (4x13x9) ===")
print(reshaped_array.shape)


# ========== DASK ========== #
import dask.dataframe as dd

# Load CSV with Dask
ddf = dd.read_csv("USCG.Search.Rescue.Stats.csv")

# Compute standard deviation for all columns
print("=== Dask Standard Deviation ===")
print(ddf.std().compute())