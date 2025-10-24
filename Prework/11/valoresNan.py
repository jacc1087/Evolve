import pandas as pd

# Example dataset wirh NaN values
data_with_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, None, 30, 35],
    'City': ['New York', 'Los Angeles', None, 'Chicago']
}

nan_df = pd.DataFrame(data_with_nan)

#Detect missing values
print("DataFrame with NaN values:")
print(nan_df)
print("Is any NaN values?")
print(nan_df.isnull())
print(nan_df.isnull().sum())

# Fill NaN values
filled_df = nan_df.fillna({'Age': nan_df['Age'].mean(), 'City': 'Unknown'})
print("Data after filling NaN values:")
print(filled_df)

#Drop rows with missing values
dropped_df = nan_df.dropna()
print("Data after dropping rows with NaN values:")
print(dropped_df)