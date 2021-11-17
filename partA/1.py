import csv
factor=1.0
cnt=0
template="<rect id=\"No%d\" class=\"barchart\" x = \"%d\" y = \"%d\" width = \"19\" height = \"%d\" fill = \"steelblue\"></rect>"
h=500
maxhight=40000000
with open("state_population_gdp.tsv") as fd:
    rd = csv.reader(fd,delimiter="\t")
    for row in rd:
        population=int(row[1])
        x=cnt * 20
        cnt += 1
        y=(maxhight-population)/maxhight*h
        height=population/maxhight*h
        print(template%(cnt,x,y,height))

