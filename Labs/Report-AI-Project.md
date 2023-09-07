# Introduction to AI
## Report - Workflow for an AI-project


I'm writing a report regarding the workflow of an AI/ML project that’s going to predict house prices.  
If you’re going to develop an AI application, to begin with, you'll need to identify the problem that you're going to solve, in this case we’re going to try and predict house prices depending on ex. *size, number of rooms, bedrooms, bathrooms, location* and so on. When you know what you’ll be working with, it’s a good idea to list out the requirements and plan out the workflow for your development.  

When you’re done with the planning and ready to start with the application, you’ll need to gather a large set of data regarding the house prices. There are different ways of gathering data, but some popular examples could be:  
- Web scraping
- APIs
- using existing datasets on either Kaggle/GitHub, 
- Sending out surveys
- Manually collecting data which would be very time-consuming.

The data you are collecting could be saved in different formats for example .json or .csv .xml. The data collected could be saved locally on your computer or preferably in a database of your choice. 

To visualize and process the data you collected you could use different packages for python, popular packages that are commonly used for data visualization is *matplotlib* and *seaborn* and then for processing the data to the format you want to work with you could use packages like *NumPy* or *pandas*.

To predict the house prices with the data collected we could use a supervised algorithm, “Linear Regression”. Linear Regression is going to try and predict the value of a variable based on one other variable. If you have a dataset with just two variables, (in our scenario it could be house price and size) and you’re applying a linear aggression algorithm to the data, it would also be called a “Simple Linear Regression”. It works in the way that we have one independent variable (house price) that the algorithm is going to try and predict depending on the dependent variable (size). 

For our scenario we would have to use a larger dataset with a larger set of different variables, which could be *size of the house, size of the garden, location, number of rooms, number of bathrooms*, etc. If we were to use a regression algorithm on the dataset described above, we would try to predict the house price (dependent value) based on the relationship of the other independent values which are known from our datasets that we collected. Also called a multiple linear regression algorithm. 
To deploy this machine learning model that you’ve written in python you could use other python packages. One common way to deploy it for visualization is a web application, you could use packages like *Flask* or *Django* for developing web applications with python.

---

Sources used for this report: 
- https://www.geeksforgeeks.org/ml-linear-regression/
- https://www.geeksforgeeks.org/best-python-libraries-for-machine-learning/
- https://chisw.com/blog/how-to-build-an-ai-app/
- https://www.kaggle.com/code/burhanykiyakoglu/predicting-house-prices/notebook
- https://waverleysoftware.com/blog/data-collection-for-machine-learning-guide/#3