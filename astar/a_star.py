import networkx as nx
import random

G = nx.Graph()
node_list = {}

def h(node):
	return 0

class Node:
	def __init__(self,id):
		self.id = id
		self.visited = False
		self.parent = None
		self.g = 0
		self.h = h(self)
	def f(self):
		return self.h + self.g

def astar(T,S,F):
	OL = [S]
	CL = []
	while (True):
		z=[x.id for x in OL]
		print(z)
		if (len(OL)==0):
			print("Search failed!")
			exit(0)
		min_node = OL[0]
		for node in OL:
			if (node.f() < min_node.f()):
				min_node = node
		if (min_node==F):
			path = []
			p = min_node
			while (p != None):
				path += [p.id]
				p = p.parent
			print(path)
			return
		min_node.visited = True
		neighbors = G.neighbors(min_node)
		for x in neighbors:
			if (not x.visited):
				x.parent = min_node
				x.g = G[min_node][x]["weight"] + min_node.g
				OL += [x]
			else:
				w = G[min_node][x]["weight"] + min_node.g
				if (w <= x.g):
					x.parent = min_node
					x.g = w
					# update children of x
					queue = [x]
					while (len(queue)!=0):
						first_node = queue[0] # 
						children = G.neighbors(first_node)
						for child in children:
							if (child.parent==first_node):
								child.g = G[first_node][child]["weight"] + first_node.g
								queue += [child]
						queue.remove(first_node)
				else:
					pass
		OL.remove(min_node)
		CL += [min_node]

def main():
	# n = int(input('Enter number of nodes : '))
	n = 6
	for i in range(n):
		node = Node(i)
		G.add_node(node)
		node_list[i] = node
	G.add_edge(node_list[0],node_list[1],weight=1)
	G.add_edge(node_list[1],node_list[2],weight=1)
	G.add_edge(node_list[1],node_list[3],weight=2)
	G.add_edge(node_list[3],node_list[4],weight=1)
	G.add_edge(node_list[4],node_list[5],weight=1)
	G.add_edge(node_list[2],node_list[5],weight=1)
	astar(G,node_list[0],node_list[5])

main()
