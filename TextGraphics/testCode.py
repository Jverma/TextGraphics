from TextGraphics.src.graph import TextGraph
from TextGraphics.Analysis.plotting import Pictures
from TextGraphics.Analysis.properties import Analysis
from TextGraphics.Applications.summary import LexRank


##  Import the corpus of text files.
directory = 'Data'

##  Create the sentence graph 
g = TextGraph(directory)
senGraph = g.sentenceGraph()
node = senGraph.nodes()[0]

##  Plot the sentence graph 
out = Pictures(senGraph)
out.graphPlot(0.3, labelingByNumbers=True)

# Compute the keyword graph
kwgraph = g.keywordGraph()
print len(kwgraph.nodes())

##  Plot the keyword graph 
out = Pictures(kwgraph)
out.graphPlot(0.3, labelingByNumbers=True)



#### Analysis
out1 = Analysis(senGraph)

# Find the connected component of a node. 
l = out1.nodeInConnectedComponent(node)
print l.nodes()

# Print 4 most central nodes. 
cS = out1.centralNodes(4)
print cS

# Compute the Keygraph
out2 = KeyGraph(directory)
keygraph = out2.network()
print len(keygraph.nodes())

# Compute the modularity of the keygraph
modul = Modularity(keygraph)
print modul.modularity()
lR = LexRank(directory)
print lR.summary()


