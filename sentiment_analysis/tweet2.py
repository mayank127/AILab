filenames = ['negative_sentiments', 'positive_sentiments', 'neutral_sentiments']
outputs = [[1,0,0],[0,0,1],[0,1,0]]
faltu_words = ["i", "a", "able", "about", "above", "abroad", "according", "accordingly", "across", "actually", "adj", "after", "afterwards", "again", "against", "ago", "ahead", "ain't", "all", "allow", "allows", "almost", "alone", "along", "alongside", "already", "also", "although", "always", "am", "amid", "amidst", "among", "amongst", "an", "and", "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere", "apart", "appear", "appreciate", "appropriate", "are", "aren't", "around", "as", "a's", "aside", "ask", "asking", "associated", "at", "available", "away", "awfully", "back", "backward", "backwards", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "both", "brief", "but", "by", "came", "can", "cannot", "cant", "can't", "caption", "cause", "causes", "certain", "certainly", "changes", "clearly", "c'mon", "co", "co.", "com", "come", "comes", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn't", "course", "c's", "currently", "dare", "daren't", "definitely", "described", "despite", "did", "didn't", "different", "directly", "do", "does", "doesn't", "doing", "done", "don't", "down", "downwards", "during", "each", "edu", "eg", "eight", "eighty", "either", "else", "elsewhere", "end", "ending", "enough", "entirely", "especially", "et", "etc", "even", "ever", "evermore", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "fairly", "far", "farther", "few", "fewer", "fifth", "first", "five", "followed", "following", "follows", "for", "forever", "former", "formerly", "forth", "forward", "found", "four", "from", "further", "furthermore", "get", "gets", "getting", "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "had", "hadn't", "half", "happens", "hardly", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "here's", "hereupon", "hers", "herself", "he's", "hi", "him", "himself", "his", "hither", "hopefully", "how", "howbeit", "however", "hundred", "i'd", "ie", "if", "ignored", "i'll", "i'm", "immediate", "in", "inasmuch", "inc", "inc.", "indeed", "indicate", "indicated", "indicates", "inner", "inside", "insofar", "instead", "into", "inward", "is", "isn't", "it", "it'd", "it'll", "its", "it's", "itself", "i've", "just", "k", "keep", "keeps", "kept", "know", "known", "knows", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "let's", "like", "liked", "likely", "likewise", "little", "look", "looking", "looks", "low", "lower", "ltd", "made", "mainly", "make", "makes", "many", "may", "maybe", "mayn't", "me", "mean", "meantime", "meanwhile", "merely", "might", "mightn't", "mine", "minus", "miss", "more", "moreover", "most", "mostly", "mr", "mrs", "much", "must", "mustn't", "my", "myself", "name", "namely", "nd", "near", "nearly", "necessary", "need", "needn't", "needs", "neither", "never", "neverf", "neverless", "nevertheless", "new", "next", "nine", "ninety", "no", "nobody", "non", "none", "nonetheless", "noone", "no-one", "nor", "normally", "not", "nothing", "notwithstanding", "novel", "now", "nowhere", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "one's", "only", "onto", "opposite", "or", "other", "others", "otherwise", "ought", "oughtn't", "our", "ours", "ourselves", "out", "outside", "over", "overall", "own", "particular", "particularly", "past", "per", "perhaps", "placed", "please", "plus", "possible", "presumably", "probably", "provided", "provides", "que", "quite", "qv", "rather", "rd", "re", "really", "reasonably", "recent", "recently", "regarding", "regardless", "regards", "relatively", "respectively", "right", "round", "said", "same", "saw", "say", "saying", "says", "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "since", "six", "so", "some", "somebody", "someday", "somehow", "someone", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify", "specifying", "still", "sub", "such", "sup", "sure", "take", "taken", "taking", "tell", "tends", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "there'd", "therefore", "therein", "there'll", "there're", "theres", "there's", "thereupon", "there've", "these", "they", "they'd", "they'll", "they're", "they've", "thing", "things", "think", "third", "thirty", "this", "thorough", "thoroughly", "those", "though", "three", "through", "throughout", "thru", "thus", "till", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "t's", "twice", "two", "un", "under", "underneath", "undoing", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "up", "upon", "upwards", "us", "use", "used", "useful", "uses", "using", "usually", "v", "value", "various", "versus", "very", "via", "viz", "vs", "want", "wants", "was", "wasn't", "way", "we", "we'd", "welcome", "well", "we'll", "went", "were", "we're", "weren't", "we've", "what", "whatever", "what'll", "what's", "what've", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "where's", "whereupon", "wherever", "whether", "which", "whichever", "while", "whilst", "whither", "who", "who'd", "whoever", "whole", "who'll", "whom", "whomever", "who's", "whose", "why", "will", "willing", "wish", "with", "within", "without", "wonder", "won't", "would", "wouldn't", "yes", "yet", "you", "you'd", "you'll", "your", "you're", "yours", "yourself", "yourselves", "you've", "zero", "link", "comment", "www"]

import re
from random import random, shuffle
from stemming.porter2 import stem
import numpy
from collections import Counter

brk = re.compile("(?:(?:[^a-zA-Z@]+')|(?:'[^a-zA-Z@]+))|(?:[^a-zA-Z@']+)")

data_count = 1

def extract_words(line):
	words = []
	line = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', line)
	line = re.sub(r'^.*\t', '',line)
	line = re.sub(r'@\w+ ', '',line)
	for word in brk.split(line):
		word = word.lower()
		word = stem(word)
		if(word.__contains__("'") or faltu_words.__contains__(word) or word.startswith('@') or len(word)<=2 or len(word) > 15):
			pass
		else:
			words += [word]
	return words

def get_feature_vector(all_words, words):
	feature_vector = [0]*len(all_words)
	j = 0
	for i in range(len(all_words)):
		# print i,j,len(words),len(all_words)
		if(all_words[i] in words):
			feature_vector[i] = 1
	return feature_vector

all_words = []
for filename in filenames:
	fin = open(filename)
	lines = fin.readlines()
	lines = lines[:int(len(lines)*data_count)]
	for line in lines:
		all_words += extract_words(line)

all_words = [k for k,v in Counter(all_words).items() if v >= 2]
all_words = list(set(all_words))
all_words.sort()
print all_words
print len(all_words)


input_vectors = []
output_vectors = []
input_words = []
for i in range(3):
	words = []
	filename = filenames[i]
	output = outputs[i]
	fin = open(filename)
	lines = fin.readlines()
	lines = lines[:int(len(lines)*data_count)]
	for line in lines:
		words = extract_words(line)
		words = list(set(words))
		words.sort()
		input_words+=[words]
		input_vectors+=[get_feature_vector(all_words, words)]
		output_vectors+= [output]

inp = [[x,y,z] for x,y,z in zip(input_vectors, output_vectors, input_words)]
shuffle(inp)
input_vectors = [x[0] for x in inp]
output_vectors = [x[1] for x in inp]
input_words = [x[2] for x in inp]


neurons_per_layer = [len(all_words),3] # first element = number of input lines2

eta = 1
moment = 0
data_sets = [[],[],[],[],[]]
output_sets = [[],[],[],[],[]]
words_set = [[],[],[],[],[]]
for i in range(5):
	print len(input_vectors), int(len(input_vectors)*0.2*i), int(len(input_vectors)*0.2*(i+1))
	data_sets[i] = input_vectors[int(len(input_vectors)*0.2*i):int(len(input_vectors)*0.2*(i+1))]
	output_sets[i] = output_vectors[int(len(input_vectors)*0.2*i):int(len(input_vectors)*0.2*(i+1))]
	words_set[i] = input_words[int(len(input_vectors)*0.2*i):int(len(input_vectors)*0.2*(i+1))]
# 
# training_data = input_vectors[:10]
# target_output = output_vectors[:10]

n_layers = len(neurons_per_layer) - 1
network = []
Input = [0]*neurons_per_layer[0]
# target_output = [[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1]]
# target_output = [[0],[1],[1],[0],[1],[0],[1],[1],[0],[1]]


Output = [0]

class Neuron:

	def __init__(self,temp=-1, index=-1):
		self.layer = temp
		self.index = index
		self.in_weights = []
		self.delta = 0
		self.output = 0
		self.moment_weights = []
		self.init_weights()

	def cal_output(self, Input):
		self.output = 0
		self.output += self.in_weights[0]*-1
		if (self.layer==1):
			for i in range(neurons_per_layer[0]):
				self.output += self.in_weights[i+1]*Input[i]
		else:
			for i in range(neurons_per_layer[self.layer-1]):
				self.output += self.in_weights[i+1]*network[self.layer-2][i].output
		self.output = 1/(1+numpy.exp(-1*self.output))

	def init_weights(self):
		for i in range(neurons_per_layer[self.layer-1]+1):
			self.in_weights += [(2*random()-1)]
			self.moment_weights += [0]

	def cal_delta(self, Output):
		oj = self.output
		if (self.layer==n_layers):
			self.delta = (Output[self.index]-oj)*oj*(1-oj)		#Outer Layer delta = (tj-oj)oj(1-oj)
		else:
			self.delta = 0
			for n in network[self.layer]:
				self.delta += n.in_weights[self.index+1]*n.delta 		#Hidden Layer = sigma Wkj*deltak * oj(1-oj)
			self.delta *= oj*(1-oj)

	def update_weight(self, Input):
		change = self.delta * -1
		self.in_weights[0] += (eta * change) + self.moment_weights[0] * moment
		self.moment_weights[0] = change
		if (self.layer==1):
			for i in range(neurons_per_layer[0]):
				change = self.delta * Input[i]
				self.in_weights[i+1] += (eta * change) + self.moment_weights[i+1] * moment
				self.moment_weights[i+1] = change
		else:
			for i in range(neurons_per_layer[self.layer-1]):
				change = self.delta * network[self.layer-2][i].output
				self.in_weights[i+1] += (eta * change) + self.moment_weights[i+1] * moment
				self.moment_weights[i+1] = change

for l in range(n_layers):
	layers = []
	for i in range(neurons_per_layer[l+1]):
		temp = Neuron(l+1, i)
		layers += [temp]
	network += [layers]

# Generating truth table
# n = neurons_per_layer[0]
# x_vector = []
# fill = 0
# temp = 1

# for i in range(pow(2,n)):
# 	x_vector.append([])
# for i in range(n):
# 	count = 0
# 	for j in range(pow(2,n)):
# 		x_vector[j] = [fill] + x_vector[j]
# 		count += 1
# 		if (count==temp):
# 			count = 0
# 			if (fill==0):
# 				fill = 1
# 			else:
# 				fill = 0
# 	temp *= 2
# test_vector = x_vector
# training_data = [[]]
# training_data = [[0,0],[0,1],[1,0],[1,1]]
# training_data = [[3,5],[2,3],[9,10],[12,15],[2.5,3.5],[-9,15],[100,101],[-1,0],[70,95],[-50,-49]]
# training_data[0] = [0,1,1,1,1,1,1]
# training_data[1] = [0,0,0,1,1,0,0]
# training_data[2] = [1,0,1,1,0,1,1]
# training_data[3] = [1,0,1,1,1,1,0]
# training_data[4] = [1,1,0,1,1,0,0]
# training_data[5] = [1,1,1,0,1,1,0]
# training_data[6] = [1,1,1,0,1,1,1]
# training_data[7] = [0,0,1,1,1,0,0]
# training_data[8] = [1,1,1,1,1,1,1]
# training_data[9] = [1,1,1,1,1,1,0]

import sys
for a in range(1):
	dataI = int(sys.argv[1])
	network = []
	training_data = []
	target_output = []
	for i in range(5):
		if not (i==dataI):
			training_data += data_sets[i]
			target_output += output_sets[i]

	for l in range(n_layers):
		layers = []
		for i in range(neurons_per_layer[l+1]):
			temp = Neuron(l+1, i)
			layers += [temp]
		network += [layers]
	x_vector = training_data
	def update_neurons():
		for x in x_vector:
			Input = x
			Output = target_output[x_vector.index(x)]
			for layer in network:
				for neuron in layer:
					neuron.cal_output(Input)
			for layer in reversed(network):
				for neuron in layer:
					neuron.cal_delta(Output)
			for layer in network:
				for neuron in layer:
					neuron.update_weight(Input)

	def get_error():
		error = 0
		for i in range(len(x_vector)):
			Input = x_vector[i]
			Output = target_output[i]
			for layer in network:
				for neuron in layer:
					neuron.cal_output(Input)
			error += sum([(x-y.output)*(x-y.output) for x,y in zip(Output,network[-1])])
		return error

	def get_output(x_vector, out_vector, test_words):
		truecount = 0
		falsecount = 0
		for i in range(len(x_vector)):
			Input = x_vector[i]
			Output = out_vector[i]
			for layer in network:
				for neuron in layer:
					neuron.cal_output(Input)
			print (test_words[i]),
			maxVar = network[-1][0].output
			for w in network[-1]:
				if(maxVar < w.output):
					maxVar = w.output
				print w.output,
			ans = []
			for w in network[-1]:
				if(maxVar == w.output):
					ans += [1]
				else:
					ans += [0]
			print ans,
			print Output,
			print (ans == Output)
			print('\n')
			print (ans == Output)
			if(ans==Output):
				truecount += 1
			else:
				falsecount += 1
			print('\n')
		return [truecount, falsecount]

	factor = 0;

	cur_error = get_error()
	threshhold = 600
	count = 0
	iterations=0;
	while True:
		iterations+=1
		if (cur_error < threshhold):
			break
		if(count==100):
			count = 0
			factor += 1
			print (factor*100, cur_error)
		count+=1

		print(cur_error)
		# print(prev_error)
		# for layer in network:
		# 	for neuron in layer:
		# 		print(neuron.in_weights)
		# 		print('')
		# 		print(neuron.layer,neuron.index)
		# 		print('')
		# print('\n')
		update_neurons()
		# for layer in network:
		# 	for neuron in layer:
		# 		print(neuron.in_weights)
		temp = cur_error
		cur_error = get_error()
		# temp -= cur_error
		# if (temp>=0.1):
		# 	eta/=2
		# elif (temp<=0.001):
		# 	eta*=2
		# 	if(eta>1): eta/=2
		# else:
		# 	pass

	print(cur_error)
	test_vector = data_sets[dataI]
	test_output = output_sets[dataI]
	test_words = words_set[dataI]
	truecount,falsecount = get_output(test_vector, test_output, test_words)
	print("true", truecount)
	print("false", falsecount)
	print(iterations)

	for layer in network:
		for neuron in layer:
			print neuron.in_weights
	# while (True):
	# 	Input = []
	# 	for i in range(neurons_per_layer[0]):
	# 		Input += [int(input(''))]
	# 	for layer in network:
	# 		for neuron in layer:
	# 			neuron.cal_output(Input)
	# 	print (Input, [w.output for w in network[-1]])
