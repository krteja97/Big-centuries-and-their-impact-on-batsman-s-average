import database_methods as db;
import sqlite3
import numpy as np;
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plot


db_name = 'stats.sqlite'
conn = sqlite3.connect(db_name);
cur = conn.cursor();

average_list = cur.execute('select average from players where innings > 50');
average_list = average_list.fetchall();
average_list = [x[0] for x in average_list];

list1 = cur.execute('select ratio from players where innings > 50');
ratio_list = list1.fetchall();
ratio_list = [x[0] for x in ratio_list];
list1 = cur.execute('select inningsperhundreds from players where innings > 50');
iph_list = list1.fetchall();
iph_list = [x[0] for x in iph_list];    

hpi_list = [];
for x in iph_list:
	hpi_list.append(1/x);

average_list = np.array(average_list).reshape(-1,1);
ratio_list = np.array(ratio_list).reshape(-1,1);

xTrain, xTest, yTrain, yTest = train_test_split(ratio_list, average_list, test_size = 0.2, random_state = 0);
linearRegressor = LinearRegression();

linearRegressor.fit(xTrain, yTrain);
print(linearRegressor.coef_)
yPrediction = linearRegressor.predict(xTest)

print(len(average_list))

plot.scatter(xTrain, yTrain, color = 'red')
plot.plot(xTrain, linearRegressor.predict(xTrain), color = 'blue')
plot.title('average vs ratio (Training set)')
plot.xlabel('ratio')
plot.ylabel('average')


plot.scatter(xTest, yTest, color = 'green')
plot.plot(xTrain, linearRegressor.predict(xTrain), color = 'yellow')
plot.title('average vs ratio (Test set)')
plot.xlabel('ratio')
plot.ylabel('average')
plot.show()

accuracy = linearRegressor.score(xTest,yTest)
print(accuracy*100,'%')


