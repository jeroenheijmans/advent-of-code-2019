import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

def createLevelFrom(data):
  x, y = 0, 0
  level = defaultdict(lambda: '#')
  for line in data:
    for c in line:
      if c == "@": position = (x,y)
      level[(x,y)] = '.' if c == "@" else c
      x += 1
    x = 0
    y += 1
  
  return level, position

def neighbors(level, p):
  return [x for x in [
    (p[0] + 1, p[1]),
    (p[0] - 1, p[1]),
    (p[0], p[1] + 1),
    (p[0], p[1] - 1),
  ] if level[x] != "#"]

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

def createGameFrom(level, position) -> (nx.Graph, set(), dict(), dict()):
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

        weight = 1
        if level[n] in ["."]:
          # Try to condense hallways:
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

  # Remove leaves, both spaces and dead-end doors:
  keepgoing = True
  while keepgoing:
    keepgoing = False
    leaves = [
      x for x in curgraph.nodes()
      if x != position and len(list(curgraph.neighbors(x))) == 1
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
      if pot in spaces and len(others) == 2:
        weight = curgraph.edges[others[0], pot]['weight'] + curgraph.edges[others[1], pot]['weight']
        curgraph.remove_node(pot)
        spaces.remove(pot)
        curgraph.add_edge(others[0], others[1], weight=weight)

  return curgraph, spaces, doors, keys

def solve(data):
  level, position = createLevelFrom(data)
  curgraph, spaces, doors, keys = createGameFrom(level, position)
  # draw(curgraph, spaces, doors, keys, position)

  allkeys = frozenset(keys.keys())
  alldoors = frozenset(doors.keys())
  states = { (position, frozenset()): 0 }
  
  while True:
    newstates = dict()

    print(f"Recursing. First state: {next(iter(states))}")

    for state in states:
      neededKeys = allkeys - state[1]
      closeddoors = alldoors - set([x for x in state[1]])
      closeddoorspoints = set([doors[k] for k in closeddoors])
      targets = [keys[k] for k in keys if k in neededKeys]
      paths = [
        nx.single_source_dijkstra(curgraph, state[0], t, weight=lambda u, v, d: d["weight"]) # TODO: Improve speed by filtering closed doors here?
        for t in targets
      ]
      paths = [
        p for p in paths
        if not set(p[1]) & closeddoorspoints
      ]
      # Show all reachable keys and their costs and their paths:
      for weight,path in paths:
        newcost = states[state] + weight
        newpos = path[-1]
        newkeys = frozenset(state[1] | { level[newpos] })
        newstate = (newpos, newkeys)
        newstates[newstate] = min(newcost, newstates[newstate]) if newstate in newstates else newcost

    states = newstates

    done = False
    for state in [s for s in states if s[1] == allkeys]:
      print(f"Found cost {states[state]} at {state[0]} keys {''.join(sorted(state[1]))}")
      done = True
    if done: break

  return min(states.values())

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

# Not 7071 - too high :'(
# Not 5014 -- too high still
# Not 4906 -- too high yet again
# Not 4674
# Not 3976
# Not 4208
# Not 3984 -- now have to wait 10 minutes after guessing incorrectly 7 times...
# Not 3914 (manual guess) - lockout of 10 minutes again
# Not 3876 - lockout 10 mins at 15:36 local time :P this answer even came from the algorithm
# Not 3868 after tweaking the level hoping it doesn't make a weird connection...
print("Part 1:", solve(raw))
