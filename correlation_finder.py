import numpy as np;
import sqlite3
import database_methods as db;
import matplotlib.pyplot as plt 

def main_correlation_finder(db_name):
	my_list = db.create_connection(db_name);
	cur = my_list[0];
	conn = my_list[1];

	list1 = cur.execute('select average from players');
	average_list = list1.fetchall();
	average_list = [x[0] for x in average_list];
	list1 = cur.execute('select ratio from players');
	ratio_list = list1.fetchall();
	ratio_list = [x[0] for x in ratio_list];
	list1 = cur.execute('select inningsperhundreds from players');
	iph_list = list1.fetchall();
	iph_list = [x[0] for x in iph_list];
	

	hpi_list = [];
	for x in iph_list:
		hpi_list.append(1/x);

	print(np.corrcoef(average_list,ratio_list)[0,1]);
	print(np.corrcoef(iph_list,ratio_list)[0,1]);
	print(np.corrcoef(iph_list,average_list)[0,1]);
	print(np.corrcoef(hpi_list,ratio_list)[0,1]);
	print(np.corrcoef(hpi_list,average_list)[0,1]);


	plt.plot(hpi_list,ratio_list);
	plt.xlabel('hpi - axis')  
	plt.ylabel('ratio - axis') 
	plt.show();


# 0.8215157467745133
#-0.8369503089338763
#-0.6530067302051804
# 0.9053118438658443
# 0.9335265302923701

# the correlation coefficients for above problem statement,very high, hypothesis is correct


