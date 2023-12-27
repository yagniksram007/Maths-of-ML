import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data from Excel sheet 
file_path = ('D:/My Files/Engineering/5th Sem/ML Lab/Data.xlsx')  # Replace with the actual file path
df = pd.read_excel(file_path)

print(df)

# Excel sheet has 'Year' and 'Sales' columns
X = df[['Year']]
y = df['Sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict sales for the next year
next_year = [[2018]]  # Replace with the year you want to predict
predicted_sales = model.predict(next_year)

# Print the predicted sales for the next year
print(f"Predicted Sales for {next_year[0][0]}: {predicted_sales[0]}")

# Visualize the linear regression line
plt.scatter(X, y, color='blue', label='Actual Sales')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Linear Regression: Sales Prediction')
plt.legend()
plt.show()
