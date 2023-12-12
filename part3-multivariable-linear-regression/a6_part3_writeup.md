# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
0.86, which tells us the accuracy of the model. In this instance, it appears to be relatively accurate, maybe not suuuper accurate, but accurate enough.
2. Is your model accurate? Why or why not?
 For the most part, as the R^2 value is pretty high and none of the values are "crazy looking"(as in way too high, way too low, etc.) It's definitely not perfect but still pretty decent.
3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
10 year old car: $13,801.13;  20 year old car:$9,921.77
4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
This may be because the model is decreasing linearly(?), so the predictions might end up negative if input goes higher.
