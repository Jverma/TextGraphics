# -*- coding: utf-8 -*-
# 	A graphical representation of a corpus of text documents. 
# 	Author - Janu Verma
# 	jv367@cornell.edu
# 	@januverma


from __future__ import division
import sys
from collections import *
import operator
import os
from math import *


try:
	import networkx as nx 
except:
	print "Error : Requires networkx"
	sys.exit()	


stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
stopwords = set(stopwords)



class TextGraph:
	"""
	Graphical representation of a corpus of text files. 

	Two types of graphs can be created :
	SentenceGraph - Nodes are the sentences in the corpus and an edge is defined between sentences
					based on their similarity.
	KeywordGraph - Nodes are the keywords in the corpus and edges are defined between two words
					based on their cooccurances in the documents. 
	"""
	def __init__(self, directory):
		"""
		Arguments:
			directory - A corpus of text files. 	
		"""
		self.corpus = os.listdir(directory)

		self.text = {}
		for f in self.corpus:
			f = os.path.join(directory,f)
			with open(f) as doc:
				info = doc.read()
				self.text[f] = info

		self.sentences = {}
		for f in self.text.keys():
			contents = self.text[f]
			self.sentences[f] = []
			paragraphs = [s for s in contents.splitlines() if s]
			for p in paragraphs:
				lines = [l for l in p.split('.') if l]
				self.sentences[f].extend(lines)


	def wordFrequency(self, sentence, stemming=False):
		"""
		Compute the normalized frequency of occurance of words in the sentence. 

		Arguments:
			sentence : A sentence
			stemming : If True, words will be stemmed by Porter stemming.
						Stemming requires package nltk. 


		Returns:
			A dictionary of all the words with their normalized frequencies 
			of occurance in the sentence. 	
		"""
		freq_dict = defaultdict(float)
		words = sentence.split()
		words = [x.lower() for x in words]
		words = [x for x in words if len(x) >= 2 and not x.isdigit()]
		for word in words:
			if not(word in stopwords):
				if (stemming == True):
					try:
						from nltk import PorterStemmer
					except:
						print "Error : Requires nltk for Stemming"	
					word = PorterStemmer().stem_word(word)
				freq_dict[word] += 1
		if len(freq_dict) != 0:
			max_freq = max(freq_dict.iteritems(), key=operator.itemgetter(1))[1]
		for w in freq_dict.keys():
			freq_dict[w] = float(freq_dict[w])
		return freq_dict
		


	def sentenceIntersection(self, s1,s2, stemming=False):
		"""
		Compute the cosine similarity of two sentences. 
		Similarity is defined as the cosine similarity of the vectors
		representating the sentences. 

		Arguments:
			s1 : sentence 1
			s2 : sentence 2
			stemming : If True, words will be stemmed by Porter stemming.
						Stemming requires package nltk. 


		Returns:
			A float number defining the similarity of the sentences. 	
		"""		
		w1 = self.wordFrequency(s1, stemming)
		w2 = self.wordFrequency(s2, stemming)
		key1 = w1.keys()
		key2 = w2.keys()
		if (len(key1) == 0) or (len(key2) == 0):
			return 0
		else:
			sum1Sq = sum([pow(w1[x],2) for x in key1]) 
			sum2Sq = sum([pow(w2[x],2) for x in key2]) 	
			commonKeys = set(key1) & set(key2)
			dotProduct = sum([w1[x]*w2[x] for x in commonKeys])
			sim = dotProduct/(sqrt(sum1Sq)*sqrt(sum2Sq))
			return sim
	

	def sentenceGraph(self, similarityThreshold=0.2, stemming=False):
		"""
		Build the sentence graph. 

		Arguments:
			similarityThreshold : If the similarity of two sentences is above
			similarityThreshold, there is an edge between the nodes represented
			by the sentences. 
			Default value is 0.1
			stemming : If True, words will be stemmed by Porter stemming.
						Stemming requires package nltk. 


		Returns:
			A networkx graph with sentences as nodes and there is an edge between two nodes
			if their similarity value is greater than similarityThreshold. 	
		"""
		g = nx.Graph()
		for f in self.sentences.keys():
			sentences = self.sentences[f]
			for s in sentences:
				g.add_node(s)
		for n1 in g.nodes():
			for n2 in g.nodes(): 
				weight_value = self.sentenceIntersection(n1,n2, stemming)
				if (weight_value > similarityThreshold):
					g.add_edge(n1,n2, weight = weight_value)


		return g	


	def words(self, d):
		"""
		Compute all the  words in a document. 

		Arguments:
			d : a document

		Returns:
			A list of all the words in the document. 	
		"""
		documents = self.text
		document = documents[d]
		words = document.split()
		words = [x.lower() for x in words]
		words = [x for x in words if not x in stopwords]
		words = [x for x in words if len(x) >= 2 and not x.isdigit()]
		return words		


	def wordDocs(self, d):
		"""
		Arguments:
			d : a document

		Returns:
			A dictionary of all the words in d with d as value. 	
		"""

		docDict = {}
		words = self.words(d)
		words = set(words)
		for w in words:
			docDict[w] = d
		return docDict

	def vocabalury(self):
		"""
		Compute all the unique words in the corpus. 

		Returns:
			A set of all the unique words in the whole corpus of documents. 
		"""
		allDocs = self.text
		allWords = []
		for d in allDocs.keys():
			docWords = self.words(d)
			allWords.extend(docWords)
		allWords = set(allWords)
		return allWords


	def docsContainingWords(self):
		"""
		Compute the documents containg a given word. 

		Returns:
			A dictionary of all the words in the corpus with the value a list
			of all the documents containg the word. 
		"""
		allDocs = self.text
		allWords = self.vocabalury()

		docsContainingWord = {}
		for x in allWords:
			docsContainingWord[x] = []
			for d in allDocs.keys():
				docsForWord = self.wordDocs(d)
				if (x in docsForWord.keys()):
					docsContainingWord[x].append(docsForWord[x])
		return docsContainingWord						


	def keywordGraph(self, cooccuranceThreshold=1):
		"""
		Build the keyword graph. 

		Arguments:
			cooccuranceThreshold : If the cooccurances of two keywords is above
			coocuranceThreshold, there is an edge between the nodes represented
			by the keywords. 
			Default value is 1

		Returns:
			A networkx graph with keywords as nodes and there is an edge between two nodes
			if their similarity value is greater than similarityThreshold.
		"""	
		docsForWords = self.docsContainingWords()
		h = nx.Graph()
		for w in self.vocabalury():
			h.add_node(w)

		for w1 in h.nodes():
			for w2 in h.nodes():
				weight = len(set(docsForWords[w1]) & set(docsForWords[w2]))
				if (weight > cooccuranceThreshold):
					h.add_edge(w1,w2,weight=weight)

		return h				







