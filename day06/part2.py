import networkx as nx
import matplotlib.pyplot as plt

with open('input.txt', 'r') as file:
  data = file.read().splitlines()

def solve(input):
  entries = list(map(lambda x: (x.split(")")[0], x.split(")")[1]), input))
  graph = nx.Graph()

  for a,b in entries:
    graph.add_edge(a,b)

  # nx.draw(graph)
  # plt.show()

  return nx.shortest_path_length(graph, "YOU", "SAN") - 2

print(solve(data))