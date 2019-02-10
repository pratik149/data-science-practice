import pandas

iris=pandas.read_excel(r"C:\Users\Pratik\PycharmProjects\DS&ML\Iris.xls")
#print(iris)

column=iris.columns.values
print(column)

X=iris[column[0:4]] #0 to 3 columns
Y=iris[column[4]] #or column[-1] #last target column

#print(X)
#print(Y)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X,Y,train_size=0.7)
#order of variable should be same i.e x,x,y,y

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

from sklearn.linear_model import LogisticRegression

lrmodel=LogisticRegression()

#fitting a model and training a model is one and the same thing

lrmodel.fit(x_train,y_train)
print(lrmodel.coef_) #coefficients for logictic quation #Assignment

print(lrmodel.intercept_) #Assignment

yprd=lrmodel.predict(x_test)
#print(yprd) #Predicated Values
#print(y_test) #Actual values

from sklearn.metrics import accuracy_score

accuracy= accuracy_score(y_test,yprd)
print(accuracy)

