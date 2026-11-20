"""
hello_feature_engineering.py

Tiny demo of a feature engineering workflow:
- create a small dataset
- handle missing values
- create a new feature
- scale numeric features
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# 1. Create a tiny demo dataset
data = {
    "age": [25, 32, None, 45, 38],
    "salary": [50000, 62000, 58000, None, 72000],
    "city": ["LA", "NY", "LA", "SF", "NY"],
}

df = pd.DataFrame(data)
print("=== Raw data ===")
print(df)
print()

# 2. Very simple feature engineering step:
#    - fill missing numeric values with the column median
#    - create a new feature: salary_per_year_of_age
df["age_filled"] = df["age"].fillna(df["age"].median())
df["salary_filled"] = df["salary"].fillna(df["salary"].median())

df["salary_per_year_of_age"] = df["salary_filled"] / df["age_filled"]

print("=== After simple feature engineering ===")
print(df[["age_filled", "salary_filled", "salary_per_year_of_age", "city"]])
print()

# 3. Build a small preprocessing pipeline with scaling
numeric_features = ["age_filled", "salary_filled", "salary_per_year_of_age"]

numeric_transformer = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
    ]
)

# 4. Fit + transform the numeric features
X_scaled = preprocessor.fit_transform(df)

scaled_df = pd.DataFrame(
    X_scaled,
    columns=[f"{col}_scaled" for col in numeric_features],
)

print("=== Scaled features ===")
print(scaled_df)
print()

print("✅ Feature engineering demo finished successfully.")
