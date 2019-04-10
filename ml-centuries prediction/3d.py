from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import sqlite3
import numpy as np;
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


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

# average_list = np.array(average_list).reshape(-1,1);
# ratio_list = np.array(ratio_list).reshape(-1,1);
# hpi_list = np.array(hpi_list).reshape(-1,1);


# averageN_list = preprocessing.scale(average_list);
# hpiN_list = preprocessing.scale(hpi_list);
# ratioN_list = preprocessing.scale(ratio_list);

fig = plt.figure();
ax = fig.add_subplot(111, projection='3d')
p = ax.scatter(average_list, ratio_list, hpi_list, c= average_list, marker='o');
# cbar = plt.colorbar(pnt3d);
# cbar.set_label("Values (units)")

fig.colorbar(p);

ax.set_xlabel('avergae')
ax.set_ylabel('ratio')
ax.set_zlabel('hpi_list')
plt.show();
