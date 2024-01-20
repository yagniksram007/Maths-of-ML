import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset from an Excel sheet
file_path ='D:/My Files/Engineering/5th Sem/ML Lab/Dataset/Weights.xlsx'


df = pd.read_excel(file_path)

# Check the first few rows of the dataset
print(df.head())

# Extracting height and weight columns
X = df[['Height']]
y = df['Weight']

# Initialize the linear regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Take user input for height
height_input = float(input("Enter the height (in cm): "))

# Make prediction for the given height
weight_prediction = model.predict([[height_input]])

# Display the predicted weight
print(f'Predicted Weight for {height_input} cm: {weight_prediction[0]}')


# Visualize the linear regression line
plt.scatter(X, y, color='blue', label='Height-Weight points')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Linear Regression')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Linear Regression:  Prediction')
plt.legend()
plt.show()