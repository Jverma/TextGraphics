# -*- coding: utf-8 -*-
#	Modularity of a graph. 
#	Reference - M. E. J. Newman (2006). "Modularity and community structure in networks"
#	Reference URL - http://arxiv.org/abs/physics/0602124

#	Author - Janu Verma
#	email - jv367@cornell.edu
#	http://januverma.wordpress.com/
#	@januverma


import networkx as nx 


class Modularity:
	"""
	Implements the computation of the modularity of a graph. 
	Modularity measures the strength of division of a network into communities. 
	More information - http://en.wikipedia.org/wiki/Modularity_(networks)

	Arguments:
		graph -  a networkx graph or diagraph.
	"""

	def __init__(self, graph):
		self.gr = graph


	def modularity(self):
		"""
		Compute the modularity. 

		Returns:
			Numerical value of the modularity of the graph. 
		"""
		g = self.gr
		A = nx.adj_matrix(g)
		degDict = nx.degree_centrality(g)

		adjDict = {}
		n = A.shape[0]
		B = A.sum(axis=1)
		for i in range(n):
			adjDict[g.nodes()[i]] = B[i,0]

		m = len(g.edges())

		connComponents = nx.connected_components(g)

		mod = 0

		for c in connComponents:
			edgesWithinCommunity = 0
			randomEdges = 0
			for u in c:
				edgesWithinCommunity += adjDict[u]
				randomEdges += degDict[u]
			mod += (float(edgesWithinCommunity) - float(randomEdges * randomEdges)/float(2 * m))	
		mod = mod/float(2 * m)
			
		return mod	
