# Input will be a formula as a string

import sys

formula_list = []

class formula:
	def __init__(self, id, left=None, right=None):
		self.id = id
		self.left = left
		self.right = right
		if(id == "" and left != None):
			self.id = '(' + left.id + ' -> ' + right.id + ')'
		elif(id == ""):
			print ("Should not have reached here. ID and left, right can not be null together.")
			exit(0)

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
	def get_symbols(self):
		if (self.is_atomic() and self.id!='F'):
			l = [self.id]
			return l
		else:
			l = []
			if (self.left != None):
				l += self.left.get_symbols()
			if (self.right != None):
				l += self.right.get_symbols()
			l = list(set(l))
			return l
	def assign_values(self):
		self.print_id()
		l = self.get_symbols()
		assignments = {}
		for element in l:
			val = raw_input('Give assignment for ' + element + ' : ')
			assignments[element] = val
		s = '('
		for ch in self.id:
			if ch in l:
				s += assignments[ch]
			else:
				s += ch
		s += ')'
		return parse(s)

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
					return formula('(' + s + ')', left, right)

def gen_hypo(s):
	global formula_list
	wff = parse(s)
	print 'Symbols are : '
	print wff.get_symbols()
	w = wff
	while w.left != None:
		formula_list += [w.left]
		w = w.right
	if (w.id!='F'):
		final = formula("", w, false)
		formula_list += [final]

axiom_set = [parse('(A -> (B -> A))'), parse('((A -> (B -> C)) -> ((A -> B) -> (A -> C)))'), parse('(((A -> F) -> F) -> A)')]

f = open(sys.argv[1])
lines = f.readlines()

def search_formula_list(w):
	global formula_list
	for wf in formula_list:
		if (w.id == wf.id):
			return True
	return False



def heuristic_3(wff):
	if(wff.left != None and wff.right.id == false.id):
		if(wff.left.left != None and wff.left.right.id == false.id):
			ax_f = formula("", wff, wff.left.left)
			if search_formula_list(ax_f):
				return []
			else:
				print "Axiom 3:",
				ax_f.print_id()
				return [ax_f]
	return []

def heuristic_2(wff):
	if(wff.left != None and wff.right.left != None):
		A = wff.left
		B = wff.right.left
		C = wff.right.right
		ax_f = formula("", wff, formula("", formula("", A, B), formula("", A, C)))
		if search_formula_list(ax_f):
			return []
		else:
			print "Axiom 2:",
			ax_f.print_id()
			return [ax_f]
	return []

def heuristic_1(wff):
	global formula_list
	for f in formula_list:
		if(f.left != None and f.left.left != None and f.left.right.id == wff.id):
			ax_f = formula("", wff, f.left)
			if search_formula_list(ax_f):
				return []
			else:
				print "Axiom 1:",
				ax_f.print_id()
				return [ax_f]
	return []

for line in lines:
	formula_list = []
	gen_hypo(line)

	for w in formula_list:
		w.print_id()


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
			temp_list = []
			for f in formula_list:
				temp_list += heuristic_3(f)
				temp_list += heuristic_2(f)
				temp_list += heuristic_1(f)
			mp_count += len(temp_list)
			formula_list += temp_list

		if mp_count == 0:
			print "Can't proceed (Need Help)"
			n = int(raw_input('Enter axiom number to use : [1 to 3]'))
			formula_list += [axiom_set[n - 1].assign_values()]

	if mp_count != 0:
		print("HENCE PROVED")
