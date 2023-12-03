 # Simple Linear Regression Model for Machine Learning.

#Importing dependencies
from sklearn.linear_model import LinearRegression
import random

# Two Empty Lists
feature_set = []
target_set = []

# Number of Rows in Data Set
number_of_rows = 200

# Limit Possible Values in Data Set
random_number_limit = 2000

# Create the Data Set
# Feature Data
for i in range(0, number_of_rows):
    x = random.randint(0, random_number_limit)
    y = random.randint(0, random_number_limit)
    z = random.randint(0, random_number_limit)

# Linear Function for target Data Set
    function = (10*x)+(2*y)+(3*z)

# Appened the data to the lists
    feature_set.append([x,y,z])
    target_set.append(function)

# Linear Regression Model
model = LinearRegression()
model.fit(feature_set, target_set)

# Create the test data set
test_set = [[8,10,0]] # Expect output = function(8,10,0) = (10*8)+(2*10)+(3*0) = 100
prediction = model.predict(test_set)

print("prediction:"+str(prediction)+" Coeficients:"+str(model.coef_))