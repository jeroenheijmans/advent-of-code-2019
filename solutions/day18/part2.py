import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

def createLevelFrom(data):
  x, y = 0, 0
  level = dict()
  for line in data:
    for c in line:
      if c == "@": position = (x,y)
      level[(x,y)] = '.' if c == "@" else c
      x += 1
    x = 0
    y += 1

  # Adjust for part 2:
  level[position] = "#"
  level[(position[0] - 1, position[1] + 0)] = "#"
  level[(position[0] + 1, position[1] + 0)] = "#"
  level[(position[0] + 0, position[1] + 1)] = "#"
  level[(position[0] + 0, position[1] - 1)] = "#"

  positions = (
    (position[0] - 1, position[1] - 1),
    (position[0] - 1, position[1] + 1),
    (position[0] + 1, position[1] - 1),
    (position[0] + 1, position[1] + 1),
  )
  
  return level, positions

def neighbors(level, p):
  return [x for x in [
    (p[0] + 1, p[1]),
    (p[0] - 1, p[1]),
    (p[0], p[1] + 1),
    (p[0], p[1] - 1),
  ] if x in level and level[x] != "#"]

def draw(g, spaces, doors, keys, positions):
  pos = nx.get_node_attributes(g, 'pos')
  
  nx.draw_networkx_nodes(g, pos, node_size=200, nodelist=positions, node_color='#eeee00', alpha=0.9)
  nx.draw_networkx_nodes(g, pos, node_size=30, nodelist=spaces, node_color='#00aaee', alpha=0.8)
  nx.draw_networkx_nodes(g, pos, node_size=150, nodelist=doors.values(), node_color='#ee0033', alpha=0.8)
  nx.draw_networkx_nodes(g, pos, node_size=150, nodelist=keys.values(), node_color='#33ee66', alpha=0.8)
  
  nx.draw_networkx_edges(g, pos, alpha=0.6)

  labels = nx.get_node_attributes(g,'label')
  nx.draw_networkx_labels(g, pos, labels=labels, font_size=11, alpha=0.4)
  
  labels = nx.get_edge_attributes(g,'weight')
  nx.draw_networkx_edge_labels(g, pos, font_size=7, edge_labels=labels)

  plt.show()

def createGameFrom(level, positions) -> (nx.Graph, set(), dict(), dict()):
  spaces = set()
  keys = dict()
  doors = dict()
  
  curgraph = nx.Graph()

  for p in level:
    if level[p] == "#": continue
    if level[p] == ".": spaces.add(p)
    if level[p].isupper(): doors[level[p].lower()] = p
    if level[p].islower(): keys[level[p]] = p
    label = "" if level[p] == "." else level[p]
    curgraph.add_node(p, pos=(p[0], -p[1]), label=label)
  
  for p in level:
    for n in neighbors(level, p):
      if n in curgraph.nodes() and p in curgraph.nodes():
        curgraph.add_edge(p, n, weight=1)

  # Remove leaves, both spaces and dead-end doors:
  keepgoing = True
  while keepgoing:
    keepgoing = False
    leaves = [
      x for x in curgraph.nodes()
      if x not in positions and len(list(curgraph.neighbors(x))) == 1
    ]
    for leaf in leaves:
      if level[leaf] == "." or level[leaf].isupper():
        keepgoing = True
        curgraph.remove_node(leaf)
        if level[leaf] == ".": spaces.remove(leaf) 
        else: del doors[level[leaf].lower()]

  # Another round of condensing hallways:
  keepgoing = True
  while keepgoing:
    keepgoing = False
    potentials = [x for x in curgraph.nodes() if len(list(curgraph.neighbors(x))) == 2]
    for pot in potentials:
      others = list(curgraph.neighbors(pot))
      if pot in spaces and len(others) == 2 and pot not in positions:
        weight = curgraph.edges[others[0], pot]['weight'] + curgraph.edges[others[1], pot]['weight']
        curgraph.remove_node(pot)
        spaces.remove(pot)
        curgraph.add_edge(others[0], others[1], weight=weight)

  return curgraph, spaces, doors, keys

def solve(data):
  level, positions = createLevelFrom(data)
  curgraph, spaces, doors, keys = createGameFrom(level, positions)
  # draw(curgraph, spaces, doors, keys, positions)

  allkeys = frozenset(keys.keys())
  alldoors = frozenset(doors.keys())
  states = { (positions, frozenset()): 0 }

  midx = min([x for x,_ in positions]) + 1
  midy = min([y for _,y in positions]) + 1
  
  while True:
    newstates = dict()

    print(f"Recursing. First state with nr of keys: {len(next(iter(states))[1])}")

    for state in states:
      neededKeys = allkeys - state[1]
      closeddoors = alldoors - set([x for x in state[1]])
      closeddoorspoints = set([doors[k] for k in closeddoors])

      for target in [keys[k] for k in keys if k in neededKeys]:
        if target[0] < midx and target[1] < midy: boti = 0
        elif target[0] < midx and target[1] > midy: boti = 1
        elif target[0] > midx and target[1] < midy: boti = 2
        elif target[0] > midx and target[1] > midy: boti = 3

        weight, path = nx.single_source_dijkstra(curgraph, state[0][boti], target, weight="weight")

        if set(path) & closeddoorspoints: continue

        newcost = states[state] + weight
        if boti == 0: newpos = (path[-1], state[0][1], state[0][2], state[0][3])
        elif boti == 1: newpos = (state[0][0], path[-1], state[0][2], state[0][3])
        elif boti == 2: newpos = (state[0][0], state[0][1], path[-1], state[0][3])
        elif boti == 3: newpos = (state[0][0], state[0][1], state[0][2], path[-1])
        newkeys = frozenset(state[1] | { level[path[-1]] })
        newstate = (newpos, newkeys)
        newstates[newstate] = min(newcost, newstates[newstate]) if newstate in newstates else newcost

    states = newstates

    done = False
    for state in [s for s in states if s[1] == allkeys]:
      done = True
    if done: break

  return min(states.values())

def solveFromFile(file):
  with open(file, 'r') as file:
    return solve(file.read().splitlines())

print("Part 2:", solveFromFile("input.txt"))
