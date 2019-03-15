from sklearn.tree import DecisionTreeRegressor;
from sklearn.model_selection import train_test_split
import pandas as pd;
import sqlite3
import numpy as np;

db_name = 'stats.sqlite'
conn = sqlite3.connect(db_name);
cur = conn.cursor();

average_list = cur.execute('select average from players where innings > 35');
average_list = average_list.fetchall();
average_list = [x[0] for x in average_list];

list1 = cur.execute('select ratio from players where innings > 35');
ratio_list = list1.fetchall();
ratio_list = [x[0] for x in ratio_list];
list1 = cur.execute('select inningsperhundreds from players where innings > 35');
iph_list = list1.fetchall();
iph_list = [x[0] for x in iph_list];    

hpi_list = [];
for x in iph_list:
	hpi_list.append(1/x);

average_list = np.array(average_list).reshape(-1,1);
ratio_list = np.array(ratio_list).reshape(-1,1);
hpi_list = np.array(hpi_list).reshape(-1,1);  

xTrain, xTest, yTrain, yTest = train_test_split(hpi_list, average_list, test_size = 0.2, random_state = 0);  
    
regressor = DecisionTreeRegressor(random_state = 0);
regressor.fit(xTrain, yTrain);
ypred = regressor.predict(xTest); 

from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(yTest, ypred))  
print('Mean Squared Error:', metrics.mean_squared_error(yTest, ypred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(yTest, ypred)))

yTest = yTest.reshape(1,-1);

yTest = yTest[0]
#print(yTest);
#print(ypred)

df=pd.DataFrame({'Actual':yTest, 'Predicted':ypred})  
print(df)
