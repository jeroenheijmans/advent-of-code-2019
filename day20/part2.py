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

def neighborsLetters(level, p):
  return [n for n in neighbors(level, p) if level[n].isupper()]

def createGameFrom(data):
  curgraph = nx.Graph()
  level = defaultdict(lambda: ' ')
  portaldict = dict()
  portals = set()
  spaces = set()
  x,y = 0,0

  for line in data:
    for c in line:
      level[(x,y)] = c
      x += 1
    y += 1
    x =0
  
  for p in level:
    label = ''

    if level[p] == ".":
      label = ""
      spaces.add(p)
      curgraph.add_node(p, pos=(p[0], -p[1]), label=label)

      for n in neighbors(level, p):
        if level[n] == ".":
          curgraph.add_edge(p, n, weight=1)
        
        if level[n].isupper():
          otherletter = neighborsLetters(level, n)[0]
          key = "".join(sorted([level[n] + level[otherletter]]))
          key = "".join(sorted(key)) # WHATT?! Why is this needed?
          portals.add(n)
          curgraph.add_node(n, pos=(n[0], -n[1]), label=key)
          curgraph.add_edge(p, n, weight=0)
          portaldict[n] = key
  
  for p1 in portaldict:
    if portaldict[p1] == "AA":
      start = p1
      continue
    if portaldict[p1] == "ZZ":
      finish = p1
      continue
    
    others = [x for x in portaldict if x != p1 and portaldict[x] == portaldict[p1]]
    p2 = others[0]
    curgraph.add_edge(p1, p2, weight=1)

  # Remove leaves without doors and keys:
  keepgoing = True
  while keepgoing:
    keepgoing = False
    leaves = [x for x in curgraph.nodes() if len(list(curgraph.neighbors(x))) == 1]
    for leaf in leaves:
      if level[leaf] == ".":
        keepgoing = True
        curgraph.remove_node(leaf)
        spaces.remove(leaf)

  # Condensing hallways:
  keepgoing = True
  while keepgoing:
    keepgoing = False
    potentials = [x for x in curgraph.nodes() if len(list(curgraph.neighbors(x))) == 2]
    for pot in potentials:
      others = list(curgraph.neighbors(pot))
      if pot in spaces and len(others) == 2 and len(set(others) & portals) == 0:
        weight = curgraph.edges[others[0], pot]['weight'] + curgraph.edges[others[1], pot]['weight']
        curgraph.remove_node(pot)
        spaces.remove(pot)
        keepgoing = True
        curgraph.add_edge(others[0], others[1], weight=weight)

  return curgraph, portals, spaces, start, finish

def draw(g, portals, spaces, start, finish):
  # Nodes
  pos = nx.get_node_attributes(g, 'pos')
  factor = max([p[0] for p in pos if p[2] == 0]) + 10
  for k in pos:
    offset = pos[k][2] * factor
    pos[k] = (pos[k][0] + offset, pos[k][1])
  
  labels = nx.get_node_attributes(g,'label')
  nx.draw_networkx_nodes(g, pos, nodelist=spaces, node_size=10, node_color='#33ee33', alpha=0.9)
  nx.draw_networkx_nodes(g, pos, nodelist=portals, node_size=30, node_color='#ee3333', alpha=0.9)
  nx.draw_networkx_labels(g, pos, labels=labels, font_size=11, alpha=0.9)

  # Edges
  labels = nx.get_edge_attributes(g,'weight')
  nx.draw_networkx_edges(g, pos, alpha=0.6)
  nx.draw_networkx_edge_labels(g, pos, font_size=7, edge_labels=labels)

  plt.show()

def solve(data):
  curgraph, portals, spaces, start, finish = createGameFrom(data)

  digraph = nx.DiGraph()

  minx = min([p[0] for p in portals])
  miny = min([p[1] for p in portals])
  maxx = max([p[0] for p in portals])
  maxy = max([p[1] for p in portals])

  def isOuter(n):
    return n[0] == minx or n[0] == maxx or n[1] == miny or n[1] == maxy

  def isInner(n):
    return not isOuter(n) and n not in spaces

  recdepth = 40
  
  for z in range(recdepth):
    for pair in curgraph.edges():
      weight = curgraph.edges[pair]["weight"]
      a = pair[0]
      b = pair[1]
      labela = curgraph.nodes[a]["label"]
      labelb = curgraph.nodes[b]["label"]

      if a in spaces or b in spaces:
        c1 = (a[0], a[1], z)
        c2 = (b[0], b[1], z)
        digraph.add_node(c1, pos=(c1[0], -c1[1], z), label=labela)
        digraph.add_node(c2, pos=(c2[0], -c2[1], z), label=labelb)
        digraph.add_edge(c1, c2, weight=weight)
        digraph.add_edge(c2, c1, weight=weight)
      elif (isInner(a) and isOuter(b)) or (isInner(b) and isOuter(a)):
        inner = (a[0], a[1], z) if isInner(a) else (b[0], b[1], z)
        outer = (a[0], a[1], z+1) if isOuter(a) else (b[0], b[1], z+1)

        digraph.add_node(inner, pos=(inner[0], -inner[1], inner[2]), label=curgraph.nodes[(inner[0], inner[1])]["label"])
        digraph.add_node(outer, pos=(outer[0], -outer[1], outer[2]), label=curgraph.nodes[(outer[0], outer[1])]["label"])
        digraph.add_edge(inner, outer, weight=weight)
        digraph.add_edge(outer, inner, weight=weight)
  
  spaces2 = set()
  portals2 = set()
  for n in [p for p in digraph.nodes()]:
    if (n[0], n[1]) in spaces: spaces2.add(n)
    if (n[0], n[1]) in portals: portals2.add(n)

  start = (start[0], start[1], 0)
  finish = (finish[0], finish[1], 0)

  # draw(digraph, portals2, spaces2, start, finish)

  print("Searching for path from", start, "to", finish)
  result = nx.dijkstra_path_length(digraph, start, finish, weight='weight')

  return result

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

print("Part 2:", solve(raw))