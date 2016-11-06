#global variables and functions for graphic display management
#to be imported with
#import graphicDisplayGlobalVarAndFunctions as gvf

#useful links

#labels and colors in networkX
#https://networkx.github.io/documentation/latest/examples/drawing/labels_and_colors.html

#look also at
#https://www.wakari.io/sharing/bundle/nvikram/Basics%20of%20Networkx

#Matplotlib colors
#http://matplotlib.org/api/colors_api.html

#html colors
#http://www.w3schools.com/html/html_colornames.asp

# in this module the try/except structures are not cotrolled for debug
# these try/except constucts, indeed, are not intended to control user errors,
# but a regular flow of inputs


import networkx as nx
import matplotlib.pyplot as plt
import commonVar as common


# the base: creating the graph (and copying its address in a common variable
# to have the possibility of direct interaction with the graph when
# the program is finished, as the common space is imported also in the main
# program
def createGraph():
    global colors, pos

    common.g=nx.DiGraph() # directed graph, instead of nx.Graph()
    colors={}
    pos={}
    common.g_labels={}
    common.g_edge_labels={}  #copy the address of the labels of the edges

# searching tools

def findNodesFromSector(sector):
    nodeList=[]
    for aNode in common.g.nodes():
        if common.g.node[aNode]['sector']==sector:
            nodeList.append(aNode)
    return nodeList

def createEdge(a, b):
    # implicitly directed, due to the use of DiGraph
    if a == None or b == None:
       print "Internal error, attempt to create an edge with a node defined None"
       exit(0)

    try:
      common.g[a][b]['weight']= 1+common.g[a][b]['weight']
    except:
      common.g.add_edge(a,b)
      common.g[a][b]['weight']=1

    if a != b:
     # verifying the presence of the edge in the other direction
     try:
      otherW = common.g[b][a]['weight']
      common.g_edge_labels[a,b]="w.s %d and %d" % (common.g[a][b]['weight'],otherW)
      common.g_edge_labels[b,a]=""
     except:
      common.g_edge_labels[a,b]="w. %d" % common.g[a][b]['weight']

    if a == b:
      common.g_edge_labels[a,b]=""
      common.g[a][b]['pseudoLabel']="auto link w. %d" \
                                      % common.g[a][b]['weight']


# using networkX and matplotlib case
def closeNetworkXdisplay():
    plt.close()

def openClearNetworkXdisplay():
    if common.graphicStatus == "PythonViaTerminal": plt.ion()
    #plt.clf()

def clearNetworkXdisplay():
    plt.clf()

def getGraph():
    try:
        return common.g
    except:
        return 0


def pruneEdges():

    if not common.prune: return
    common.prune=False

    print "New threshold to prune: < %d" % common.pruneThreshold

    edges=common.g.edges()
    print "weights of the links"
    for anEdge in edges:
        u = anEdge[0].number
        uu= anEdge[0]
        v = anEdge[1].number
        vv= anEdge[1]
        w = common.g[anEdge[0]][anEdge[1]]["weight"]
        print u, v, w

        if w < common.pruneThreshold:
            # managing labels, related to createEdge phase above
            common.g_edge_labels.pop((uu,vv))
            try: common.g_edge_labels[vv,uu]="w. %d" % common.g[vv][uu]['weight']
            except: pass
            if uu==vv:
                common.g[uu][uu]['pseudoLabel']=""
                common.g_labels[uu]=str(uu.number)+" ("+\
                                    str(len(uu.recipeWaitingList))+")"
            #removing
            common.g.remove_edge(uu, vv)


def drawGraph():


    #directed, due to the use of DiGraph

    # draw_netwokx is well documented at
    # https://networkx.github.io/documentation/latest/reference/
    # generated/networkx.drawing.nx_pylab.draw_networkx.html
    #nx.draw_networkx(agentGraph,    font_size=10,node_size=500, \
    clearNetworkXdisplay()
    pruneEdges()
    nx.draw_networkx(common.g,pos,font_size=10,node_size=500, \
         node_color=colors.values(), \
         labels = common.g_labels)
    nx.draw_networkx_edge_labels(common.g,pos,edge_labels=common.g_edge_labels,\
                                 font_size=9)
    #plt.draw()
    plt.show() # used by %Matplotlib inline [without ion()]; not conflicting
               # with ion()

    if common.graphicStatus == "PythonViaTerminal": plt.pause(0.01)
    # to show the sequence of the shown images in absence of pauses


    #print agentGraph.nodes(data=True)
    #print agentGraph.edges(data=True)
    #print labels
    #print edge_labels

    #print a, agentGraph.node[a].keys(), agentGraph.node[a].values(),\
    #      agentGraph.node[a]['sector']


    # adjacency
    print
    for i in range(len(common.orderedListOfNodes)):
      print "%d " % common.orderedListOfNodes[i].number,
    print
    #print "drawGraph verification of existing nodes",common.g.nodes()
    if common.g.nodes() !=[]:
        A = nx.adjacency_matrix(common.g, nodelist=common.orderedListOfNodes, \
                              weight='weight')
        #print A          # as sparse matrix, defaul from nx 1.9.1
        print A.todense() # as a regular matrix

    else: print "No nodes, impossible to create the adjacency_matrix"
    print

    # neighbors

    for aNode in common.g.nodes():
        print aNode.number, [node.number \
                                   for node in nx.neighbors(common.g,aNode)]

    # betweenness_centrality
    # Betweenness centrality of a node v is the sum of the fraction of all-pairs
    # shortest paths that pass through v
    # http://networkx.lanl.gov/reference/generated/
    # networkx.algorithms.centrality.betweenness_centrality.html
    print
    print "betweenness_centrality"
    common.btwn = nx.betweenness_centrality(common.g, normalized=False, weight='weight')
    #print btw
    for i in range(len(common.orderedListOfNodes)):
        print common.orderedListOfNodes[i].number, \
              common.btwn[common.orderedListOfNodes[i]]

    # closeness_centrality
    # Closeness centrality at a node is 1/average distance to all other nodes
    # http://networkx.lanl.gov/reference/generated/
    # networkx.algorithms.centrality.closeness_centrality.html
    print
    print "closeness_centrality"
    common.clsn = nx.closeness_centrality(common.g, normalized=False)
    #print clsn
    for i in range(len(common.orderedListOfNodes)):
        print common.orderedListOfNodes[i].number, \
              common.clsn[common.orderedListOfNodes[i]]
