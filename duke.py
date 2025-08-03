import polars as pl

# V - VIEW: Load and look at the dataset
df = pl.from_dicts([
    {"fruit": "apple", "count": 10, "price": 1.2},
    {"fruit": "banana", "count": 5, "price": 0.8},
    {"fruit": "apple", "count": 15, "price": 1.3},
    {"fruit": "banana", "count": 8, "price": 0.75},
    {"fruit": "orange", "count": 12, "price": 1.1},
    {"fruit": "apple", "count": 6, "price": 1.1}
])
print(df)
print(df.schema)  # column names and types

# I - INSPECT: Look deeper into the data
print("First 3 rows:\n", df.head(3))
print("Describe price column:\n", df.select(pl.col("price").describe()))
print("Unique fruits:\n", df.select(pl.col("fruit").unique()))

# M - MANIPULATE: Group, filter, add new columns
# Group by fruit and get summary stats
agg_df = df.groupby("fruit").agg([
    pl.col("count").sum().alias("total_count"),
    pl.col("price").mean().alias("avg_price"),
    pl.col("count").mean().alias("avg_count")
])

# Add a new column to original df (e.g., total value = count * price)
df = df.with_columns((pl.col("count") * pl.col("price")).alias("total_value"))

print("\nAggregated Summary:")
print(agg_df)

print("\nUpdated DataFrame with total value column:")
print(df)