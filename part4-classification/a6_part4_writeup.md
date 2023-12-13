# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
My model scored 0.68 whithout StandardScaler, which is lower than the previous score(0.83) This is most likely due to the fact that scaling data distributes the data evenly, and then without it your results would be disproportionate.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
The model scored a 0.83, which is accurate enough because of how close it is to 1, especially compared to without the StandardScaler.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model did pretty wel. There weren't any noticeable patterns in the incorrect answers, but it did appear that it mostly predicted Not Purchased compared to Purchased.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
The model predicts she would not buy an SUV.
