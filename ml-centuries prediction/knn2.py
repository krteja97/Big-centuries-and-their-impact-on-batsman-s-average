

import database_methods as db;
import sqlite3
import numpy as np;
import matplotlib.pyplot as plot
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import mean_squared_error
from sklearn import neighbors
from math import sqrt  

db_name = 'stats.sqlite'
conn = sqlite3.connect(db_name);
cur = conn.cursor();


average_list = cur.execute('select average from players where innings > 35');
average_list = average_list.fetchall();
average_list = [x[0] for x in average_list];

iph_list = cur.execute('select inningsperhundreds from players where innings > 35');
iph_list = iph_list.fetchall();
iph_list = [x[0] for x in iph_list];    

hpi_list = [];
for x in iph_list:
	hpi_list.append(1/x);


stddev2_list = cur.execute('select average - stddev2 from players where innings > 35');
stddev2_list = stddev2_list.fetchall();
stddev2_list = [x[0] for x in stddev2_list];

ratio_list = cur.execute('select ratio from players where innings > 35');
ratio_list = ratio_list.fetchall();
ratio_list = [x[0] for x in ratio_list];

###########################################################################

# average_list = preprocessing.scale(average_list)
# iph_list = preprocessing.scale(iph_list)
# stddev2_list = preprocessing.scale(stddev2_list)

x = np.array([hpi_list,stddev2_list,ratio_list]).reshape(-1,3);
xTrain, xTest, yTrain, yTest = train_test_split(x, average_list, test_size = 0.3, random_state = 0);



#############################################################################


rmse_val = [] #to store rmse values for different k
k_list = [];

for k in range(30):
	k = k + 1;
	k_list.append(k)
	model = neighbors.KNeighborsRegressor(n_neighbors = k)
	model.fit(xTrain, yTrain)  #fit the model
	pred=model.predict(xTest) #make prediction on test set
	error = sqrt(mean_squared_error(yTest,pred)) #calculate rmse
	rmse_val.append(error) #store rmse values
	print('RMSE value for k= ' , k , 'is:', error);


##############################################################################

##find for k = 10
model = neighbors.KNeighborsRegressor(n_neighbors = 7)
model.fit(xTrain,yTrain)
pred = model.predict(xTest)
error = sqrt(mean_squared_error(yTest,pred))


i = 0;
for x in xTest:
	print(yTest[i], pred[i])
	i = i + 1;

plot.plot(rmse_val,k_list)
plot.show();


