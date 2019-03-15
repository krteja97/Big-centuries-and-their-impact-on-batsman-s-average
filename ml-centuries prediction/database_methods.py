import sqlite3
import ssl

def create_connection(db_name):
		conn = sqlite3.connect(db_name);
		cur = conn.cursor();
		return [cur,conn];


def create_tables(cur):
	cur.execute(''' create table if not exists players 
                (pid integer, player_name text, innings integer, total_runs integer, runs_in_hundreds integer, average real,
                 hundreds integer, inningsperhundreds real, ratio real)''');


def sslError():
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	return ctx ;