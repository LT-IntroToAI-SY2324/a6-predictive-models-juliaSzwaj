# Project by Julia Szwajnos :)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("final-project/sleep_data.csv")
x = data[["Age","Sleep Duration","Stress Level"]].values
y = data["Quality of Sleep"].values

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)
model = LinearRegression().fit(xtrain, ytrain)
coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y),2)

#print(f"Model's Linear Equation: y={coef[0]}x1 + {coef[1]}x2 + {intercept}")
print("R Squared value:", r_squared)

print("Results: ")
predict = model.predict(xtest)
predict = np.around(predict, 2)

print()

for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]
    x_coord = x_coord
    print(f"Age: {x_coord[0]} Sleep Duration: {x_coord[1]} Stress Level: {x_coord[2]} Predicted: {predicted_y}")

#visualizing the data (graph)
x_1 = data["Age"]
x_2 = data["Sleep Duration"]
x_3 = data["Stress Level"]
y = data["Quality of Sleep"]

fig, graph = plt.subplots(3)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("Age")
graph[0].set_ylabel("Quality of sleep")

graph[1].scatter(x_2, y)
graph[1].set_xlabel("Sleep Duratoin")
graph[1].set_ylabel("Quality of Sleep")

graph[2].scatter(x_3, y)
graph[2].set_xlabel("Stress Level")
graph[2].set_ylabel("Quality of Sleep")

print("Correlation between Age and Quality of Sleep:",round(x_1.corr(y),2))
print("Correlation between Sleep Duration and Quality of Sleep:",round(x_2.corr(y),2))
print("Correlation between Stress Level and Quality of Sleep:",round(x_3.corr(y),2))

plt.tight_layout()
plt.show()