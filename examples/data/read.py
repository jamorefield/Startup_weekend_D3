import csv, sys
from string import Template

# Init the string template
s = Template("""{"type":"Feature","id":$id,"geometry":{"type":"Point","coordinates":[$long,$lat]},
    "properties":{"city":"$city","attendance":$attendance,"date":"$date"}}""")

# Init output file
ofile = open("swviz_world_data.json", "w")
ofile.write("""{"type":"FeatureCollection","features":[\n""")

filename = "swviz_world_data.csv"
reader = csv.reader(open(filename, "r"))

last_line_no = 0
for row in reader:
	last_line_no += 1

print last_line_no
reader = csv.reader(open(filename, "r"))

try:
	for row_num, row in enumerate(reader):
		if row_num != 0:
			ofile.write(s.substitute(long=row[0], lat=row[1], city=row[2], attendance=row[3], date=row[4], id=row_num))
		if row_num != last_line_no - 1 or row_num == 1:
		 	ofile.write(",\n")
except csv.Error, e:
    sys.exit("file %s, line %d: %s" % (filename, reader.line_num, e))

ofile.write("]}")
ofile.close()


