import pandas as pd

left_data = {
    'id': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
}

right_data = {
    'id': [3, 4, 5],
    'Score': [85, 90, 95]
}

left_df = pd.DataFrame(left_data)
right_df = pd.DataFrame(right_data)

# Merge DataFrames on 'id' column
merged_df = pd.merge(left_df, right_df, on='id', how='inner')
print("Merged DataFrame:")
print(merged_df)

# Outer join exampe
outer_join_df = pd.merge(left_df, right_df, on='id', how='outer')
print("\nOuter Join DataFrame with Indicator:")
print(outer_join_df)