import database_methods as db;
import player_ids as pd;
import extractor as tb;
from correlation_finder import main_correlation_finder;
import consistency_factor as cf;

import sqlite3
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup
import statistics

base_progress_url = "http://www.howstat.com/cricket/Statistics/Players/PlayerProgressBat.asp?PlayerID=";


def create_player_progress_url(x):
	if(x < 100):
		url = base_progress_url + '00' + str(x);
	elif(x < 1000):
		url = base_progress_url + '0' + str(x);
	else:
		url = base_progress_url + str(x);
	print(url);
	return url;



def getNecessaryAttributes(soup):

	table = soup.find('table', attrs = {'class' : 'TableLined'});
	rows = table.findAll("tr");

	count = 0;
	length = len(rows);
	rows = rows[3:-1];
	cur_runs = 0;
	check_last_innings = False;

	innings_list = [];
	innings_list_withNotout = [];

	for row in rows:
		cells = row.findAll("td");
		innings = cells[6].text.split()[0];

		if(innings != '-' and innings != 'DNB*'):
			if(innings[-1] == '*'):
				check_last_innings = True;
				innings = innings[:-1];
				cur_runs += int(innings);
				innings_list_withNotout.append(int(innings));
			else:
				check_last_innings = False;
				cur_runs += int(innings);
				innings_list.append(cur_runs);
				cur_runs = 0;
				innings_list_withNotout.append(int(innings));

	if(check_last_innings == True):
		innings_list.append(cur_runs);


	standard_deviation = statistics.stdev(innings_list);
	mean = statistics.mean(innings_list);
	standard_deviationNO = statistics.stdev( innings_list_withNotout);
	print(standard_deviationNO);
	print(len(innings_list_withNotout));
	print(mean)
	print(standard_deviation);
	return {'mean' : mean, 'std_deviation' : standard_deviation, 'stddev2' : standard_deviationNO};




def myPlayerRuns():
	ctx = db.sslError();
	dbname = 'stats.sqlite';
	my_list = db.create_connection(dbname);
	cur = my_list[0];
	conn = my_list[1];

	tlist = cur.execute('select pid from players where stddev2 is NULL');
	playerid_list = tlist.fetchall();
	playerid_list = [x[0] for x in playerid_list];

	for x in playerid_list:
		url = create_player_progress_url(x);
		page = urllib.request.urlopen(url, context = ctx);
		soup = BeautifulSoup(page, 'html.parser');

		arg = getNecessaryAttributes(soup);

		cur.execute('''update players set mean = ? where pid = ?''', (arg['mean'], x,));
		cur.execute('''update players set std_deviation = ? where pid = ?''', (arg['std_deviation'], x,));
		cur.execute('''update players set stddev2 = ? where pid = ?''',(arg['stddev2'],x,));
	
		conn.commit();


	cur.close();

#calling my functions
myPlayerRuns();