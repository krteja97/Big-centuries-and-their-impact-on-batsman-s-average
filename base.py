import database_methods as db;
import player_ids as pd;
import extractor as tb;
from correlation_finder import main_correlation_finder;
import consistency_factor as cf;
import player_progress as pp;

import sqlite3
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup


#database handling

db.sslError();
dbname = 'stats.sqlite';
my_list = db.create_connection(dbname);
cur = my_list[0];
conn = my_list[1];
db.create_tables(cur); 


for pid in pd.player_ids:
	cur.execute('select player_name from players where pid = ?', (pid,));
	try:
		acct = cur.fetchone()[0]
		continue
	except:
		try:
			url = tb.create_normal_url(pid);
			curl = tb.create_centuries_url(pid);

			arg1 = tb.playerProfile(url);
			arg2 = tb.playerCenturies(curl);
			inningsperhundreds = arg1['innings']/arg1['hundreds'];
			ratio = arg2['runs_in_hundreds']/arg1['total_runs'];

			cur.execute('''insert into players (pid, player_name, innings, total_runs, runs_in_hundreds, average, hundreds,
						inningsperhundreds, ratio) values(?,?,?,?,?,?,?,?,?) ''', (pid, arg1['player_name'], arg1['innings'] ,
						arg1['total_runs'] , arg2['runs_in_hundreds'] , arg1['average'] , arg1['hundreds'] , inningsperhundreds, ratio,));
			conn.commit();
		except:
			conn.commit();

cur.close();

#main_correlation_finder(dbname);
#cf.consistency_factor('stats.sqlite');








