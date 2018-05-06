import math
def distance_sqair_F(point1,point2):
	return sum(sqair_F(subtact_F(point1,point2)))
def subtact_F(point1,point2):
	sub=[""]*len(point1)
	for x in range(len(sub)):
		sub[x]=point1[x]-point2[x]
	return sub
def sqair_F(point1):
	sq=[""]*len(point1)
	for x in range(len(point1)):
		sq[x]=point1[x]**2
	return sq
def mult_F(point1,mut):
	her=[""]*len(point1)
	for x in range(len(her)):
		her[x]=point1[x]*mut
	return her
def add_F(point1,point2):
	ret=[""]*len(point1)
	for x in range(len(point1)):
		ret[x]=point1[x]+point2[x]
	return ret
# form [[mass],#pos#[ x,y,z],#velocity#[x,y,z],#force#[x,y,z],#conection#[to,[lanth,consent],mut_F]
def coler_F(poin1,poin2,consent):#con[string constent, string lanth]
	#print(poin1)
	#print(poin2)
	dis=math.sqrt(distance_sqair_F(poin1,poin2))
	con=consent[0]
	#print("ther")
	#print(consent)
	#print(dis)
	#print(con)
	if (dis-con)>=0:
		this=consent[1]*(dis-con)/con
		rep=3**(-((this)**2)**(1/4))
		#print("go")
		#print(rep)
		#print([1,rep,rep])
		return [1,rep,rep]
	else:
		this=consent[1]*(dis-con)/dis
		rep=3**(-((this)**2)**(1/4))
		#print([rep,rep,1])
		return [rep,rep,1]

	return [1,1,1]
gravity=0
print("thos")
def scailcon_F(poin1,poin2,consent):
	dis=math.sqrt(distance_sqair_F(poin1,poin2))/8
	return [dis,(1/dis)*consent[0],(1/dis)*consent[0]]


def get_lis_F(this):
	lis=this[0]
	for x in range(len(this[1])):
		lis=lis[this[1][x]]
	return lis


def makestring_F(point):
	return ""+str(point[0])+","+str(point[1])+","+str(point[2])+""

def exple_dis_F(time,points):
	print(time)
	return [math.sin(time),math.cos(time),math.sin(time),points[3],points[4]]


def pos_dis1_F(time,points,y):
	#print(time)
	x=math.sin(time)*points[3][0]+points[3][1]
	y=points[3][2]
	z=points[3][3]
	return [x,y,z,points[3],points[4]]

def pos_dis2_F(time,points,y):
	x=points[3][1]
	y=points[3][2]+math.sin(time)*points[3][0]
	z=points[3][3]
	return [x,y,z,points[3],points[4]]

def vec(end,start) :
	k=[""]*3
	c=[""]*3
	t=[""]*3
	t[0]=start[0]
	t[1]=start[1]
	t[2]=start[2]
	c[0]=end[0]
	c[1]=end[1]
	c[2]=end[2]
	k[0]=c[1]
	k[1]=c[0]
	k[2]=c[2]
	k[1]=k[1]-t[0]
	k[0]=k[0]-t[1]
	k[2]=k[2]-t[2]
	c=k
	h=[c[0],c[1],c[2]]
	lit=c[1]
	
	if c[1]!=0 or c[2]!=0 or c[0]!=0:

		if c[1]!=0 and c[0]!=0:
			thata=math.pi/2-math.atan(c[1]/c[0])
		if c[1]==0 or c[0]==0:
			thata=0
		pi=math.pi/2-math.acos(c[2]/math.sqrt(c[0]**2+c[1]**2+c[2]**2))

		rect=[c[1]/2,c[0]/2,c[2]/2]
	##where to change arrow lanth
		scail=math.sqrt(c[0]**2+c[1]**2+c[2]**2)/8
	if c[1]==0 and c[2]==0 and c[0]==0:
		scail=0

	#good
	if c[1]>=0 and c[1]>=0:
		pi=pi
		thata=thata

	if c[0]<=0 and c[1]>=0:
		pi=pi
		thata=thata
	if c[0]>=0 and c[1]<=0:
		pi=math.pi-pi
		thata=thata
	#good
	if c[0]<=0 and c[1]<=0:
		pi=math.pi-pi
		thata=thata
	if c[1]==0:
	    if c[0]>=0:
	        thata=-math.pi/2
	    if c[0]<=0:
	        thata=math.pi/2
	if c[0]==0:
	    if c[1]>=0:
	        thata=0
	    if c[1]<=0:
	        thata=math.pi
	thata=thata
	if c[0]<=0 and c[1]<=0:
		thata=thata+math.pi
	if c[0]>=0 and c[1]>=0:
		thata=thata+math.pi
	return [rect[0]+t[0],rect[1]+t[1],rect[2]+t[2],scail,-pi,thata+math.pi]

#formpoint,topoint,thing_that_goesto_colerF,coler_F,thing_that_goes_to_scail_function,
#conectionlist[0]=[0,1,[0.5,1],coler_F,[0.01,2],scailcon_F]

def mut_F(ten,number):#ten is [[string consetn,string lanth,pointat,pointfrom],mult_f]
	#ten[0][2] is points
	pos1=get_lis_F(ten[0][2])[0:3]
	pos2=get_lis_F(ten[0][3])[0:3]
	dis=math.sqrt(distance_sqair_F(pos1,pos2))
	mult=ten[0][0]*(dis-ten[0][1])#ten[0][1] is string consent ten[0][2] is spring lanth
	if dis:
		mult=mult/dis
	else:
		mult=0

	vec=mult_F(subtact_F(pos2,pos1),-mult)
	return [vec,ten]



def grave_F(ten,number):
	return [ten[0][0],ten]


conectionlist=[""]*0


points=[""]*6

points[0]=[""]*4
points[0][0]=[1]
points[0][1]=[0,0,0,[0.1,0,0,0],pos_dis2_F]
points[0][2]=[0,0,0]
points[0][3]=[0,0,0]


points[1]=[""]*4
points[1][0]=[1]
points[1][1]=[0,1,0,[0.1,0,1,0],pos_dis2_F]
points[1][2]=[0,0,0]
points[1][3]=[0,0,0]



points[2]=[""]*4
points[2][0]=[1]
points[2][1]=[0,0,1]
points[2][2]=[0,0,0]
points[2][3]=[0,0,0]
points[2].append([[[0,0,-0.1]],grave_F])





points[3]=[""]*4
points[3][0]=[1]
points[3][1]=[0,1,1]
points[3][2]=[0,0,0]
points[3][3]=[0,0,0]
points[3].append([[[0,0,-0.1]],grave_F])










conectionlist.append([0,1,[1,1],coler_F,[0.01,2],scailcon_F])


points[2].append([[1,1,[points,[0,1]],[points,[2,1]]],mut_F])
conectionlist.append([0,2,[1,1],coler_F,[0.01,2],scailcon_F])


points[3].append([[1,1,[points,[1,1]],[points,[3,1]]],mut_F])
conectionlist.append([1,3,[1,1],coler_F,[0.01,2],scailcon_F])


points[3].append([[1,1,[points,[2,1]],[points,[3,1]]],mut_F])
points[2].append([[1,1,[points,[3,1]],[points,[2,1]]],mut_F])
conectionlist.append([2,3,[1,1],coler_F,[0.01,2],scailcon_F])



points[2].append([[1,math.sqrt(2),[points,[1,1]],[points,[2,1]]],mut_F])
conectionlist.append([1,2,[math.sqrt(2),1],coler_F,[0.01,2],scailcon_F])


points[3].append([[1,math.sqrt(2),[points,[0,1]],[points,[3,1]]],mut_F])
conectionlist.append([0,3,[math.sqrt(2),1],coler_F,[0.01,2],scailcon_F])





this=[0,0,0]

#print(points[0][0][1:])

velocityvecaddlist=[""]*3
velocityvecaddlist[0]=0
velocityvecaddlist[1]=1
velocityvecaddlist[2]=2


forcevecaddlist=[""]*3
forcevecaddlist[0]=0
forcevecaddlist[1]=1
forcevecaddlist[2]=2



add=""
#make#
stl="stl3.stl"
for x in range(len(points)):
	add=add+"o,point"+str(x)+","+stl+"\n"
#addconection#

conadd=""
for x in range(len(conectionlist)):
	coname=str(conectionlist[x][0])+"><"+str(conectionlist[x][1])
	#print(coname)
	conadd=conadd+"o,con"+coname+",line.stl\n"

veladd=""
#make#
stl="ves.stl"
for x in range(len(velocityvecaddlist)):
	veladd=veladd+"o,vel"+str(velocityvecaddlist[x])+","+stl+"\n"


forceadd=""
#make#
stl="ves.stl"
for x in range(len(forcevecaddlist)):
	forceadd=forceadd+"o,forc"+str(forcevecaddlist[x])+","+stl+"\n"



wrt=""
wrt=wrt+add+conadd+veladd
#scails the points
scail=0.1
# amount of time 
time=0.01
timesperfram=5
skipingfram=1
for timer in range(500):
	for y in range(len(points)):
		pos=points[y][1][0:3]
		#resets force
		points[y][3]=[0,0,0]
		#part that adds the tention forces
		for x in range(len(points[y])-4):
			frce=points[y][4+x][1](points[y][4+x],y)
			points[y][3][0:3]=add_F(points[y][3][0:3],frce[0])
			points[y][4+x]=frce[1]
		if len(points[y][1])==5:
			points[y][1]=points[y][1][4](time*timer,points[y][1],y)
		else:
			points[y][2]=add_F(points[y][2],mult_F(points[y][3],time))
			points[y][1]=add_F(points[y][1],mult_F(points[y][2],time))
	scails=""
	
	
	if timer%timesperfram==0:
		frame=(timer*skipingfram)//timesperfram
		for x in range(len(points)):
			scails=scails+"s,point"+str(x)+","+str(points[x][0][0]*scail)+","+str(frame)+"\n"
			#makeslocations of points#


		locations=""

		for x in range(len(points)):
			triplet=","+str(points[x][1][0])+","+str(points[x][1][1])+","+str(points[x][1][2])
			#print(points[x][1])
			locations=locations+"l,point"+str(x)+","+makestring_F(points[x][1])+","+str(frame)+"\n"



		#conections#
		moveconections=""
		for x in range(len(conectionlist)):
			coname="con"+str(conectionlist[x][0])+"><"+str(conectionlist[x][1])
			place1=points[conectionlist[x][0]][1]
			place2=points[conectionlist[x][1]][1]
			place_of_con=vec(place1,place2)
			moveconections=moveconections+"l,"+coname+","+makestring_F(place_of_con[0:3])+","+str(frame)+"\n"
			moveconections=moveconections+"a,"+coname+","+makestring_F([0,place_of_con[4],place_of_con[5]])+","+str(frame)+"\n"
		#conection color
		colorcon=""
		for x in range(len(conectionlist)):
			coname="con"+str(conectionlist[x][0])+"><"+str(conectionlist[x][1])
			place1=points[conectionlist[x][0]][1][0:3]
			place2=points[conectionlist[x][1]][1][0:3]
			color=conectionlist[x][3](place1,place2,conectionlist[x][2])
			colorcon=colorcon+"c,"+coname+","+makestring_F(color)+","+str(frame)+"\n"
		#where the scailing of is done
		scailcon=""
		for x in range(len(conectionlist)):
			coname="con"+str(conectionlist[x][0])+"><"+str(conectionlist[x][1])
			place1=points[conectionlist[x][0]][1][0:3]
			place2=points[conectionlist[x][1]][1][0:3]
			sccail=conectionlist[x][5](place1,place2,conectionlist[x][4])
			makestring_F(sccail)
			scailcon=scailcon+"sc,"+coname+","+makestring_F(sccail)+","+str(frame)+"\n"
		# where the velocity arows come from
		stl="ves.stl"
		velmake=""
		for x in range(len(velocityvecaddlist)):
			place1=points[velocityvecaddlist[x]][1][0:3]
			place2=points[velocityvecaddlist[x]][2][0:3]
			if place2==[0,0,0]:
				place2=[0.001,0,0]
			place2=add_F(place1,place2)
			velmake=velmake+"arw,vel"+str(velocityvecaddlist[x])+","+makestring_F(place2)+","+makestring_F(place1)
			velmake=velmake+","+stl+","+str(frame)+"\n"
		#where the force arows come form
		stl="ves.stl"
		forcemake=""
		for x in range(len(forcevecaddlist)):
			place1=points[forcevecaddlist[x]][1][0:3]
			place2=points[forcevecaddlist[x]][3][0:3]
			if place2==[0,0,0]:
				place2=[0.001,0,0]
			place2=add_F(place1,place2)
			forcemake=forcemake+"arw,forc"+str(forcevecaddlist[x])+","+makestring_F(place2)+","+makestring_F(place1)
			forcemake=forcemake+","+stl+","+str(frame)+"\n"
		#print(points[0][3])
		wrt=wrt+moveconections+scailcon+forcemake+velmake+moveconections+locations+scails+colorcon+forcemake


file = open("All.txt", "w")


file.write(wrt)
file.close()








