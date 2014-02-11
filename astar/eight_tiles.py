# test cases source -- http://www.d.umn.edu/~jrichar4/8puz.html

import networkx as nx
import random
import copy
import sys
G = nx.Graph()
node_list = {}
node_map = {}
steps = 0

hflag = -1

# start_state = [[8,3,5],[4,1,6],[2,7,0]]
# start_state = [[1,3,4],[8,6,2],[7,0,5]]
# start_state = [[2,8,1],[0,4,3],[7,6,5]]
# start_state = [[2,8,1],[4,6,3],[0,7,5]]
start_state = [[5,6,7],[4,0,8],[3,2,1]] # -- worst input
final_state = [[1,2,3],[8,0,4],[7,6,5]]

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
				p.print_node()
				p = p.parent
			return
		global steps
		steps += 1
		min_node.visited = True
		neighbors = getChildren(min_node)
		for y in neighbors:
			x = node_map[str(y)]
			if (not x.visited):
				x.parent = min_node
				x.g = 1 + min_node.g # cost of each edge is 1
				OL += [x]
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
	hflag = sys.argv[1]
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