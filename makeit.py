import csv
import bpy
import math
import bpy
import time

LOC="/Users/alexhaussmann/Desktop/mathproject/"
def check(name):
	heck=1
	try :
		bpy.data.objects[str(name)]
	except:
		heck=0
	return heck
def makerode(points,name,bev,res):
	import bpy
	import math
	import pdb
	from mathutils import Vector
	coords=[""]*len(points)
	for x in range(len(points)):
		coords[x]=points[x]


	# create the Curve Datablock
	curveData = bpy.data.curves.new(name, type='CURVE')
	curveData.dimensions = '3D'
	curveData.resolution_u = 2

	# map coords to spline
	polyline = curveData.splines.new('POLY')
	polyline.points.add(len(coords)-1)
	for i, coord in enumerate(coords):
	    x,y,z = coord
	    polyline.points[i].co = (x, y, z, 1)

	# create Object
	curveOB = bpy.data.objects.new(name, curveData)
	curveData.bevel_depth = bev
	curveData.fill_mode = 'FULL'
	curveData.bevel_resolution = res



	# attach to scene and validate context
	scn = bpy.context.scene
	scn.objects.link(curveOB)
	scn.objects.active = curveOB
def vec(name,end,start) :
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
	bpy.data.objects[name].location[0] = rect[0]+t[0]
	bpy.data.objects[name].location[1] = rect[1]+t[1]
	bpy.data.objects[name].location[2] = rect[2]+t[2]

	bpy.data.objects[name].scale[0] = scail
	bpy.data.objects[name].scale[1] = scail
	bpy.data.objects[name].scale[2] = scail

	bpy.data.objects[name].rotation_euler[1] = -pi
	bpy.data.objects[name].rotation_euler[2] = thata+math.pi
	c=h

def vecc(name,end,start) :
	print("this is")
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
	bpy.data.objects[name].location[0] = rect[0]+t[0]
	bpy.data.objects[name].location[1] = rect[1]+t[1]
	bpy.data.objects[name].location[2] = rect[2]+t[2]

	bpy.data.objects[name].scale[0] = scail
	bpy.data.objects[name].scale[1] = scail
	bpy.data.objects[name].scale[2] = scail

	bpy.data.objects[name].rotation_euler[1] = -pi
	bpy.data.objects[name].rotation_euler[2] = thata+math.pi
	c=h


def vecc_no_scail(name,end,start) :
	print("this is")
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
	bpy.data.objects[name].location[0] = rect[0]+t[0]
	bpy.data.objects[name].location[1] = rect[1]+t[1]
	bpy.data.objects[name].location[2] = rect[2]+t[2]

	bpy.data.objects[name].rotation_euler[1] = -pi
	bpy.data.objects[name].rotation_euler[2] = thata+math.pi
	c=h
def vec_scail(end,start,sail) :
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

		scail=math.sqrt(c[0]**2+c[1]**2+c[2]**2)/sail
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
	back=[""]*6
	back[0]= rect[0]+t[0]
	back[1] = rect[1]+t[1]
	back[2] = rect[2]+t[2]

	back[3] = scail


	back[4] = -pi
	back[5] = thata+math.pi

	c=h
	return back
def vec(name,end,start) :
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
	bpy.data.objects[name].location[0] = rect[0]+t[0]
	bpy.data.objects[name].location[1] = rect[1]+t[1]
	bpy.data.objects[name].location[2] = rect[2]+t[2]

	bpy.data.objects[name].scale[0] = scail
	bpy.data.objects[name].scale[1] = scail
	bpy.data.objects[name].scale[2] = scail

	bpy.data.objects[name].rotation_euler[1] = -pi
	bpy.data.objects[name].rotation_euler[2] = thata+math.pi
	c=h
#works 
#what it dose is make a arow between 2 points
def get(tpe,life):
	with open(""+tpe+""+life+".txt", "r") as x:
		a1reader=csv.reader(x)
		a1list= []
		for row in a1reader:
			if len(row)!=0:
				a1list=a1list + [row]
		return a1list
	x.close()	 
#works
# get array form csv file
def ges(tpe,life):
	with open(""+tpe+""+life+".txt", "r") as x:
		a1reader=csv.reader(x)
		a1list= []
		for row in a1reader:
			if len(row)!=0:
				a1list=a1list + row
		return a1list
	x.close() 
# gets lift form csv file
def getloc(name):
	a=[""]*3
	a[0]=bpy.data.objects[str(name)].location[0]
	a[1]=bpy.data.objects[str(name)].location[1]
	a[2]=bpy.data.objects[str(name)].location[2]
	return a 
# gets loction of object
def colorset(name):
	bpy.context.scene.objects.active = bpy.data.objects[str(name)]
	activeObject = bpy.context.active_object #Set active object to variable
	mat = bpy.data.materials.new(name=str(name)) 
def color(name,c):
	bpy.context.object.active_material.diffuse_color[0] = c[0]
	bpy.context.object.active_material.diffuse_color[1] = c[1]
	bpy.context.object.active_material.diffuse_color[2] = c[2]
# looks like it works
# changes collor of object
def loc(name,r) :
	bpy.data.objects[name].location[0] = r[0]
	bpy.data.objects[name].location[1] = r[1]
	bpy.data.objects[name].location[2] = r[2]  
# changes loction of object
def scail(name,s) :
	bpy.data.objects[name].scale[0] = s
	bpy.data.objects[name].scale[1] = s
	bpy.data.objects[name].scale[2] = s 
# scails object
def rot(name,a) :
	bpy.data.objects[name].rotation_euler[0] = a[0]
	bpy.data.objects[name].rotation_euler[1] = a[1]
	bpy.data.objects[name].rotation_euler[2] = a[2]
# rotates object
def make(name,stl,location):
	bpy.ops.import_mesh.stl(filepath=location+str(stl)+"")
	bpy.context.object.name = str(name) 
# makes object given stl
#make("vet","ves.stl")
#"C:/Users/Melinda/Desktop/comp/"
def select(name):
	bpy.ops.object.select_pattern(pattern=str(name))
	bpy.context.scene.objects.active = bpy.data.objects[str(name)]
# selects an obj by name
# adds objs based on obj_f

#changes angle based on file angle_f
#changes location based on file location_f

#changes scail based on file scail_f

#changes arrows based on file arrow_f

#changes color based on file coolor_f
def scailpartal(name,s):
	bpy.data.objects[name].scale[0] = s[0]
	bpy.data.objects[name].scale[1] = s[1]
	bpy.data.objects[name].scale[2] = s[2]
def dem_F(name,dim):
	bpy.data.objects[name].dimensions[0] = dim[0]
	bpy.data.objects[name].dimensions[1] = dim[1]
	bpy.data.objects[name].dimensions[2] = dim[2]



	pass
def stuff(location):
	addobj(location,"All")
def tro(location,fil):
	a=location
	objt=get(location,fil)
	obj=[""]*2
	angle=[""]*4
	location=[""]*4
	se=[""]*2
	sec=[""]*4
	ar=[""]*2
	arw=[""]*9
	coolor=[""]*4
	for x in range(len(objt)):
		frame=objt[x][len(objt[x])-1]
		inpit=0
		try:
			bpy.context.scene.frame_current = int(frame)
		except:
			print("fail"+str(x)+"")
		if objt[x][0]=="o":
			obj[0]=objt[x][1]
			obj[1]=objt[x][2]
			if check(str(obj[0]))==0:
				make(str(obj[0]),str(obj[1]),a)
				#this give the material
				bpy.context.scene.objects.active = bpy.data.objects[str(obj[0])]
				activeObject = bpy.context.active_object
				mat = bpy.data.materials.new(name=str(obj[0]))
				activeObject.data.materials.append(mat)
				bpy.context.object.active_material.name = str(obj[0])
				bpy.context.object.active_material.name = str(obj[0])
		if objt[x][0]=="a":
			angle[0]=objt[x][1]
			angle[1]=objt[x][2]
			angle[2]=objt[x][3]
			angle[3]=objt[x][4]
			try:
				if check(str(angle[0]))==1:
					r=[float(angle[1]),float(angle[2]),float(angle[3])]
					
					rot(str(angle[0]),r)
					bpy.ops.object.select_all(action='DESELECT')
					select(str(angle[0]))
					bpy.ops.anim.keyframe_insert_menu(type='Rotation')
			except:
				print("fail"+str(x)+"")
		if objt[x][0]=="l":
			location[0]=objt[x][1]
			location[1]=objt[x][2]
			location[2]=objt[x][3]
			location[3]=objt[x][4]
			try:
				if check(str(location[0]))==1:
					l=[float(location[1]),float(location[2]),float(location[3])]
					loc(str(location[0]),l)
					bpy.ops.object.select_all(action='DESELECT')
					select(location[0])
					bpy.ops.anim.keyframe_insert_menu(type='Location')
			except:
				print("fail"+str(objt[x][0])+"")
		if objt[x][0]=="s":
			se[0]=objt[x][1]
			se[1]=objt[x][2]
			try:
				if check(str(se[0]))==1:
					s=float(se[1])
					scail(str(se[0]),s)
					bpy.ops.object.select_all(action='DESELECT')
					select(se[0])
					bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_VisualScaling')
			except:
				print("fail"+str(x)+"")
		if objt[x][0]=="sc":
			sec[0]=objt[x][1]
			sec[1]=objt[x][2]
			sec[2]=objt[x][3]
			sec[3]=objt[x][4]
			try:
				if check(str(sec[0]))==1:
					s=[float(sec[1]),float(sec[2]),float(sec[3])]
					scailpartal(str(sec[0]),s)
					bpy.ops.object.select_all(action='DESELECT')
					select(sec[0])
					bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_VisualScaling')


			except:
				print("fail"+str(x)+"")
		if objt[x][0]=="dim":
			try:
				if check(str(objt[x][1]))==1:
					s=[float(objt[x][2]),float(objt[x][3]),float(objt[x][4])]
					dem_F(str(objt[x][1]),s)
					bpy.ops.object.select_all(action='DESELECT')
					select(objt[x][1])
					bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_VisualScaling')
			except:
				print("fail"+str(x)+"")
		if objt[x][0]=="ar":
			ar[0]=objt[x][1]
			ar[1]=objt[x][2]
			if check(str(ar[0]))==1 and check(str(ar[1]))==1:
				name=str(ar[0])+"->"+str(ar[1])
				if check(name)==0:
					make(name,"ves.stl",LOC)
					#this give the material
					bpy.context.scene.objects.active = bpy.data.objects[name]
					activeObject = bpy.context.active_object
					mat = bpy.data.materials.new(name=name)
					activeObject.data.materials.append(mat)
					bpy.context.object.active_material.name = name
					bpy.context.object.active_material.name = name
		if objt[x][0]=="arw":
			print("got")
			arw[0]=objt[x][1]# name
			arw[1]=float(objt[x][2])# point1
			arw[2]=float(objt[x][3])
			arw[3]=float(objt[x][4])

			arw[4]=float(objt[x][5])# point 2
			arw[5]=float(objt[x][6])
			arw[6]=float(objt[x][7])
			arw[7]=objt[x][8]# stl
			arw[8]=float(objt[x][9])# lanth
			print(objt[x])
			if check(arw[0])==0:
				make(str(arw[0]),str(arw[7]),LOC)
			starrt=[arw[1],arw[2],arw[3]]
			endds=[arw[4],arw[5],arw[6]]
			vecc(str(arw[0]),starrt,endds)
			print("this")
			select(arw[0])
			bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_VisualScaling')
			bpy.ops.anim.keyframe_insert_menu(type='Rotation')
			bpy.ops.anim.keyframe_insert_menu(type='Location')
		if objt[x][0]=="arw_no_scail":
			print("got")
			arw[0]=objt[x][1]# name
			arw[1]=float(objt[x][2])# point1
			arw[2]=float(objt[x][3])
			arw[3]=float(objt[x][4])

			arw[4]=float(objt[x][5])# point 2
			arw[5]=float(objt[x][6])
			arw[6]=float(objt[x][7])
			arw[7]=objt[x][8]# stl
			arw[8]=float(objt[x][9])# lanth
			print(objt[x])
			if check(arw[0])==0:
				make(str(arw[0]),str(arw[7]),LOC)
			starrt=[arw[1],arw[2],arw[3]]
			endds=[arw[4],arw[5],arw[6]]
			vecc_no_scail(str(arw[0]),starrt,endds)
			print("this")
			select(arw[0])
			bpy.ops.anim.keyframe_insert_menu(type='Rotation')
			bpy.ops.anim.keyframe_insert_menu(type='Location')


		if objt[x][0]=="c":
			coolor[0]=objt[x][1]
			coolor[1]=objt[x][2]
			coolor[2]=objt[x][3]
			coolor[3]=objt[x][4]
			try:
				if check(str(coolor[0]))==1:
					k=[float(coolor[1]),float(coolor[2]),float(coolor[3])]
					bpy.ops.object.select_all(action='DESELECT')
					select(str(coolor[0]))
					color(str(coolor[0]),k)
					bpy.context.object.active_material.keyframe_insert("diffuse_color", index=-1, frame=bpy.context.scene.frame_current, group="")

			except:
				print("fail"+str(x)+"")
		if objt[x][0]=="ml":
			number_5=len(objt[x])-5
			number_6=number_5/3
			print(objt)
			pits=[""]*int(number_6)
			print(number_6)
			for k in range(len(pits)):
				pits[k]=[float(objt[x][4+3*k]),float(objt[x][5+3*k]),float(objt[x][6+3*k])]
			print(pits)
			makerode(pits,"the",float(objt[x][2]),float(objt[x][3]))
			

def arrowaddsub(location,arrow_f):
	arw=get(location,arrow_f)
	for x in range(len(arw)):
		if check(str(arw[x][0]))==1 and check(str(arw[x][1]))==1:
			name=str(arw[x][0])+"->"+str(arw[x][1])
			if check(name)==0:
				make(name,"ves.stl",a)
				#this give the material
				bpy.context.scene.objects.active = bpy.data.objects[name]
				activeObject = bpy.context.active_object
				mat = bpy.data.materials.new(name=name)
				activeObject.data.materials.append(mat)
				bpy.context.object.active_material.name = name
				bpy.context.object.active_material.name = name
			dimx=bpy.data.objects[name].dimensions[1]
			dimy=bpy.data.objects[name].dimensions[2]
			bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_VisualScaling')
			vecs(name,getloc(str(arw[x][0])),getloc(str(arw[x][1])))
			select(str(name))
			bpy.data.objects[name].dimensions[1] = dimx
			bpy.data.objects[name].dimensions[2] = dimy
			bpy.ops.object.select_all(action='DESELECT')
			bpy.ops.anim.keyframe_insert_menu(type='Rotation')
			bpy.ops.anim.keyframe_insert_menu(type='Location')
			bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_VisualScaling')

pits=[""]*3
pits[0]=[0,0,0]
pits[1]=[2,3,4]
pits[2]=[4,3,4]
#makerode(pits,"the",1,4)
tro(LOC,"All")
fram1=0
for x in range(75):
	pass
	#bpy.context.scene.frame_set(fram1+x*2)
	#arrowaddsub(LOC,"ves.stl")



