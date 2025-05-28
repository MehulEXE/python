import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
import numpy as np

# Load dataset
df = pd.read_csv(r"C:\Users\dell\Downloads\MagicBricks.csv")

# Drop column with many missing values
df = df.drop(columns=['Per_Sqft'])

# Impute missing numerical values
num_imputer = SimpleImputer(strategy='median')
df[['Bathroom', 'Parking']] = num_imputer.fit_transform(df[['Bathroom', 'Parking']])

# Impute missing categorical values
cat_imputer = SimpleImputer(strategy='most_frequent')
df[['Furnishing', 'Type']] = cat_imputer.fit_transform(df[['Furnishing', 'Type']])

# Encode categorical variables
label_encoders = {}
for col in ['Furnishing', 'Locality', 'Status', 'Transaction', 'Type']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Split features and target
X = df.drop(columns=['Price'])
y = df['Price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Print nicely formatted results
print("Model Performance on Test Data")
print("-" * 40)
print(f"Mean Squared Error (MSE): ₹{mse:,.0f}")
print(f"Root Mean Squared Error (RMSE): ₹{rmse:,.0f}")
print(f"R² Score: {r2:.2f} ({r2 * 100:.1f}%)")

# Display example predictions
print("\nSample Predictions:")
for actual, predicted in zip(y_test[:5], y_pred[:5]):
    print(f"Actual: ₹{actual:,.0f} \t Predicted: ₹{predicted:,.0f}")
