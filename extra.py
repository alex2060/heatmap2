import csv
def get(tpe,life):
    with open(""+tpe+""+life+"", "r") as x:
        a1reader=csv.reader(x)
        a1list= []
        for row in a1reader:
            if len(row)!=0:
                a1list=a1list + [row]
    x.close()
    return a1list


heatdata=get("heatdata.txt","")
print(heatdata)

add=""
for x in range(len(heatdata)-1):
	add+="o,point"+str(x)+",cube.stl,0\n"
	point=str(heatdata[x+1][0])+","+str(heatdata[x+1][1])+","+str(float(heatdata[x+1][2])/2)
	add+="l,point"+str(x)+","+point+",1\n"
	sccail=str(float(heatdata[0][1]))+","+str(float(heatdata[0][0]))+","+str(float(heatdata[x+1][2]))
	add+="sc,point"+str(x)+","+sccail+",1\n"
file = open("All.txt", "w")


file.write(add)
file.close()
