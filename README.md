TextGraphics is a python module for graphical methods in text mining. It can create two types of graphs from a corpus of text files. 

1. sentenceGraph - nodes are sentences in the corpus and edges are defined between two nodes based on the cosine similarity of the normalized word frequency vectors of the sentences represented by the nodes. 
2. keywordGraph - nodes are keywords in the corpus and edges are defined between two nodes based on the co-occurances of the keywords represented by the nodes. 

We choose a threshold for cosine similarity or co-occurance count. 

Analysis package contains codes to study basic properties of the graphs and methods to plot the graphs. 
Also there is an implementation of Girvan-Newman algorithm for extracting the communities in the graph. 

Applications imclude auto summarization based on LexRank and topic modeling. 

<b>Dependencies:</b>

1. numpy
2. networkx
3. matplotlib
4. nltk (for stemming only)



<a href="https://pypi.python.org/pypi/textgraphics/0.20"><b> Download</b></a>

<b>Install</b>
pip install textgraphics


<a href="http://pythonhosted.org/textgraphics/"><b>Documentation</b></a>

<b>Usage:</b>

    from TextGraphics.src.graph import TextGraph
    g = TextGraph(corpus)
    senGraph = g.sentenceGraph()
    keyGraph = g.keywordGraph()
    
    from TextGraphics.Applications.summary import LexRank
    lR = LexRank(corpus)
    lR.summary()

See testCode.py for usage. 



