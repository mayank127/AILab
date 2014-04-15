# test cases source -- http://www.d.umn.edu/~jrichar4/8puz.html

import random
import copy
import sys
node_list = {}
node_map = {}
steps = 0
pathLength = 0

hflag = 0

# s1=[[8,3,5],[4,1,6],[2,7,0]]
# s2=[[3,1,4],[6,2,8],[0,5,7]]
# s3=[[2,8,1],[4,6,3],[0,7,5]]
# s4=[[1,2,3],[6,5,4],[0,7,8]]
# s5=[[1,3,2],[4,0,8],[7,6,5]]
# s6=[[5,6,7],[4,0,8],[3,2,1]] # -- worst input
# final_state = [[1,2,3],[8,0,4],[7,6,5]]

# start_state = [[2,1,3],[4,5,6],[7,0,8]]
# start_state = [[8,3,5],[4,1,6],[2,7,0]]
# start_state = [[1,3,4],[8,6,2],[7,0,5]] # 9
# start_state = [[2,8,1],[0,4,3],[7,6,5]] # -- non-optimal start state 1
# start_state = [[2,8,1],[4,6,3],[0,7,5]]
# start_state = [[5,6,7],[4,0,8],[3,2,1]] # -- worst input
start_state = [[1,3,6],[4,0,2],[7,5,8]]
final_state = [[1,2,3],[4,5,6],[7,8,0]]

# start_state = [[2,1,4],[7,8,3],[5,6,0]]
# final_state = [[1,7,4],[0,3,6],[2,5,8]] # 10
# start_state = [[2,0,3],[1,8,4],[7,6,5]]
# final_state = [[1,2,3],[8,0,4],[7,6,5]] # -- non-optimal final state 1

# start_state = [[0,1,2],[3,4,5],[6,7,8]]
# final_state = [[4,1,2],[0,6,3],[7,5,8]]

startList=[start_state]

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
		if(hflag==1):
			self.h = self.h_manhattan()
		elif(hflag==2):
			self.h = self.inversionPairs()/2
		elif(hflag==3):
			self.h = 0; #Trivial
		elif(hflag==4):
			self.h = self.h_manhattan_new()
		elif(hflag==5):
			self.h = self.h_plain_new()
		else:
			self.h = self.h_plain() #displaced tiles

	def h_plain(self):
		x = copy.deepcopy(final_state)
		count = 0
		for i in range(3):
			for j in range(3):
				if (self.config[i][j]!=x[i][j] and self.config[i][j]!=0):
					count += 1
		return count

	def h_plain_new(self):
		x = copy.deepcopy(start_state)
		count = 0
		for i in range(3):
			for j in range(3):
				if (self.config[i][j]!=x[i][j] and self.config[i][j]!=0):
					count += 1
		return count*10 +20

	def h_manhattan(self):
		count= 0
		for i in range(3):
			for j in range(3):
				ele = self.config[i][j]
				if(ele!=0):
					pos = index_2d(final_state,ele);
					count+= abs(i-pos[0]) + abs(j-pos[1])
		return count

	def h_manhattan_new(self):
		count= 0
		for i in range(3):
			for j in range(3):
				ele = self.config[i][j]
				if(ele!=0):
					pos = index_2d(start_state,ele);
					count+= abs(i-pos[0]) + abs(j-pos[1])
		return count*10 + 10

	def f(self):
		return self.h + self.g


	def inversionPairs(self):
		arr=[]
		for row in self.config:
			for ele in row:
				if(ele!=0):
					arr.append(ele)
		nInversions=0;
		for i in range(len(arr)):
			for j in range(i+1, len(arr)):
				if(arr[i]>arr[j]):
					nInversions+=1
		arr=[]
		for row in final_state:
			for ele in row:
				if(ele!=0):
					arr.append(ele)
		for i in range(len(arr)):
			for j in range(i+1, len(arr)):
				if(arr[i]>arr[j]):
					nInversions-=1
		return abs(nInversions)

	def print_node(self):
		for i in range(3):
			print self.config[i]
		print('--------------------')

def getChildren(node):
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
	for c in children:
		if (not str(c) in node_map.keys()):
			node_map[str(c)] = Node(c)
	return children



def astar(S,F):
	node_map[str(S.config)] = S
	node_map[str(F.config)] = F

	OL = [S]
	CL = []
	while (True):
		if (len(OL)==0):
			print("Search failed!")
			exit(0)
		min_node = OL[0]
		for node in OL:
			if (node.f() < min_node.f()):
				min_node = node
		if (min_node.config==F.config):
			p = min_node
			while (p != None):
				global pathLength
				pathLength+=1
				# p.print_node()
				p = p.parent
			return
		global steps
		steps += 1
		if(steps%100==0):
			print(steps)
		min_node.visited = True
		neighbors = getChildren(min_node)
		for y in neighbors:
			x = node_map[str(y)]
			if (not x.visited):
				if not x in OL:
					x.parent = min_node
					x.g = 1 + min_node.g # cost of each edge is 1
					OL += [x]
				else:
					w = 1 + min_node.g
					if (w < x.g):
						x.parent = min_node
						x.g = 1 + min_node.g
			else:
				w = 1 + min_node.g
				if (w < x.g):
					print "parent pointer redirection ", str(x.config), " old g = ", x.g, " new g = ", w
					x.parent = min_node
					x.g = w
					# update children of x
					queue = [x]
					while (len(queue)!=0):
						first_node = queue[0] # 
						children = getChildren(first_node)
						for c in children:
							child = node_map[str(c)]
							if (child.parent==first_node):
								child.g = 1 + first_node.g
								queue += [child]
						queue.remove(first_node)
				else:
					pass
		OL.remove(min_node)
		CL += [min_node]

def main():
	global hflag
	for snode in startList:
		hflag = int(sys.argv[1])
		start = Node(snode)
		final = Node(final_state)
		# print ("\nSTART")
		# start.print_node()
		# print ("FINAL")
		# final.print_node()
		# print ("PATH")

		#Non Reachability Test
		# print start.inversionPairs()-final.inversionPairs()
		if(start.inversionPairs()%2!=0):
			print("Puzzle cannot be solved")
			exit(0)

		astar(start,final)
		print("Number of steps : " + str(steps))
		print("pathLength : "+str(pathLength))
main()