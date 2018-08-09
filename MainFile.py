import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import prediction
dates = []
prices = []

def getdata(filename):
    with open(filename,'r') as csvfile:
        csvfilereader = csv.reader(csvfile)
        next(csvfilereader)
        for row in csvfilereader:
            dates.append(int (row[0].split('-')[0]))
            prices.append(float(row[1]))

    return


def predict_price(dates,prices,x):
    dates = np.reshape(dates,(len(dates),1))

    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

    svr_lin.fit(dates,prices)
    svr_rbf.fit(dates,prices)
    svr_poly.fit(dates,prices)

    plt.scatter(dates, prices, color='black', label = 'Data')
    plt.plot(dates, svr_rbf.predict(dates),label = 'RBF')
    plt.plot(dates, svr_lin.predict(dates),label = 'Linear')
    plt.plot(dates, svr_poly.predict(dates),label = 'Polynomial')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('The Prophet')
    plt.legend()
    plt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]


getdata('aapl.csv')

y = input("enter the date :")

predictprices = predict_price(dates, prices, y)

print(predictprices)

