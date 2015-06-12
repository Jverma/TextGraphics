# -*- coding: utf-8 -*-
#	Some properties of the graph. 
#	Most of these operations are taken from the basic Networkx package. 

import networkx as nx
import operator


class Properties:
	"""
	Some important properties of the graph. 

	Arguments:
		graph -  A networkx graph or digraph. 
	"""
	def __init__(self, graph):
		self.g = graph

	def ConnectedComponents(self):
		"""
		Compute the connected components of the graph.

		Returns:
			a list containing lists of nodes in each connected components. 
		"""	

		gr = self.g
		conn_comps = nx.connected_component_subgraphs(gr, copy=True)
		return list(conn_comps)

	def nodeInConnectedComponent(self, node):
		"""
		Place a node in a connected component of the graph. 

		Arguments:
			node - the node whose connected component is desired. 

		Returns:
			A connected subgraph of the original graph which contains the node.	
		"""	
		gr = self.g
		neighhboringNodes = nx.node_connected_component(gr, node)
		subgraph = nx.subgraph(gr, neighhboringNodes)
		return subgraph


	def centralNodes(self, nNodes, closeness=False, betweenness=False):
		"""
		Compute the most central nodes. It measure how important/central in the graph a node is. 
		We have three metrics for measuring centrality ---

		Degree Centrality : The degree centrality for a node v is the fraction of nodes it is connected to.
							This is the default measure. 

		Closeness Centrality : Closeness centrality of a node u is the reciprocal of the sum of the 
								shortest path distances from u to all n−1 other nodes. 
								(http://en.wikipedia.org/wiki/Centrality#Closeness_centrality)

		Betweenness Centrality : Betweenness centrality of a node v is the sum of the fraction of all-pairs 
								shortest paths that pass through v. 
								(http://en.wikipedia.org/wiki/Betweenness_centrality)


		Arguments:
			nNodes - number of most central nodes to be retrieved. 
			closeness : If True, the closeness centrality is evaluated. 
			betweenness : If True, the betweenness centrality is evaluated. 
		
		Returns:
			A list of most central nodes. 				
		"""
		gr = self.g
		if (closeness == True):
			centralityDict = nx.closeness_centrality(gr)
		if (betweenness == True):
			centralityDict = nx.betweenness_centrality(gr)
		else:
			centralityDict = nx.degree_centrality(gr)


		sortedCentralityDict = sorted(centralityDict.iteritems(), key=operator.itemgetter(1), reverse=True)
		
		central_nodes = []
		i = 0
		while (i < nNodes):
			u,v = sortedCentralityDict[i]
			central_nodes.append(u)
			i += 1

		return central_nodes	


		

























