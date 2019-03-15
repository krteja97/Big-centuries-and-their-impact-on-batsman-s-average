import database_methods as db;

import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

#base links for web scrapping
base_centuries_url = "http://www.howstat.com/cricket/statistics/Players/PlayerNotables.asp?PlayerID="
base_player_url = "http://www.howstat.com/cricket/statistics/Players/PlayerOverview.asp?PlayerId=";


def create_normal_url(x):
	if(x < 100):
		url = base_player_url + '00' + str(x);
	elif(x < 1000):
		url = base_player_url + '0' + str(x);
	else:
		url = base_player_url + str(x);
	print(url);
	return url;

def create_centuries_url(x):
	if(x < 100):
		curl = base_centuries_url + '00' + str(x) + '&s=2'
	elif(x < 1000):
		curl = base_centuries_url + '0' + str(x) + '&s=2'
	else:
		curl = base_centuries_url + str(x) + '&s=2'
	print(curl);
	return curl;


def get_player_name(soup):
	player = soup.find('td', attrs = {'class' : 'TextGreenBold12'})
	player_name = player.text.split()[0] + " " + player.text.split()[1] + " " + player.text.split()[2] ;
	return player_name;


def get_total_runs(soup):
	span_name = soup.find('span', string="Aggregate:");
	tag_name = span_name.parent.parent;
	cells = tag_name.findAll("td");
	aggregate = cells[1].text.split()[0];
	return int(aggregate);

def get_average(soup):
	average_row = soup.find('span', string = "Average:");
	average_tds = average_row.parent.parent;
	cells = average_tds.findAll("td");
	average = cells[1].text.split()[0];
	return float(average);

def get_innings(soup):
	span_name = soup.find('span', string="Innings:");
	tag_name = span_name.parent.parent;
	cells = tag_name.findAll("td");
	child1 = cells[1].find("a", recursive=False)
	innings = child1.text.split()[0]
	return int(innings);

def get_hundreds(soup):
	span_name = soup.find('span', string="100s:");
	tag_name = span_name.parent.parent;
	cells = tag_name.findAll("td");
	child1 = cells[1].find("a", recursive=False)
	hundreds = child1.text.split()[0]
	return int(hundreds);


def playerProfile(url):
	ctx = db.sslError();

	page = urllib.request.urlopen(url, context = ctx);
	soup = BeautifulSoup(page, 'html.parser');

	player_name = get_player_name(soup);
	total_runs = get_total_runs(soup);
	average = get_average(soup);
	innings = get_innings(soup);
	hundreds = get_hundreds(soup);
	return {'player_name' : player_name , 'innings' : innings , 'total_runs' : total_runs, 'average' : average, 'hundreds' : hundreds};




def playerCenturies(url):
	ctx = db.sslError();

	page = urllib.request.urlopen(url, context = ctx);
	soup = BeautifulSoup(page, 'html.parser');

	table_name = soup.find('table', attrs = {'class':'TableLined'});
	rows = table_name.findAll("tr");
	
	count = 0;
	total_runs = 0;
	length = len(rows);
	
	for row in rows:
		cells = row.findAll("td");
		if(count != 0 and count != length - 1):
			innings = cells[4].text.split()[0];

			if(innings[-1] == '*'):
				innings = innings[:-1];
				total_runs = total_runs + int(innings);
			else:
				total_runs = total_runs + int(innings);
		
		count = count + 1;
	return {'runs_in_hundreds' : int(total_runs)};