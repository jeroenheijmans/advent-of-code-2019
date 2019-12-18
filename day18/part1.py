import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

def neighbors(level, p):
  all = [
    (p[0] + 1, p[1]),
    (p[0] - 1, p[1]),
    (p[0], p[1] + 1),
    (p[0], p[1] - 1),
  ]

  return [x for x in all if level[x] != "#"]

def drawascii(level):
  maxx = max([x for x,_ in level.keys()])
  maxy = max([y for _,y in level.keys()])
  for y in range(maxy+1):
    line = ""
    for x in range(maxx+1):
      line += level[(x,y)]
    print(line)

def draw(g, spaces, doors, keys, position):
  pos = nx.get_node_attributes(g, 'pos')
  
  nx.draw_networkx_nodes(g, pos, node_size=200, nodelist=[position], node_color='#eeee00', alpha=0.9)
  nx.draw_networkx_nodes(g, pos, node_size=30, nodelist=spaces, node_color='#00aaee', alpha=0.8)
  nx.draw_networkx_nodes(g, pos, node_size=150, nodelist=doors.values(), node_color='#ee0033', alpha=0.8)
  nx.draw_networkx_nodes(g, pos, node_size=150, nodelist=keys.values(), node_color='#33ee66', alpha=0.8)
  
  nx.draw_networkx_edges(g, pos, alpha=0.6)

  labels = nx.get_node_attributes(g,'label')
  nx.draw_networkx_labels(g, pos, labels=labels, font_size=11, alpha=0.4)
  
  labels = nx.get_edge_attributes(g,'weight')
  nx.draw_networkx_edge_labels(g, pos, font_size=7, edge_labels=labels)

  plt.show()

def createGameFrom(level, position):
  keepgoing = True
  curgraph = nx.Graph()
  curgraph.add_node(position, label="@", pos=(position[0], -position[1]))
  visited = set([position])
  spaces = set()
  keys = dict()
  doors = dict()
  tovisit = set([position])
  nextvisits = set()
  while keepgoing:
    for p in tovisit:
      for n in neighbors(level, p):
        if n in visited or level[n] in ["#", "@"]:
          continue
        if level[n] in ["."]:
          weight = 1
          while True:
            nextneighbors = neighbors(level, n)
            others = [x for x in nextneighbors if x != p and x != n and x not in visited]
            if len(others) != 1 or level[others[0]] != ".": break
            # print("skipping through", n, "to", others)
            visited.add(n)
            n = others[0]
            weight += 1
          nextvisits.add(n)
          visited.add(n)
          spaces.add(n)
        elif level[n].islower():
          nextvisits.add(n)
          visited.add(n)
          keys[level[n]] = n
        else:
          nextvisits.add(n)
          visited.add(n)
          doors[level[n].lower()] = n

        # print("adding node", n, level[n])
        label = '' if level[n] == '.' else level[n]
        curgraph.add_node(n, pos=(n[0], -n[1]), label=label)
        curgraph.add_edge(p, n, weight=weight)

    keepgoing = len(nextvisits) > 0
    tovisit = nextvisits
    nextvisits = set()
  return curgraph, spaces, doors, keys

def solve(data):
  x, y = 0, 0
  level = defaultdict(lambda: '#')
  for line in data:
    for c in line:
      if c == "@": position = (x,y)
      level[(x,y)] = '.' if c == "@" else c
      x += 1
    x = 0
    y += 1

  curgraph, spaces, doors, keys = createGameFrom(level, position)
  
  # drawascii(level)
  print(len(doors), 'Doors:', doors.keys())
  print(len(keys), 'Keys:', keys.keys())
  draw(curgraph, spaces, doors, keys, position)

  return None

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

print("Part 1:", solve(raw))
