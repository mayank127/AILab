# Input will be a formula as a string

import sys

formula_list = []

class formula:
	def __init__(self, id, left=None, right=None):
		self.id = id
		self.left = left
		self.right = right
	def is_atomic(self):
		if (len(self.id) == 1):
			return True
		else:
			return False
	def print_formula(self):
		if(self.left != None):
			print("("),
			self.left.print_formula()
			print("->"),
			self.right.print_formula()
			print(")"),
		else:
			print (self.id),
	def print_id(self):
		print (self.id)

false = formula("F")

def parse(s):
	s = s.strip()
	if(len(s)==1):
		return formula(s)
	else:
		if(s[0] == '(' and s[-1] == ')'):
			s = s[1:-1]
			count = 0
			for i in range(len(s)):
				c = s[i]
				if c == '(':
					count += 1
				elif c== ')':
					count -= 1
				elif count == 0 and c == '-':
					left = parse(s[:i-1])
					right = parse(s[i+2:])
					return formula(s, left, right)

def gen_hypo(s):
	global formula_list
	wff = parse(s)
	w = wff
	while w.left != None:
		formula_list += [w.left]
		w = w.right
	final = formula(w.id + " -> F", w, false)
	formula_list += [final]

f = open(sys.argv[1])
lines = f.readlines()
for line in lines:
	formula_list = []
	# print line
	gen_hypo(line)

	for w in formula_list:
		w.print_id()

	def search_formula_list(w):
		for wf in formula_list:
			if (w.id == wf.id):
				return True
		return False

	while not search_formula_list(false):
		mp_count = 0
		for w in formula_list:
			if (w.left != None):
				if search_formula_list(w.left):
					if not search_formula_list(w.right):
						formula_list += [w.right]
						w.right.print_id()
						mp_count += 1
		if mp_count == 0:
			print ("Can not Prove")
			break

	print("HENCE PROVED")