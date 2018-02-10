# Randomised contraction algo to find min cut of a graph

from collections import defaultdict
import random

class Graph:
	def __init__(self):
		# List of edges
		self.list_edges = []
		# List of vertices
		self.list_vertices = []
		# Mapping of edges -> vertex endpoint
		self.edge_vertex = dict()
		# Mapping of vertex -> edges
		self.vertex_edge = defaultdict(list)

	def add_edge(self, edge_name, vertex1, vertex2):
		self.list_edges.append(edge_name)

		if vertex1 not in self.list_vertices:
			self.list_vertices.append(vertex1)
		if vertex2 not in self.list_vertices:
			self.list_vertices.append(vertex2)

		self.edge_vertex[edge_name] = (vertex1, vertex2)

		self.vertex_edge[vertex1].append(edge_name)
		self.vertex_edge[vertex2].append(edge_name)

	def del_edge(self, edge):
		del(self.edge_vertex[edge])
		self.list_edges.remove(edge)

	def contract(self, v1, v2, edge):
		edges = self.vertex_edge[v1]
		for e in edges:
			if e == edge:
				continue

			# Continue because self-loop was terminated
			if e not in self.list_edges:
				continue

			# Replace v1 for the edge
			va, vb = self.edge_vertex[e]
			if va == v1:
				self.edge_vertex[e] = (v2, vb)
			else:
				self.edge_vertex[e] = (v2, va)

			# Remove self-loop edge
			va, vb = self.edge_vertex[e]
			if va == vb:
				self.del_edge(e)

		# Remove v1 from list of vertices
		self.list_vertices.remove(v1)

	def min_cut(self):
		while len(self.list_vertices) > 2:
			edge = random.choice(self.list_edges)
			v1, v2 = self.edge_vertex[edge]
			self.contract(v1, v2, edge)
			self.del_edge(edge)

		return self.list_edges

if __name__ == "__main__":
	graph = Graph()

	graph.add_edge("e1", "v1", "v2")
	graph.add_edge("e2", "v1", "v3")
	graph.add_edge("e3", "v2", "v3")
	graph.add_edge("e4", "v2", "v4")
	graph.add_edge("e5", "v3", "v4")

	print (graph.min_cut())
