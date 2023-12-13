import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y
print("x: ", x)
print("y: ", y)
# Step 2: Standardize the data using StandardScaler, 
scaler = StandardScaler().fit(x)

# Step 3: Transform the data
x = scaler.transform(x)
# Step 4: Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y)

# Step 5: Fit the data
model = linear_model.LogisticRegression()

# Step 6: Create a LogsiticRegression object and fit the data
model.fit(x_train, y_train)
print("Score: ", model.score(x_test, y_test))

# Step 7: Print the score to see the accuracy of the model
print("y_test: ", y_test)
for index in range(len(x_test)):
    x = x_test[index]
    x = x.reshape(-1, 3)
    y_pred = "Not Purchased" if not model.predict(x)[0] else "Purchased"
    actual = "Not PUrchased" if not y_test[index] else "Purchased"
    print("Predicted OUtcome: " + y_pred + "; Actual Outcome: " + actual + ";\n")
# Step 8: Print out the actual ytest values and predicted y values
# based on the xtest data
#print("Predicted OUtcome: " + y_pred + "; Actual Outcome: " + actual + ";\n")

custom_data = numpy.array([[34, 56000, 1]])
custom_scaler = StandardScaler().fit(custom_data)
custom_data = custom_scaler.transform(custom_data)
custom_prediction = model.predict(custom_data.reshape(-1, 3))[0]
print("Custom Data Outcome (Writeup):")
print("Not Purchased" if not custom_prediction else "Purchased")
