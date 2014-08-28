# -*- coding: utf-8 -*-
#	Community detection by Girvan - Newman algorithm.
#	Reference - Community structure in social and biological networks  
#	Reference URL - http://www.pnas.org/content/99/12/7821

#	Author - Janu Verma
#	email - jv367@cornell.edu
#	http://januverma.wordpress.com/
#	@januverma


#import sys
#import os
#import operator
import networkx as nx
from src.graph import TextGraph



class GirvanNewman:
	"""
	Implements the Girvan - Newman algorithm for community detection in a graph. 

	Arguments:
		graph - A networkx graph or digraph. 
	"""

	def __init__(self, graph):
		self.g = graph



	def communitySplits(self, graph):
		"""
		Compute the splits for the formation of communities. 

		Arguments:
			graph -  A networkx graph of digraph. 

		Returns:
			The graph with weak edges removed. 	
		"""

		nConnComp = nx.number_connected_components(graph)
		nComm = nConnComp

		while (nComm <= nConnComp):
			betweenness = nx.edge_betweenness_centrality(graph)
			if (len(betweenness.values()) != 0 ):
				max_betweenness = max(betweenness.values())
			else:
				break	
			for u,v in betweenness.iteritems():
				if float(v) == max_betweenness:
					graph.remove_edge(u[0], u[1])
			nComm = nx.number_connected_components(graph)			
		return graph		


	def communities(self, nCommunities):
		"""
		Compute communities.

		Arguments:
			nCommunities - number of communities to be returned. T
			This is added to simplify the process, the original GN algorithm doesn't 
			need predecided number of communities. 
			Other measures like a threshold on betweenness centrality can be used instead. 

		Returns:
			A list of communities where each community is a list of the nodes in the community.	 
		"""
		gr = self.g
		n = nx.number_connected_components(gr)
		components = nx.connected_components(gr)

		while (n < nCommunities):
			gr = self.communitySplits(gr)
			components = nx.connected_components(gr)
			n = nx.number_connected_components(gr)
			if gr.number_of_edges() == 0:
				break
		return components
					
		



