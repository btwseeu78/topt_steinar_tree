import GraphStructure as GS
import GraphHandler as gh

# These should be taken from user input

n1 = GS.Node(0, 0, 1) #A
n2 = GS.Node(0, 9, 1) #B
n3 = GS.Node(10, 0, 1) #C
n4 = GS.Node(10, 10, 1) #D

# These should never be here and are only for debug purpose

e1 = GS.Edge(n1, n2) #AB
e2 = GS.Edge(n1, n3) #AC
e3 = GS.Edge(n2, n4) #BD
e4 = GS.Edge(n3, n4) #CD
e5 = GS.Edge(n1, n4)

start_nodes = [n1, n2, n3, n4]
start_edges = [] #[e1, e2, e3, e4, e5]

GH = gh.GraphHandler();

for node in start_nodes:
	GH.addNode(node)

for edge in start_edges:
	GH.addEdgeObj(edge)

valueX = ''
valueY = ''

while valueX != 'exit' or valueY != 'exit':
	valueX = float(input("Value X of new node: "))
	valueY = float(input("Value Y of new node: "))
	if isinstance(valueX, ( int, long, float ) ) and isinstance(valueY, ( int, long, float ) ) :
		node = GS.Node(valueX, valueY, 1)
		GH.addNode(node)
		GH.draw()
	else:
		print('Inproper values for X or Y')

