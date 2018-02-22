class Queue:
	def __init__(self, l):
		self.queue = []
		self.queue.extend(l)

	def put(self, item):
		self.queue.append(item)

	def get(self):
		item = self.queue[0]
		self.queue.remove(item)

		return item

	def __len__(self):
		return len(self.queue)

def graph_bfs(adj, start):
	queue = Queue([start])
	visited = set()
	bfs_order = []

	queue.put(start)

	while len(queue) > 0:
		node = queue.get()

		if node in visited:
			continue

		visited.add(node)

		nodes_adjacent = adj[node]
		for n in nodes_adjacent:
			queue.put(n)

		bfs_order.append(node)

	return bfs_order

if __name__ == "__main__":
	adj = {
		'a' : ('b', 'c'),
		'b' : ('a', 'd', 'e'),
		'c' : ('a', 'e'),
		'd' : ('b', 'e', 'f'),
		'e' : ('b', 'd', 'f'),
		'f' : ()
	}

	bfs_order = graph_bfs(adj, 'a')
	print (" ".join(bfs_order))
