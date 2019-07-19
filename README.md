# Big-centuries-and-their-impact-on-batsman-s-career-average

there is a high correlation between some of the parameters that i have taken into account.

1) batting average (average)
2) ratio between runs scored in hundreds and total runs scored(ratio)
3) hundreds per innings(hpi)
4) standard deviation for all the innings played without notouts(stddev2)
5) innings per hundred(iph)
6) std deviation for all innings with notouts(stddev)

the correlation coefficient observed for these cases: (minimum of 35 innings and any batsman who has
 scored atleast a century in test matches):

	(average,ratio) 	0.78
	(iph,ratio)			-0.75
	(iph,average)		-0.64
	(hpi,ratio)			0.95
	(hpi,average)		0.89
	(average,stddev)	0.90
	(stddev2,average)	0.88
	(stddev2,ratio)		0.91
	(stddev2,hpi)		0.90


high correlation is observed
so hypothesis is correct

# comparison between england players of 1990's and 2000's

the england_stats.sqlite file contains their details..
the ratios are around 0.20-0.27 for 1990's
and 0.30-0.41 for 2000's

# comparision between australian players and english players

the england_stats.sqlite file contains their details..
the ratios are around 0.20-0.27 for 1990's players

the australian_stats.sqlite file contains details for aussies.
their ratios are around 0.30-0.45 in some cases..

thats the difference i guess

