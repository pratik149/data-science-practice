import pandas

iris=pandas.read_excel("Iris.xls")
#print(iris)

#For knowing the attributes/features present in the data
column=iris.columns.values
print(column)

#Splitting attributes into predictors and target variable in X and Y respectively
X=iris[column[0:4]] #0 to 3 columns
Y=iris[column[4]] #or column[-1] #last target column

#print(X) #printing predictors
#print(Y) #printing target variable

#Importing train-test-split library
from sklearn.model_selection import train_test_split

#splitting train and test data
x_train, x_test, y_train, y_test = train_test_split(X,Y,train_size=0.7)
#order of variable should be same i.e x,x,y,y

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

#Importing the model which is suitable for the problem
from sklearn.neighbors import KNeighborsClassifier
#initializing the model
knn = KNeighborsClassifier(n_neighbors=5)

#fitting a model and training a model is one and the same thing
knn.fit(x_train,y_train)

#Storing predcited values of x-test by our model in variable yprd
yprd=knn.predict(x_test)
#print(yprd) #Predicated Values
#print(y_test) #Actual values

#Importing accuracy metric for validating the performance
from sklearn.metrics import accuracy_score

accuracy= accuracy_score(y_test,yprd)
print(accuracy)


khanasmatara5@gmail.com


