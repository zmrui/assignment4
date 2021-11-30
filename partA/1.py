import csv
factor=1.0
cnt=0
template="<rect id=\"No%d\" class=\"%s\" x = \"%d\" y = \"%d\" width = \"19\" height = \"%d\" fill = \"steelblue\"></rect>"
h=500
maxhight=40000000
with open("state_population_gdp.tsv") as fd:
    rd = csv.reader(fd,delimiter="\t")
    for row in rd:
        name = str(row[0])
        population=int(row[1])
        x=cnt * 20
        cnt += 1
        y=(maxhight-population)/maxhight*h
        height=population/maxhight*h
        print(template%(cnt,name,x,y,height))


for i <- 1 to k
   for j <- 1 to k
      do if edge(i,j) is not exist 
      return false
return true
