csv_data = reader('swviz_data.csv')

# Init output file
ofile = open('us-centroids.json', 'w')

# Init the string template
s = Template("""{"type":"Feature","id":"25","geometry":{"type":"Point","coordinates":[$long,$lat]},"properties":{"city":$city,"attendance":$attendance,"date":$date,"ein":$ein}},""")

for row in csv_data:
	lat = tbd
	long = 
	attendance = tbd
	city = tbd
	date = tbd
	ofile.write(s.substitute(lat=lat, long=long, city=city, attendance=attendance))

csv_data.close()
ofile.close()