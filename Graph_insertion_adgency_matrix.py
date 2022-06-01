def add_node(node):
    global node_count
    if node in nodes:
        print('The node is present in the graph so we cant add')
    else:
        node_count+=1
        nodes.append(node)
        for i in graph:
            i.append(0)
        temp=[]
        for i in range(len(nodes)):
            temp.append(0)
        graph.append(temp)
            
def print_graph():
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            print(format(graph[i][j],'<3'),end=' ')
        print()
def add_edge(x,y,cost):
    if x not in nodes:
        print('Nodes are not present in graph')
    else:
        graph[nodes.index(x)][nodes.index(y)]=cost
        graph[nodes.index(y)][nodes.index(x)]=cost
node_count=0
graph=[]
nodes=[]
add_node('A')
add_node('B')

add_node('C')
add_edge('A','B',30)

print(nodes)
print_graph()