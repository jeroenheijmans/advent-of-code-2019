import networkx

with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def solve(input):
  entries = list(map(lambda x: x.split(")"), input))
  graph = networkx.Graph()
  graph.add_edges_from(entries)
  return networkx.shortest_path_length(graph, "YOU", "SAN") - 2

print(solve(data))