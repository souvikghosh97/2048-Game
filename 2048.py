


##############################################

##ACADEMY OF TECHNOLOGY
##COPY RIGHT:-ACADEMY OF TECHNOLOGY
##PROGRAM DEVELOPED BY SOUVIK GHOSH

##############################################




import time,os,sys,random
def First(l):
	i1=random.choice([0,1,2,3])
	i2=random.choice([0,1,2,3])
	j1=random.choice([0,1,2,3])
	j2=random.choice([0,1,2,3])
	if i1==i2 and j1==j2:
		while j1==j2:
			j2=random.choice([0,1,2,3])
	l[i1][j1],l[i2][j2]=2,2
	
	return l

def rotate(lt):
	l0,l1,l2,l3=[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
	l=[l0,l1,l2,l3]
	c=3
	for i in range(0,4):
		r=0
		for j in range(0,4):
			l[r][c]=lt[i][j]
			r+=1
		c-=1
	return l

def rotateBack(lt):
	l0,l1,l2,l3=[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
	l=[l0,l1,l2,l3]
	c=0
	for i in range(0,4):
		r=3
		for j in range(0,4):
			l[r][c]=lt[i][j]
			r-=1
		c+=1





	return l

def isWin(l):
	for i in range(0,4):
		for j in range(0,4):
			if l[i][j]==2048:
				return 1
	return 0
def unhide(l):
	i,j=random.choice([0,1,2,3]),random.choice([0,1,2,3])
	while l[i][j]!=0:
		i,j=random.choice([0,1,2,3]),random.choice([0,1,2,3])

	l[i][j]=random.choice([2,4,2,8,2,4,2,2,2,2,2,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,2,2,2,2,2,2,2,2,2,2,2,4,2,8])


	return l
def shift(l):
	
	for i in range(3,0,-1):
		if l[i]==0:
			j=i-1
			while j>=0 and l[j]==0:
				j-=1
			if j>=0 and l[j]!=0:
				l[i]=l[j]
				l[j]=0
		
	return l



	


def shiftR(l):
	for k in range(0,4):
		l[k]=shift(l[k])
		for i in range(3,0,-1):
			if l[k][i]!=0:
				j=i-1
				while j>=0 and l[k][j]==0:
					j-=1
				if j>=0 and l[k][i]==l[k][j]:
					l[k][i]=l[k][i]*2
					l[k][j]=0
			l[k]=shift(l[k])
	return l


def shiftL(l):
	l=rotate(l)
	l=rotate(l)
	shiftR(l)
	l=rotateBack(l)
	l=rotateBack(l)
	
	return l
def shiftU(l):
	l=rotate(l)
	shiftR(l)
	l=rotateBack(l)
	return l

def shiftD(l):
	l=rotate(l)
	l=rotate(l)
	l=rotate(l)
	shiftR(l)
	l=rotateBack(l)
	l=rotateBack(l)
	l=rotateBack(l)
	return l

def printList(l):
	for i in range(0,4):
		print "| ",
		for j in range(0,4):
			if l[i][j]!=0:
				print " ",l[i][j]," ","|",
			else:
				print " "," "," ","|",
		print "\n"
	print "\n\n" 

def isGameOver(l):
	fl,c=1,0
	for i in range(0,3):
		for j in range(0,3):
			if l[i][j]!=0:
				c+=1
	if c<16:
		return 0
		
			
	for i in range(0,3):
		for j in range(0,3):
			if l[i][j]==l[i][j+1] or l[i][j]==l[i+1][j]:
				fl=0
				break

	
	return fl


l0,l1,l2,l3=[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]
l=[l0,l1,l2,l3]
l=First(l)
printList(l)
while True:
	try:
		print "\n\n6.Right, 4.Left, 8.Up, 2.Down, 5.Exit",
		ch=eval(raw_input(":  "))
		if ch==6:
			l=shiftR(l)
		elif ch==4:
			l=shiftL(l)
		elif ch==8:
			l=shiftU(l)
		elif ch==2:
			l=shiftD(l)
		elif ch==5:
			sys.exit()
		else:
			print "\n\n\tInvalid Choice...\n\n"
			continue
		if isWin(l)==1:
			print "You Win "
			break
	

		if isGameOver(l)==1:
			print "Game Over"
			break
		else:
			l=unhide(l)
		printList(l)
	except SyntaxError:
		pass
