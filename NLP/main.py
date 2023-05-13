import pandas as pd
from sklearn.model_selection import train_test_split
from NLP_class import pre_process _and_countrazier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# Import the pandas library for data manipulation
data = pd.read_csv("emails.csv", header=None)

# Set the column names of the data
data.columns = ['text', 'label']

# Remove rows with missing values
data.dropna(inplace=True)

# Create an instance of the pre_proccess_nlp class
data_coun =  pre_process _and_countrazier()

# Perform CountVectorizer on the text column of the data
cou = data_coun.CountVectorizer_(data['text'])

# Set the features (x) and the target variable (y)
x = cou
y = data['label']

def classfire_(x, y):
    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
    
    # Create an instance of the Gaussian Naive Bayes classifier
    classfir = GaussianNB()
    
    # Fit the classifier to the training data
    classfir.fit(x_train, y_train)
    
    # Predict the target variable using the testing data
    y_pred = classfir.predict(x_test)
    
    # Compute the confusion matrix
    conf = confusion_matrix(y_test, y_pred)
    
    # Compute the accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy, conf, y_pred

# Call the classfire_ function and store the results
acc, conf, y_pred = classfire_(x, y)

# Print the accuracy score
print(acc)
