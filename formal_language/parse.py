# Input will be a formula as a string

formula_list = []

class formula:
	def __init__(self, id):
		self.id = id
	def is_atomic(self):
		if (len(self.id) == 1):
			return True
		else:
			return False
	def print_formula(self):
		print self.id

def parse(wff):
	global formula_list
	if (wff.is_atomic()):
		s = '(' + wff.id + ' -> F)'
		new = formula(s)
		formula_list += [new]
	else:
		open_count = 0
		close_count = 0
		exp = wff.id[1:-1]
		
		
		for i in range(1,len(wff.id)):
			if (exp[i] == '('):
				open_count += 1
			if (exp[i] == ')'):
				close_count += 1
			if (open_count == close_count):
				s = exp[1:i+1]
				# print s
				new1 = formula(s)
				formula_list += [new1]
				s = exp[i+5:-1]
				if (len(s)==1):
					new = formula("(" + s + " -> " + "F)")
					return
				else:
					new2 = formula(s)
					formula_list += [new2]
					parse(new2)
					return

s = raw_input('')
new = formula(s)
parse(new)
for f in formula_list:
	f.print_formula()