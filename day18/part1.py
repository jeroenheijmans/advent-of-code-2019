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
  visited = set([position])
  tovisit = set([position])
  nextvisits = set()
  spaces = set()
  keys = dict()
  doors = dict()
  
  # Start by marking the starting position:
  curgraph = nx.Graph()
  curgraph.add_node(position, label="@", pos=(position[0], -position[1]))

  while keepgoing:
    for p in tovisit:
      for n in neighbors(level, p):
        if n in visited or level[n] in ["#", "@"]:
          continue

        if level[n] in ["."]:
          # Try to condense hallways:
          weight = 1
          while True:
            nextneighbors = neighbors(level, n)
            others = [x for x in nextneighbors if x != p and x != n and x not in visited]
            if len(others) != 1 or level[others[0]] != ".": break
            visited.add(n)
            n = others[0]
            weight += 1
          # Add empty space:
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

        label = '' if level[n] == '.' else level[n]
        curgraph.add_node(n, pos=(n[0], -n[1]), label=label)
        curgraph.add_edge(p, n, weight=weight)

    keepgoing = len(nextvisits) > 0
    tovisit = nextvisits
    nextvisits = set()

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
  
  # Another round of condensing hallways:
  keepgoing = True
  while keepgoing:
    keepgoing = False
    potentials = [x for x in curgraph.nodes() if len(list(curgraph.neighbors(x))) == 2]
    for pot in potentials:
      others = list(curgraph.neighbors(pot))
      if pot in spaces and len(others) == 2:
        weight = curgraph.edges[others[0], pot]['weight'] + curgraph.edges[others[1], pot]['weight']
        curgraph.remove_node(pot)
        spaces.remove(pot)
        curgraph.add_edge(others[0], others[1], weight=weight)

  return curgraph, spaces, doors, keys

def recursePath(level, graph: nx.Graph, allkeys, mykeys, position, origin):
  # print("Recursing on", "".join(mykeys), "vs", "".join(sorted(allkeys)))
  newkeys = mykeys.copy()
  if level[position].islower():
    newkeys.add(level[position])
  elif position == origin:
    print("Starting recursion from @ at hardcoded input position", position)
  else:
    raise ValueError(f"Unexpected recursion at {position} char {level[position]}")
  
  # Recursion ends when we have all keys:
  if allkeys == newkeys:
    # print("Ending recursion with allkeys!")
    return 0
  
  # Find reachable, needed keys:
  reachableNeededKeys = set()
  visited = set([position])
  tovisit = set([position])
  nextvisits = set()
  keepgoing = True
  while keepgoing:
    keepgoing = False
    for p in tovisit:
      others = graph.neighbors(p)
      for other in others:
        if other in visited:
          continue
        visited.add(other)
        if level[other] == ".":
          nextvisits.add(other) # open space means just searching on
        elif level[other].isupper():
          if level[other].lower() in newkeys:
            nextvisits.add(other) # we have a key for this door!
        elif level[other].islower():
          if level[other] not in newkeys:
            path = nx.single_source_dijkstra(graph, position, other, weight='weight')
            pathweight = path[0] # path[1] is list of point-tuples in order
            reachableNeededKeys.add((other, pathweight)) # found a new key! recurse on this
          else:
            nextvisits.add(other) # key already owned
        else:
          raise ValueError("Can't continue at", p)
    
    keepgoing = len(tovisit) > 0
    tovisit = nextvisits
    nextvisits = set()

  paths = []
  sortedtargets = sorted(reachableNeededKeys, key=lambda x: x[1])
  minweight = sortedtargets[0][1]
  for k, pathweight in sortedtargets:
    if pathweight > minweight + 50:
      break
    if position == origin:
      print("Pathing from", position, "to", k, "for key", level[k], "while having keys", "".join(sorted(newkeys)))
    innerresult = recursePath(level, graph, allkeys, newkeys, k, origin)
    newweight = innerresult + pathweight
    paths.append(newweight)

  return min(paths)

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

  origin = position
  curgraph, spaces, doors, keys = createGameFrom(level, position)

  allkeys = set(keys.keys())
  mykeys = set()
  
  # draw(curgraph, spaces, doors, keys, position)

  return recursePath(level, curgraph, allkeys, mykeys, position, origin)

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

# Not 7071 - too high :'(
# Not 5014 -- too high still
# Not 4906 -- too high yet again
print("Part 1:", solve(raw))
