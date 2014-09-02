# -*- coding: utf-8 -*-
#	SimRank of the nodes in a graph. 
#	Reference - G. Jeh and J. Widom. "SimRank: a measure of structural-context similarity".
#	Reference URL - 

#	Author - Janu Verma
#	email - jv367@cornell.edu
#	http://januverma.wordpress.com/
#	@januverma


import networkx as nx 
import numpy as np 
import itertools

class SimRank:
	"""
	SimRank is a vertex similarity measure. It computes the similarity between two nodes on a graph based on the topology, 
	i.e., the nodes and the links of the graph.
	More information - 

	Arguments:
		graph -  a networkx graph
	"""

	def __init__(self, graph):
		self.gr = graph

	def simrank(self, r=0.9, max_iter=100, epsilon=1e-4):
		"""
		Compute the SimRank of the graph. 

		Arguments:
			r - relative importance factor. 
			It represents the relative importance between in-direct neighbors and direct neighbors.
			max_iter - maximum number of iterations.
			epsilon - convergence threshold. 

		Returns:
			A matrix (numpy array) containing the simrank scores of the nodes.	
		"""
		g = self.gr
		nodes = g.nodes()
		n = len(nodes)
		nodesDict = {node:i for (i,node) in enumerate(nodes)}
		print nodesDict

		prevSim = np.zeros(n)
		newSim = np.identity(n)

		for i in range(max_iter):
			if (np.allclose(newSim, prevSim, atol=epsilon)):
				break
			prevSim = np.copy(newSim)
			
			for n1 in nodes:
				for n2 in nodes:
					if (n1 == n2):
						continue

					simrank12 = 0.0	
					neighbors1 = g.neighbors(n1)
					neighbors2 = g.neighbors(n2)
					for u in neighbors1:
						for v in neighbors2:
							simrank12 += prevSim[nodesDict[u]][nodesDict[v]]
					newSim[nodesDict[n1]][nodesDict[n2]] = (r * simrank12)/(len(neighbors1)  * len(neighbors2))
			
		return newSim

