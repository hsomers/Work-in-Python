from chapter12DFS import *

def getDigraph(data):
    """Assumes data is a txt file describing a directed graph
    as printed by the class Digraph. The last line of the file is EOF"""
    
    alpha=Digraph()   #prepare Digraph object
    nodeDict ={}     #a node dictionary that will be keyed by name
    
    infile=open(data,'r')  #open data file
    
    line=infile.readline()  #read initial line
    lineTrimmed=line[:-1]  #remove line feed
    while lineTrimmed != 'EOF':  #loop until EOF
        linelist=lineTrimmed.split(',') #split line into a list
        n1=linelist[0]   #name of source node
        n2=linelist[1]   #name of destination node
   
    #check the node dictionary for existing nodes
        if n1 in nodeDict:  #if node exists use it
            sourcenode=nodeDict[n1]
        else:  #if node isn't in dictionary 
            sourcenode=Node(n1)     #create node
            nodeDict[n1]=sourcenode  #put node in node dictionary
            alpha.addNode(sourcenode) #add node to alpha
        
        if n2 in nodeDict:
            destnode=nodeDict[n2]
        else:
            destnode=Node(n2)
            nodeDict[n2]=destnode
            alpha.addNode(destnode)
            
        edge1=Edge(sourcenode,destnode)   #make the edge sourcenode->destnode
        alpha.addEdge(edge1) #add the edge to alpha
        edge2=Edge(destnode, sourcenode) # make the edge destnode->sourcenode
        alpha.addEdge(edge2) #add the edge to alpha
        line=infile.readline() #go to next line
        lineTrimmed=line[:-1]
    
    infile.close()  #close data file
    
    return alpha  #return the digraph
    
def findMaxClique():
    alpha = getDigraph('social.txt') 
    maxcliqueVal = 0                        #Set the maxclique value to zero                                          
    for src in alpha.nodes:             #for each node in the social network
        clique = []                     #create a new clique...
        clique.append(src)              #and add the original node
        for i in alpha.childrenOf(src): #for each child of the original node...
            for j in clique:            #for each item in the clique...
                if i == j:              #if i is the same as j, it won't be a child of itself, so just pass
                    pass
                elif i in alpha.childrenOf(j): #if i is a child of j, then append i to the clique
                    clique.append(i)
                else:                   #however, if i is not a child of any of the items, remove it from the list and break the loop
                    clique.remove(i)
                    break
        clique2 = []                    #set a new clique list to change the nodes to their respective names
        for node in clique:             #for each node in the clique list...
            name = node.getName()       #name is the name in a string format
            clique2.append(name)        #append the name to clique2
            cliqueSet = set(clique2)    #make clique2 into a set so that no names will repeat
            if len(cliqueSet)>maxcliqueVal: #if the size of the clique set is larger than the current...
                                            #value for maxclique, then change the value of maxclique
                maxcliqueVal = len(cliqueSet)
                maxclique = cliqueSet       #also set the maxclique to the clique that is largest
    print(maxcliqueVal)                    #print the size of the max clique
    print(maxclique)                       #print the maximum clique
            
            
            
            