#this has diff classes

import database_methods as db;
import sqlite3
import numpy as np;
import matplotlib.pyplot as plot
from sklearn import preprocessing

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



averageN_list = preprocessing.scale(average_list);
hpiN_list = preprocessing.scale(hpi_list);


plot.scatter(averageN_list, hpiN_list, color = 'blue');

#####################################----------------------players abpve average > 50 ##############


a50_list = [];
hpi50_list = [];

i=0;
for x in average_list:
	if(x >= 50):
		a50_list.append(averageN_list[i]);
		hpi50_list.append(hpiN_list[i]);

	i = i + 1;

plot.scatter(a50_list,hpi50_list, color = 'green');



####################################---------------------------players between 45 and 50 ############


a45_list = [];
hpi45_list = [];

i=0;
for x in average_list:
	if(x >= 45 and x < 50):
		a45_list.append(averageN_list[i]);
		hpi45_list.append(hpiN_list[i]);

	i = i + 1;

plot.scatter(a45_list,hpi45_list, color = 'red');


####################################------------------------players between 40 and 45 ##############

a40_list = [];
hpi40_list = [];

i=0;
for x in average_list:
	if(x >= 40 and x < 45):
		a40_list.append(averageN_list[i]);
		hpi40_list.append(hpiN_list[i]);

	i = i + 1;

plot.scatter(a40_list,hpi40_list, color = 'orange');


###################################------------------------players btwn 30 and 35 ################

a30_list = [];
hpi30_list = [];

i=0;
for x in average_list:
	if(x >= 30 and x < 40):
		a30_list.append(averageN_list[i]);
		hpi30_list.append(hpiN_list[i]);

	i = i + 1;

plot.scatter(a30_list,hpi30_list, color = 'yellow');


####################################-----------------final--------------------------###########

plot.show();