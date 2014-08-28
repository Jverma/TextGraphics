# -*- coding: utf-8 -*-
#	Plots of the graph and its properties. 
#	This will be deprecated and replaced by better viusals 
#	based on R package ggplot2 or d3.js


from __future__ import division
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
#from TextGraphics.src.graph import TextGraph



class Pictures:
	"""
	Analyzing the graph by using drawings. 

	Arguments:
		graph - a networkx graph or digraph. 
	"""

	def __init__(self, graph):
		self.g = graph

	def graphPlot(self, threshold, labelingByNumbers=False):
		"""
		Plot of the (weighted) graph. 

		Arguments:
			threshold - a value of the weight threshold to separate 
						strong edges from weak ones. 

		Returns:
			a matplotlib plot of the graph. 				
		"""	
		nodes = self.g.nodes()

		labels = {}
		for i,s in enumerate(nodes):
			labels[s] = i

		elarge = [(u,v) for (u,v,d) in self.g.edges(data=True) if d['weight'] > threshold]
		esmall = [(u,v) for (u,v,d) in self.g.edges(data=True) if d['weight'] <= threshold]

		pos = nx.spring_layout(self.g)

		nx.draw_networkx_nodes(self.g, pos, node_size=500)

		nx.draw_networkx_edges(self.g, pos, edgelist=elarge, width=3)
		nx.draw_networkx_edges(self.g, pos, edgelist=esmall, width=3, alpha=0.5, edge_color='b', style='dashed')

		if (labelingByNumbers == True): 
			nx.draw_networkx_labels(self.g, pos, font_size=20, font_family='sans_serif', labels=labels)	
		else:
			nx.draw_networkx_labels(self.g, pos, font_size=20, font_family='sans_serif')

		plt.axis('off')
		plt.show()



	def degreePlot(self):
		"""
		Plot the degrees of the nodes. 
		"""

		gr = self.g
		degreeDict = nx.degree_centrality(gr)
		n = len(degreeDict)

		x = range[n]
		y = []

		for sen in degreeDict.keys():
			degree = degreeDict[sen]
			y.append(degree)

		plt.plot(x,y,'ro')
		plt.show()

	def betweennessPlot(self):
		"""
		Plot the betweenness centrality of the nodes. 
		"""		
		gr = self.g
		betweennessDict = nx.betweenness_centrality(gr)
		n = len(betweennessDict)

		x = range[n]
		y = []

		for sen in betweennessDict.keys():
			betweenness = betweennessDict[sen]
			y.append(betweenness)

		plt.plot(x,y,'ro')
		plt.show()

	def closenessPlot(self):
		"""
		Plot the closeness centrality of the nodes. 
		"""	
		gr = self.g
		closenessDict = nx.closeness_centrality(gr)
		n = len(closenessDict)

		x = range[n]
		y = []

		for sen in closenessDict.keys():
			closeness = closenessDict[sen]
			y.append(closeness)

		plt.plot(x,y,'ro')
		plt.show()		





























				

