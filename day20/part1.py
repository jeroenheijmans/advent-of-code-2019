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
  pos = nx.get_node_attributes(g, 'pos')

  nx.draw_networkx_nodes(g, pos, nodelist=spaces, node_size=100, node_color='#eeee00', alpha=0.9)
  nx.draw_networkx_nodes(g, pos, nodelist=portals, node_size=100, node_color='#ee0000', alpha=0.9)

  nx.draw_networkx_edges(g, pos, alpha=0.6)
  labels = nx.get_node_attributes(g,'label')
  nx.draw_networkx_labels(g, pos, labels=labels, font_size=11, alpha=0.4)
  labels = nx.get_edge_attributes(g,'weight')
  nx.draw_networkx_edge_labels(g, pos, font_size=7, edge_labels=labels)
  plt.show()

def solve(data):
  curgraph, portals, spaces, start, finish = createGameFrom(data)
  draw(curgraph, portals, spaces, start, finish)

  path = nx.single_source_dijkstra(curgraph, start, finish, weight='weight')
  pathweight = path[0] # path[1] is list of point-tuples in order

  return pathweight

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

print("Part 1:", solve(raw))