import polars as pl

# Create DataFrame 
data = [{"fruit": "apple", "count": 10, "price": 0.50}, 
        {"fruit": "banana", "count": 20, "price": 0.25}]
df = pl.from_dicts(data)

# Expressions to select, filter, aggregate
sel = df.select(["fruit", "count"]) # Select columns
filt = sel.filter(pl.col("fruit") == "apple") # Filter rows
agg = filt.groupby("fruit").agg(pl.col("count").sum()) # Aggregate

print(agg)