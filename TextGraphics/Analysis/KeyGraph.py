# -*- coding: utf-8 -*-
#	Implement the KeyGraph of a corpus of textual files. 
#	Reference - H. Sayyadi, L. Raschid. "A Graph Analytical Approach for Topic Detection", ACM Transactions on Internet Technology (TOIT), 2013

#	Author - Janu Verma
#	email - jv367@cornell.edu
#	http://januverma.wordpress.com/
#	@januverma


import networkx as nx 
from TextGraphics.src.graph import TextGraph

class KeyGraph:
	"""
	Implements the KeyGraph from the keywordGraph. 
	KeyGraph is a slight modification of the keywordGraph as defined in the paper ...
	KeyGraph is used in extracting topics for the corpus of the documents.

	Arguments:
		directory : a corpus of text files. 
		cooccuranceThrehsold : If the cooccurances of two keywords is above
			coocuranceThreshold, there is an edge between the nodes represented
			by the keywords. 
			Default value is 1
	"""

	def __init__(self, directory, cooccuranceThrehsold=1):
		self.corpus = directory
		self.model = TextGraph(directory)
		self.graph = self.model.keywordGraph(cooccuranceThrehsold)
		self.docFreqDict = self.model.docFreq()



	def probCoocurance(self, keyword1, keyword2):
		"""
		Compute the probability of cooourance of a keyword in a document
		given a given keyword occurs in the document.

		Arguments:
			keyword1 : first keyword. 
			keyword2 : second keyword.

		Returns:
			Numerical value of the probability.	 
		"""	
		documentFrequencyDict = self.docFreqDict
		docsContainingKeyword1 = set(documentFrequencyDict[keyword1])
		docsContainingKeyword2 = set(documentFrequencyDict[keyword2])

		commonDocs = len(docsContainingKeyword1 & docsContainingKeyword2)
		prob = commonDocs/len(docsContainingKeyword1)

		return prob



	def network(self, docFreqThreshold=2, probThreshold=0.01):
		"""
		Compute the KeyGraph. 	

		Arguments:
			docFreqThreshold : If the documnet frequency of a keyword is below
								the docFreqThreshold, then the node corresponding
								to the keyword is removed from the graph. 
								Default value is 1.
		"""	
		g = self.graph
		allNodes = g.nodes()
		allEdges = g.edges()
		documentFrequency = self.docFreqDict

		for x in allNodes:
			if (len(documentFrequency[x]) < docFreqThreshold):
				g.remove_node(x)

		for e in allEdges:
			node1 = e[0]
			node2 = e[1]
			if (self.probCoocurance(node1,node2) < probThreshold) or (self.probCoocurance(node2, node1) < probThreshold):
				g.remove_edge(node1,node2)				
		return g		
