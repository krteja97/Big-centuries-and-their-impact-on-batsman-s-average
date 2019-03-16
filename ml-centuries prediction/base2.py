import database_methods as db;
import sqlite3
import numpy as np;
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plot


db_name = 'stats.sqlite'
conn = sqlite3.connect(db_name);
cur = conn.cursor();

average_list = cur.execute('select average from players where innings > 35');
average_list = average_list.fetchall();
average_list = [x[0] for x in average_list];

list1 = cur.execute('select stddev2 from players where innings > 35');
dev_list = list1.fetchall();
dev_list = [x[0] for x in dev_list];



average_list = np.array(average_list).reshape(-1,1);
dev_list = np.array(dev_list).reshape(-1,1);

xTrain, xTest, yTrain, yTest = train_test_split(dev_list, average_list, test_size = 0.3, random_state = 0);
linearRegressor = LinearRegression();

linearRegressor.fit(xTrain, yTrain);
print(linearRegressor.coef_)
yPrediction = linearRegressor.predict(xTest)

print(len(average_list))

plot.scatter(xTrain, yTrain, color = 'red')
plot.plot(xTrain, linearRegressor.predict(xTrain), color = 'blue')
plot.title('average vs dev (Training set)')
plot.xlabel('dev ')
plot.ylabel('average')


plot.scatter(xTest, yTest, color = 'green')
plot.plot(xTrain, linearRegressor.predict(xTrain), color = 'yellow')
plot.title('average vs dev (Test set)')
plot.xlabel('dev')
plot.ylabel('average')
plot.show()

accuracy = linearRegressor.score(xTest,yTest)
print(accuracy*100,'%')


