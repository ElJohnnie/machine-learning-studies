import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Dados de exemplo
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Min-Max Scaling usando NumPy
min_val = np.min(data)
max_val = np.max(data)
normalized_data_numpy = (data - min_val) / (max_val - min_val)

print("Min-Max Scaled Data (NumPy):")
print(normalized_data_numpy)

# Criando um DataFrame com pandas
data_df = pd.DataFrame(data, columns=['Feature1', 'Feature2', 'Feature3'])

# Z-Score Normalization usando pandas
normalized_data_pandas = data_df.apply(lambda column: (column - column.mean()) / column.std(), axis=0)

print("Z-Score Normalized Data (pandas):")
print(normalized_data_pandas)

# Min-Max Scaling com Scikit-learn
min_max_scaler = MinMaxScaler()
normalized_data_minmax = min_max_scaler.fit_transform(data)

print("Min-Max Scaled Data (Scikit-learn):")
print(normalized_data_minmax)

# Z-Score Normalization com Scikit-learn
z_score_scaler = StandardScaler()
normalized_data_zscore = z_score_scaler.fit_transform(data)

print("Z-Score Normalized Data (Scikit-learn):")
print(normalized_data_zscore)
