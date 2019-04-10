#lets apply k means algorithm

import database_methods as db;
import sqlite3
import numpy as np;
import matplotlib.pyplot as plot
from sklearn import preprocessing
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D



db_name = 'stats.sqlite'
conn = sqlite3.connect(db_name);
cur = conn.cursor();


average_list = cur.execute('select average from players where innings > 35');
average_list = average_list.fetchall();
average_list = [x[0] for x in average_list];

list1 = cur.execute('select inningsperhundreds from players where innings > 35');
iph_list = list1.fetchall();
iph_list = [x[0] for x in iph_list];    

hpi_list = [];
for x in iph_list:
	hpi_list.append(1/x);


stddev2_list = cur.execute('select stddev2 from players where innings > 35');
stddev2_list = stddev2_list.fetchall();
stddev2_list = [x[0] for x in stddev2_list ];



averageN_list = preprocessing.scale(average_list);
hpiN_list = preprocessing.scale(hpi_list);
stddev2N_list = preprocessing.scale(stddev2_list);


fig = plot.figure()
ax = Axes3D(fig);

ax.scatter(averageN_list,hpiN_list,stddev2N_list);
ax.set_xlabel('average');
ax.set_ylabel('hpi');
ax.set_zlabel('stddev2');
plot.show();

plot.scatter(averageN_list,stddev2N_list, color = 'pink');
plot.show();

