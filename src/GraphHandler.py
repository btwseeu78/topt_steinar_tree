try:
	import GraphStructure as GS
	import networkx as nx
	import matplotlib.pyplot as plt
except:
	raise


class GraphHandler:
	xs = []
	ys = []
	originalPoints = []
	allPoints = dict()
	hananPoints = set()

	def __init__(self):
		self.G = nx.Graph()
		self.drawer = Drawer(self.G)

	def addNode(self, node):
		self.G.add_node(node, posxy=(node.x, node.y), type=node.type)
		self.allPoints[(node.x, node.y)] = node
		if node.type == 1:
			self.originalPoints.append(node)
			self.addHananPoints(node)
		elif node.type == 2:
			self.hananPoints.add(node)

	def addEdge(self, start, end):
		edge = GS.Edge(start, end)
		self.G.add_edge(edge.n1, edge.n2, weight=edge.weight)

	def addEdgeObj(self, edge):
		self.G.add_edge(edge.n1, edge.n2, weight=edge.weight)

	def draw(self):
		self.createHananGrid()
		self.connectInputsWithHannan()
		mst = nx.minimum_spanning_tree(self.G, weight='weight')
		self.drawer.draw(mst) # draws only MST
		#self.drawer.draw(self.G) # draws whole graph

	def addHananPoints(self, node):
		if node.x not in self.xs:
			self.xs.append(node.x)
			self.xs.sort()
		if node.y not in self.ys:
			self.ys.append(node.y)
			self.ys.sort()
		for x in self.xs:
			for y in self.ys:
				hananNode = GS.Node(x, y, 2)
				i = 0
				for origPoints in self.allPoints.iteritems():
					i += 1
					if origPoints[1].__eq__(hananNode):
						i = -1
						break
				if i != -1:
					self.addNode(hananNode)

	def createHananGrid(self):
		for indexX in range(len(self.xs)):
			for indexY in range(len(self.ys)):
				start = self.allPoints[(self.xs[indexX], self.ys[indexY])]
				#connect to the one on the right:
				if indexX+1<len(self.xs):
					end = self.allPoints[(self.xs[indexX+1], self.ys[indexY])]
					self.addEdge(start, end)
				#connect to the one below:
				if indexY+1<len(self.ys):
					end = self.allPoints[(self.xs[indexX], self.ys[indexY+1])]
					self.addEdge(start, end)

	def connectInputsWithHannan(self):
		for origPoint in self.originalPoints:
			for hananPoint in self.hananPoints:
				self.addEdge(origPoint, hananPoint)



class Drawer:
	def __init__(self, graph):
		self.G = graph;

	def draw(self, data):
		pos=nx.get_node_attributes(self.G,'posxy') # positions for all nodes
		type=nx.get_node_attributes(self.G, 'type')
		userInput=self.G.subgraph( [n for n,attrdict in self.G.node.items() if attrdict['type'] == 1 ] )
		hananInput=self.G.subgraph( [n for n,attrdict in self.G.node.items() if attrdict['type'] == 2 ] )
		heuristicsInput=self.G.subgraph( [n for n,attrdict in self.G.node.items() if attrdict['type'] == 3 ] )

		# nodes
		# nx.draw_networkx_nodes(self.G,pos,nodelist=self.G.nodes(), node_size=700)
		nx.draw_networkx_nodes(self.G,pos,nodelist=userInput, node_size=700, node_color='r') #draws nodes from user input
		nx.draw_networkx_nodes(self.G,pos,nodelist=hananInput, node_size=700, node_color='g') #draws Hanan nodes
		nx.draw_networkx_nodes(self.G,pos,nodelist=heuristicsInput, node_size=700, node_color='b') #draws heuristic nodes

		# edges
		nx.draw_networkx_edges(data, pos)

		# labels
		# nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif')

		plt.axis('on')
		plt.savefig("weighted_graph.png") # save as png
		plt.show() # display