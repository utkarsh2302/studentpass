import pandas as pd

# Assuming you have already downloaded the dataset and saved it as 'StudentsPerformance.csv' locally
dataset_path = 'StudentsPerformance.csv'

# Step 2: Load the dataset
df = pd.read_csv(dataset_path)

# Step 3: Create a new column for passing status in maths
df['math_pass_status'] = df['math score'].apply(lambda x: 'pass' if x > 33 else 'fail')

# Step 4: Save the updated dataset to a new CSV file
updated_dataset_path = 'StudentsPerformance_with_pass_status.csv'
df.to_csv(updated_dataset_path, index=False)

print("Updated dataset saved to", updated_dataset_path)
