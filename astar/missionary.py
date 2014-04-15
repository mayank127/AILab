# test cases source -- http://www.d.umn.edu/~jrichar4/8puz.html
import random
import copy
import sys
node_list = {}
node_map = {}
steps = 0
hflag=0


n_missionary=3
n_cannibal=3
n=3
start_state = [n_missionary,n_cannibal,0] # <M,C,P> (0:left and 1:right)
final_state = [0,0,1]

def invert(n):
	if (n==0):
		return 1
	else:
		return 0

class Node:

	def __init__(self,config):
		self.visited = False
		self.parent = None
		self.g = 0
		self.config = config
		if(hflag==1):
			self.h = self.h_minSteps()
		elif(hflag==2):
			self.h = self.h_npersonLeft()
		else:
			self.h = self.cal_h()

	def cal_h(self):
		return 0

	def f(self):
		return self.h + self.g

	def h_npersonLeft(self):
		return (self.config[0]+self.config[1])*1000

	def h_minSteps(self):
		return (self.config[0]+self.config[1])/2


	def print_node(self):
		print(self.config)
		print('--------------------')

def isValid(x):
	return (x[0]>=0 and x[1]>=0 and (x[0]-x[1]>=0 or x[0]==0) and ((n-x[0])-(n-x[1])>=0 or (n-x[0]==0)))


def getChildren(node):
	config = copy.deepcopy(node.config)
	children = []
	left = [config[0],config[1]]
	right = [n-config[0],n-config[1]]
	boat = config[2]
	if(boat):
		missionary = right[0]
		cannibal = right[1]
	else:
		missionary = left[0]
		cannibal = left[1]

	x = [missionary-2,cannibal,invert(boat)]
	if (isValid(x)):
		if(boat):
			new_left = [n-x[0],n-x[1],invert(boat)]
			children += [new_left]
		else:
			children += [x]

	x = [missionary-1,cannibal,invert(boat)]
	if (isValid(x)):
		if(boat):
			new_left = [n-x[0],n-x[1],invert(boat)]
			children += [new_left]
		else:
			children += [x]

	x = [missionary,cannibal-2,invert(boat)]
	if (isValid(x)):
		if(boat):
			new_left = [n-x[0],n-x[1],invert(boat)]
			children += [new_left]
		else:
			children += [x]

	x = [missionary,cannibal-1,invert(boat)]
	if (isValid(x)):
		if(boat):
			new_left = [n-x[0],n-x[1],invert(boat)]
			children += [new_left]
		else:
			children += [x]

	x = [missionary-1,cannibal-1,invert(boat)]
	if (isValid(x)):
		if(boat):
			new_left = [n-x[0],n-x[1],invert(boat)]
			children += [new_left]
		else:
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
			pathLength=0
			while (p != None):
				p.print_node()
				p = p.parent
				pathLength+=1
			print("Path length = "+str(pathLength))
			return
		global steps
		steps += 1
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
				if (w <= x.g):
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
	hflag = int(sys.argv[1])
	start = Node(start_state)
	final = Node(final_state)
	print ("\nSTART")
	start.print_node()
	print ("FINAL")
	final.print_node()
	print ("PATH")
	astar(start,final)
	print("Number of steps : " + str(steps))
main()