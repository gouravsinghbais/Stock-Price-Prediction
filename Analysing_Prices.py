import  csv
import pandas
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.legend as lg
import matplotlib.pyplot as plt
import matplotlib.text
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
dates = []
prices = []
with open('aapl.csv', 'r') as csvfile:
    csv_file = csv.reader(csvfile)
    next(csv_file)
    for row in csv_file :
        dates.append(int(row[0].split('-')[0]))
        prices.append(float(row[1]))
print(dates)
print(prices)

plt.scatter(dates,prices,color = 'black',label = 'prices on dates')
plt.xlabel('Date')
plt.ylabel('Prices')
plt.plot(dates,prices,color = 'blue')
plt.title('The Prophet : Analysis', color = 'red')
plt.legend()
plt.show()
