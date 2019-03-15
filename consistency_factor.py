import sqlite3

import database_methods as db;




def consistency_factor(table_name):
	my_list = db.create_connection(table_name);
	cur = my_list[0];
	conn = my_list[1];
	#cur.execute('alter table players add column consistency_factor real');
	cur.execute('update players set consistency_factor = average/ratio')
	conn.commit();
	cur.close();