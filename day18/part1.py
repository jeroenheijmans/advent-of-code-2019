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
  for y in range(maxy):
    line = ""
    for x in range(maxx):
      line += level[(x,y)]
    print(line)

def draw(g, spaces, doors, keys):
  pos=nx.spring_layout(g)
  nx.draw_networkx_nodes(g,pos,nodelist=spaces,node_color='#00aaee')
  nx.draw_networkx_nodes(g,pos,nodelist=doors.values(),node_color='#ee0033')
  nx.draw_networkx_nodes(g,pos,nodelist=keys.values(),node_color='#33ee66')
  nx.draw_networkx_edges(g,pos)
  nx.draw_networkx_labels(g, pos)
  plt.show()

def createGameFrom(level, position):
  keepgoing = True
  curgraph = nx.Graph()
  curgraph.add_node(position)
  visited = set()
  reachablekeys = dict()
  reachabledoors = dict()
  tovisit = set([position])
  nextvisits = set()
  while keepgoing:
    for p in tovisit:
      for n in neighbors(level, p):
        if n in visited or level[n] == "#":
          continue
        
        # TODO: for non-intersection-points, continue building a weighted graph

        curgraph.add_node(n)
        curgraph.add_edge(p, n)
        if level[n] == ".":
          nextvisits.add(n)
          visited.add(n)
        elif level[n].islower():
          nextvisits.add(n)
          visited.add(n)
          reachablekeys[level[n]] = n
        else:
          reachabledoors[level[n].lower()] = n

    keepgoing = len(nextvisits) > 0
    tovisit = nextvisits
    nextvisits = set()
  return curgraph, visited, reachabledoors, reachablekeys

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

  # drawascii(level)

  curgraph, visited, reachabledoors, reachablekeys = createGameFrom(level, position)

  # closestdist = 100000
  # closestletter = None
  # for letter in set(reachabledoors.keys()) & set(reachablekeys.keyu()):
  #   door = reachabledoors[letter]
  #   key = reachablekeys[letter]
  #   keydist = nx.shortest_path_length(curgraph, position, key)
  #   doordist = nx.shortest_path_length(curgraph, key, door)
  #   totaldist = keydist + doordist

  # Need to condense "visited" first, use a dist instead of single steps
  # draw(curgraph, visited, reachabledoors, reachablekeys)

  return None

with open('input.txt', 'r') as file:
  raw = file.read().splitlines()

print("Part 1:", solve(raw))
