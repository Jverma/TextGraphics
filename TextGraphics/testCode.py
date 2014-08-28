from TextGraphics.src.graph import TextGraph
from TextGraphics.Analysis.plotting import Pictures
from TextGraphics.Analysis.properties import Analysis
from TextGraphics.Applications.summary import LexRank


directory = 'Data'
g = TextGraph(directory)
senGraph = g.sentenceGraph()
node = senGraph.nodes()[0]

out = Pictures(senGraph)
out.graphPlot(0.3, labelingByNumbers=True)

out1 = Analysis(senGraph)
l = out1.nodeInConnectedComponent(node)
print l.nodes()

cS = out1.centralNodes(4)
print cS

lR = LexRank(directory)
print lR.summary()