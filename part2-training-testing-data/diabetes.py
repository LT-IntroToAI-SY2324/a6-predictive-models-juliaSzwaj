import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = load_diabetes(as_frame=True)
y = data.target
data = data.frame
#print(data)
x = data["bmi"].values

x = x.reshape(-1, 1)

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.10)
#create the model
model = LinearRegression().fit(xtrain, ytrain)

#get the coef_, intercept_ values and r^2 values
#use float() to turn the arrays into a single float value
coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(xtrain, ytrain)

#print out the linear equation and r^2 value
print("Model's Linear Equation: y=", coef, "x+", intercept)
print("R Squared value: ", r_squared)

'''
**********TEST THE MODEL**********
'''

# get the predicted y values for teh xtest values - returns an array of the results
predict = model.predict(xtest)
#round the value in the np array to 2 decimal places
predict = np.around(predict, 2)

#compare te actual and predicted values
print("\nTesting Linear Model with Testing Data:")
for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]
    #print("x value:", float(x_coord), "Predicted y values:", predicted_y"Actual y value:", "actual")

#start here ^^^^^^^

#graph the data
# sets the size of the graph
plt.figure(figsize=(6,4))

# creates a scatter plot and labels the axes
plt.scatter(x,y)
plt.xlabel("Temperature °F")
plt.ylabel("Chirps per Minute")
plt.title("Cricket Chirps by Temperature")

# prints the correlation coefficient
print(f"Correlation between Temperature and Chirps/Min: {x.corr(y)}")

# show the plot
plt.show()