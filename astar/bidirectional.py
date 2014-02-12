# test cases source -- http://www.d.umn.edu/~jrichar4/8puz.html

import random
import copy
import sys
node_mapF = {}
node_mapB = {}
stepsF = 0
stepsB = 0
pathLength =0

hflag = 0

start_state = [[8,3,5],[4,1,6],[2,7,0]]
# start_state = [[1,3,4],[8,6,2],[7,0,5]]
# start_state = [[2,8,1],[0,4,3],[7,6,5]]
# start_state = [[2,8,1],[4,6,3],[0,7,5]]
# start_state = [[5,6,7],[4,0,8],[3,2,1]] # -- worst input

# start_state = [[2,0,3],[1,8,4],[7,6,5]]
final_state = [[1,2,3],[8,0,4],[7,6,5]]

# start_state = [[2,1,4],[7,8,3],[5,6,0]]
# final_state = [[1,7,4],[0,3,6],[2,5,8]]

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

class Node:
	def __init__(self,config):
		self.visited = False
		self.parent = None
		self.g = 0
		self.config = config
		self.h = 0
		global hflag 
		if(hflag):
			self.h = self.h_manhattan()
		else:
			self.h = self.h_plain()

	def h_plain(self):
		x = copy.deepcopy(final_state)
		count = 0
		for i in range(3):
			for j in range(3):
				if (self.config[i][j]!=x[i][j]):
					count += 1 
		return count

	def h_manhattan(self):
		count= 0;
		for i in range(3):
			for j in range(3):
				ele = self.config[i][j]
				if(ele!=0):
					pos = index_2d(final_state,ele);
					count+= abs(i-pos[0]) + abs(j-pos[1])
		return count

	def f(self):
		return self.h + self.g

	def print_node(self):
		for i in range(3):
			print self.config[i]
		print('--------------------')

def getChildren(node,temp):
	config = node.config
	posx = -1
	posy = -1
	for i in range(3):
		flag = False
		for j in range(3):
			if (config[i][j]==0):
				posx, posy = i, j
				flag = True
				break
		if (flag):
			break
	children = []
	if (posx <= 1):
		x = copy.deepcopy(config)
		x[posx][posy], x[posx+1][posy] = x[posx+1][posy], x[posx][posy]
		children += [x] 
	if (posx >= 1):
		x = copy.deepcopy(config)
		x[posx][posy], x[posx-1][posy] = x[posx-1][posy], x[posx][posy]
		children += [x]
	if (posy <= 1):
		x = copy.deepcopy(config)
		x[posx][posy], x[posx][posy+1] = x[posx][posy+1], x[posx][posy]
		children += [x] 
	if (posy >= 1):
		x = copy.deepcopy(config)
		x[posx][posy], x[posx][posy-1] = x[posx][posy-1], x[posx][posy]
		children += [x]
	if(temp=='b'):
		for c in children:
			if (not str(c) in node_mapB.keys()):
				node_mapB[str(c)] = Node(c)
	elif(temp=='f'):
		for c in children:
			if(not str(c) in node_mapF.keys()):
				node_mapF[str(c)] = Node(c)
	else:
		print (temp)
		print("some serious trouble")
	return children

def astar(S,F):
	node_mapF[str(S.config)] = S
	node_mapF[str(F.config)] = F

	node_mapB[str(S.config)] = S
	node_mapB[str(F.config)] = F

	OLF = [S]
	CLF = []
	OLB = [F]
	CLB = []

	while (True):
		if (len(OLF)==0 or len(OLB)==0):
			print("Search failed!")
			exit(0)

		min_node = OLF[0]
		for node in OLF:
			if (node.f() < min_node.f()):
				min_node = node
		if (min_node.config==F.config):
			p = min_node
			while (p != None):
				p.print_node()
				p = p.parent
			return

		for ele in CLB:
			if ele.config==min_node.config:
				print("path found")
				path=[]
				p = min_node
				global pathLength
				while (p != None):
					path.append(p);
					pathLength+=1
					p = p.parent
				path.reverse()
				for p in path:
					p.print_node()
				p = ele.parent
				while (p != None):
					pathLength+=1
					p.print_node()
					p = p.parent
				return 

		global stepsF
		stepsF += 1
		if(stepsF%100==0):
			print(stepsF)

		min_node.visited = True
		neighbors = getChildren(min_node,'f')
		for y in neighbors:
			x = node_mapF[str(y)]
			if (not x.visited):
				x.parent = min_node
				x.g = 1 + min_node.g # cost of each edge is 1
				OLF += [x]
			else:
				w = 1 + min_node.g
				if (w <= x.g):
					x.parent = min_node
					x.g = w
					# update children of x
					queue = [x]
					while (len(queue)!=0):
						first_node = queue[0] # 
						children = getChildren(first_node,'f')
						for c in children:
							child = node_mapF[str(c)]
							if (child.parent==first_node):
								child.g = 1 + first_node.g
								queue += [child]
						queue.remove(first_node)
				else:
					pass
		OLF.remove(min_node)
		CLF += [min_node]

		# ############################
		min_node = OLB[0]
		for node in OLB:
			if (node.f() < min_node.f()):
				min_node = node
		if (min_node.config==S.config):
			p = min_node
			while (p != None):
				p.print_node()
				p = p.parent
			return

		for ele in CLF:
			if ele.config==min_node.config:
				print("path found")
				path=[]
				p = ele
				global pathLength
				while (p != None):
					pathLength+=1
					path.append(p);
					p = p.parent
				path.reverse()
				for p in path:
					p.print_node()
				p = min_node.parent
				while (p != None):
					pathLength+=1
					p.print_node()
					p = p.parent
				return 

		global stepsB
		stepsB += 1
		min_node.visited = True
		neighbors = getChildren(min_node,'b')
		for y in neighbors:
			x = node_mapB[str(y)]
			if (not x.visited):
				x.parent = min_node
				x.g = 1 + min_node.g # cost of each edge is 1
				OLB += [x]
			else:
				w = 1 + min_node.g
				if (w <= x.g):
					x.parent = min_node
					x.g = w
					# update children of x
					queue = [x]
					while (len(queue)!=0):
						first_node = queue[0] # 
						children = getChildren(first_node,'b')
						for c in children:
							child = node_mapB[str(c)]
							if (child.parent==first_node):
								child.g = 1 + first_node.g
								queue += [child]
						queue.remove(first_node)
				else:
					pass
		OLB.remove(min_node)
		CLB += [min_node]

def main():
	global hflag 
	hflag = int(sys.argv[1])
	start = Node(start_state)
	final = Node(final_state)
	print ("\nSTART")
	start.print_node()
	print ("FINAL")
	final.print_node()
	print ("PATH")
	astar(start,final)
	print("Number of steps : " + str(max(stepsF,stepsB)))
	print("pathLength : "+str(pathLength))
main()