import csv, sys
from string import Template

# Init the string template
s = Template("""{"type":"Feature","id":$id,"geometry":{"type":"Point","coordinates":[$long,$lat]},
    "properties":{"city":"$city","attendance":$attendance,"date":"$date"}},\n""")

# Init output file
ofile = open("us-centroids.json", "w")
ofile.write("""{"type":"FeatureCollection","features":[\n""")

filename = "swviz_data.csv"
reader = csv.reader(open(filename, "r"))

try:
	for row_num, row in enumerate(reader):
		print row
		if row_num != 0:
			ofile.write(s.substitute(long=row[0], lat=row[1], city=row[2], attendance=row[3], date=row[4], id=row_num))
except csv.Error, e:
    sys.exit("file %s, line %d: %s" % (filename, reader.line_num, e))

ofile.write("]}")
ofile.close()

