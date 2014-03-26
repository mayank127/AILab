# Input will be a formula as a string

import sys

formula_list = []
proof_list = []

HYPO = 0
AXIOM = 1
MODPON = 2
USER = 3
NOTYPE = -1


class formula:
	def __init__(self, id, left=None, right=None):
		self.id = id
		self.left = left
		self.right = right
		self.number = 0
		
		self.type = NOTYPE
		self.parent1 = None
		self.parent2 = None

		if(id == "" and left != None):
			self.id = '(' + left.id + ' -> ' + right.id + ')'
		elif(id == ""):
			print ("Should not have reached here. ID and left, right can not be null together.")
			exit(0)

	def get(self):
		return formula(self.id, self.left, self.right)

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
		ax = parse(s)
		ax.set_axiom(self.axiom)
		return ax

	def get_num(self):
		return self.number

	def set_type(self, num, type=NOTYPE, parent1=None, parent2=None):
		self.number = num
		self.type = type
		self.parent1 = parent1
		self.parent2 = parent2

	def get_type(self):
		return self.type

	def get_parents(self):
		return [self.parent1, self.parent2]

	def set_axiom(self, ax):
		self.axiom = ax

	def print_proof(self, l):
		print "L%d:" %(l - self.pnum),

		if(self.type == HYPO):
			print("HYPOTHESIS:\t\t\t"),
		elif(self.type == MODPON):
			print ("MODUS PONENS (L%d, L%d):\t" %(l - self.pparent1, l - self.pparent2)),
		elif(self.type == AXIOM):
			print("FROM AXIOM-" + str(self.axiom) +":\t\t"),
		elif(self.type == USER):
			print ("USER AXIOM-" + str(self.axiom) + ":\t\t"),
		self.print_id()

	def set_proof_number(self, num, p1=None, p2=None):
		self.pnum = num
		self.pparent1 = p1
		self.pparent2 = p2
	def get_proof_number(self):
		return self.pnum

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
	# print 'Symbols are : '
	# print wff.get_symbols()
	w = wff
	while w.left != None:
		formula_list += [w.left]
		l = len(formula_list)
		formula_list[-1].set_type(l-1, HYPO)
		w = w.right
	if (w.id!='F'):
		final = formula("", w, false)
		formula_list += [final]
		l = len(formula_list)
		formula_list[-1].set_type(l-1, HYPO)

axiom_set = [parse('(A -> (B -> A))'), parse('((A -> (B -> C)) -> ((A -> B) -> (A -> C)))'), parse('(((A -> F) -> F) -> A)')]
axiom_set[0].set_axiom(0)
axiom_set[1].set_axiom(1)
axiom_set[2].set_axiom(2)

if(len(sys.argv) != 2):
	print "wrong use: " + sys.argv[0] + " filename"
	exit(0)

f = open(sys.argv[1])
lines = f.readlines()

def search_formula_list(w):
	global formula_list
	for wf in formula_list:
		if (w.id == wf.id):
			return True
	return False

def find_in_formula_list(w):
	global formula_list
	for wf in formula_list:
		if (w.id == wf.id):
			return wf.get_num()
	return -1

def heuristic_3(wff):
	if(wff.left != None and wff.right.id == false.id):
		if(wff.left.left != None and wff.left.right.id == false.id):
			ax_f = formula("", wff.get(), wff.left.left.get())
			ax_f.set_axiom(3)
			if search_formula_list(ax_f):
				return []
			else:
				print "Axiom 3:",
				ax_f.print_id()
				return [ax_f]
	return []

def heuristic_2(wff):
	if(wff.left != None and wff.right.left != None):
		A = wff.left.get()
		B = wff.right.left.get()
		C = wff.right.right.get()
		ax_f = formula("", wff.get(), formula("", formula("", A, B), formula("", A, C)))
		ax_f.set_axiom(2)
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
			ax_f = formula("", wff.get(), f.left.get())
			ax_f.set_axiom(1)
			if search_formula_list(ax_f):
				return []
			else:
				print "Axiom 1:",
				ax_f.print_id()
				return [ax_f]
	return []

def modus_ponens():
	global formula_list
	mp_count = 0
	for w in formula_list:
		if (w.left != None):
			if search_formula_list(w.left):
				if not search_formula_list(w.right):
					formula_list += [w.right.get()]
					l = len(formula_list)
					formula_list[-1].set_type(l-1, MODPON, find_in_formula_list(w.left), w.get_num())
					mp_count += 1
	return mp_count

def search_proof_list(w):
	global proof_list
	for wf in proof_list:
		if (w.id == wf.id):
			return True
	return False

def find_proof_number(w):
	global proof_list
	for wf in proof_list:
		if (w.id == wf.id):
			return wf.get_proof_number()
	return -1


def print_proof(i):
	global formula_list
	global proof_list

	if(not search_proof_list(formula_list[i])):
		proof_list += [formula_list[i]]
		l = len(proof_list)
		proof_list[-1].set_proof_number(l-1)

	if(formula_list[i].get_type() == MODPON):
		p = formula_list[i].get_parents()
		if(not search_proof_list(formula_list[p[1]])):
			proof_list += [formula_list[p[1]]]
			l = len(proof_list)
			proof_list[-1].set_proof_number(l-1)
		if(not search_proof_list(formula_list[p[0]])):
			proof_list += [formula_list[p[0]]]
			l = len(proof_list)
			proof_list[-1].set_proof_number(l-1)
		print_proof(p[1])
		print_proof(p[0])

		l = find_proof_number(formula_list[i])
		proof_list[l].set_proof_number(l, find_proof_number(formula_list[p[0]]), find_proof_number(formula_list[p[1]]))
			



for line in lines:
	false = formula("F")
	formula_list = []
	gen_hypo(line)
	proof_list = []
	for w in formula_list:
		w.print_id()


	while not search_formula_list(false):
		mp_count = modus_ponens()
		
		if mp_count == 0:
			temp_list = []
			for f in formula_list:
				temp_list += heuristic_3(f)
				temp_list += heuristic_2(f)
				temp_list += heuristic_1(f)
			mp_count += len(temp_list)
			for w in temp_list:
				formula_list += [w]
				l = len(formula_list)
				formula_list[-1].set_type(l-1, AXIOM)

		if mp_count == 0:
			print "Can't proceed (Need Help)"
			n = int(raw_input('Enter axiom number to use : [1 to 3]'))
			formula_list += [axiom_set[n - 1].assign_values()]
			l = len(formula_list)
			formula_list[-1].set_type(l-1, USER)

	if mp_count != 0:
		print("HENCE PROVED")

	if(search_formula_list(false)):
		i = find_in_formula_list(false)
		print_proof(i)
		print ("\n\nPROOF HERE -------------------------------------------------------------")
		for w in reversed(proof_list):
			w.print_proof(len(proof_list))
		print("------------------------------------------------------------------------\n\n")