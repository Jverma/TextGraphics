# -*- coding: utf-8 -*-
#	Python implementation of the LexRank algorithm.
#	Reference - LexRank: Graph-based Centrality as Salience in Text Summarization
#	Reference URL - http://tangra.si.umich.edu/~radev/lexrank/lexrank.pdf

#	Author - Janu Verma
#	email - jv367@cornell.edu
#	http://januverma.wordpress.com/
#	@januverma


import sys
import os
import operator
import networkx as nx
from TextGraphics.src.graph import TextGraph
from TextGraphics import Data




class LexRank:
	"""
	Constructs a summary of the input document by extracting most informative sentences. 

	Arguments:
		directory - A corpus of text files to be summarized. 
	"""
	def __init__(self, directory):
		self.graph = TextGraph(directory)



	def lexR(self, graph):
		"""
		Compute the LexRank of the sentences. 
		LexRank of a sentence in the sentence graph is the PageRank of the node 
		representing the sentence. It is a measure of the importance and influence 
		of the sentence in the corpus. 

		Arguments:
			graph -  A networkx graph or digraph. 

		Returns:
			A dictionary of all the nodes with their PageRank scores. 
		"""

		pr = nx.pagerank_numpy(graph, alpha=0.85)
		return pr




	def summary(self, compression = 0.25):
		"""
		Builds the summary based on the LexRank scores of the sentences.

		Arguments:
			compression : A number in [0,1] which is equal to the fraction of total 
			sentences to be included in the summary. 
			Default value is 0.25

		Returns:
			Summary of the input document.	 
		"""
		g = self.graph.sentenceGraph()
		total_sentences = len(g.nodes())
		n_sentences = int(total_sentences * compression)

		rankings = self.lexR(g)
		ranked_sentences = sorted(rankings.iteritems(), key=operator.itemgetter(1), reverse=True)

		summary_sentences = ""
		i = 0
		while (i < n_sentences):
			u,v = ranked_sentences[i]
			summary_sentences += u
			i = i + 1
		return summary_sentences	









