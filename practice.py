import polars as pl

# Step 1: Create a DataFrame
df = pl.DataFrame({
    "name": ["Carlos", "Emma", "Liam", "Sophia"],
    "age": [29, 34, 23, 31],
    "salary": [52000, 68000, 48000, 72000],
    "department": ["IT", "HR", "IT", "Finance"]
})

# Step 2: Filter people in IT department and age > 25
filtered_df = df.filter(
    (pl.col("department") == "IT") & (pl.col("age") > 25)
)

# Step 3: Add a new column with 10% bonus
df_with_bonus = df.with_columns(
    (pl.col("salary") * 1.10).alias("salary_with_bonus")
)

# Step 4: Group by department and calculate average salary
avg_salary = df.groupby("department").agg(
    pl.col("salary").mean().alias("avg_salary")
)

# Step 5: Sort by age
sorted_df = df.sort("age")

# Step 6: Show results
print("Original DataFrame:\n", df)
print("\nFiltered (IT & age > 25):\n", filtered_df)
print("\nWith Bonus Column:\n", df_with_bonus)
print("\nAverage Salary by Department:\n", avg_salary)
print("\nSorted by Age:\n", sorted_df)