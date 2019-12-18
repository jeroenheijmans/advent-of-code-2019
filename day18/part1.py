import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

def neighbors(level, p):
  return [
    (p[0] + 1, p[1]),
    (p[0] - 1, p[1]),
    (p[0], p[1] + 1),
    (p[0], p[1] - 1),
  ]

def drawascii(level):
  maxx = max([x for x,_ in level.keys()])
  maxy = max([y for _,y in level.keys()])
  for y in range(maxy+1):
    line = ""
    for x in range(maxx+1):
      line += level[(x,y)]
    print(line)

def draw(g, spaces, doors, keys):
  pos = nx.get_node_attributes(g, 'pos')
  nx.draw_networkx_nodes(g, pos, node_size=20, nodelist=spaces, node_color='#00aaee', alpha=0.4)
  nx.draw_networkx_nodes(g, pos, node_size=100, nodelist=doors.values(), node_color='#ee0033')
  nx.draw_networkx_nodes(g, pos, node_size=100, nodelist=keys.values(), node_color='#33ee66')
  nx.draw_networkx_edges(g, pos)

  labels = nx.get_node_attributes(g,'label')
  nx.draw_networkx_labels(g, pos, labels=labels, font_size=11, alpha=0.4)
  
  labels = nx.get_edge_attributes(g,'weight')
  nx.draw_networkx_edge_labels(g, pos, font_size=7, edge_labels=labels)

  plt.show()

def createGameFrom(level, position):
  keepgoing = True
  curgraph = nx.Graph()
  curgraph.add_node(position, pos=position)
  visited = set()
  spaces = set()
  reachablekeys = dict()
  reachabledoors = dict()
  tovisit = set([position])
  nextvisits = set()
  while keepgoing:
    for p in tovisit:
      for n in neighbors(level, p):
        if n in visited or level[n] == "#":
          continue
        
        weight = 1
        while True:
          nextneighbors = neighbors(level, n)
          others = [x for x in nextneighbors if level[x] == "." and x != p and x not in visited]
          if len(others) != 1:
            break
          visited.add(n)
          n = others[0]
          weight += 1

        label = '' if level[n] == '.' else level[n]
        curgraph.add_node(n, pos=n, label=label)
        curgraph.add_edge(p, n, weight=weight)
        if level[n] == ".":
          nextvisits.add(n)
          visited.add(n)
          spaces.add(n)
        elif level[n].islower():
          print("Adding", level[n])
          nextvisits.add(n)
          visited.add(n)
          reachablekeys[level[n]] = n
        else:
          print("Adding2", level[n])
          nextvisits.add(n)
          visited.add(n)
          reachabledoors[level[n].lower()] = n

    keepgoing = len(nextvisits) > 0
    tovisit = nextvisits
    nextvisits = set()
  return curgraph, spaces, reachabledoors, reachablekeys

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

  curgraph, spaces, reachabledoors, reachablekeys = createGameFrom(level, position)
  print(reachablekeys.values())
  drawascii(level)
  draw(curgraph, spaces, reachabledoors, reachablekeys)

  return None

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

print("Part 1:", solve(raw))
