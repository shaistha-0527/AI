def dfs(state, goal, depth, path):
  if state == goal:
    return path
  if depth == 0:
    return None
  zero = state.index(0)
  moves = [-3, 3, -1, 1]
  for move in moves:
    new = zero + move
    if 0 <= new < 9:
      if move == -1 and zero % 3 == 0:
        continue
      if move == 1 and zero % 3 == 2:
        continue
      s = list(state)
      s[zero], s[new] = s[new], s[zero]
      s = tuple(s)
      if s not in path:
        result = dfs(s, goal, depth - 1, path + [s])
        if result:
          return result
  return None
def IDS(start, goal):
  depth = 0
  while True:
    result = dfs(start, goal, depth, [start])
    if result:
      return result
    depth += 1
start = (1, 2, 3,
0, 4, 6,
7, 5, 8)
goal = (1, 2, 3,
4, 5, 6,
7, 8, 0)
solution = IDS(start, goal)
for state in solution:
  print(state[:3])
  print(state[3:6])
  print(state[6:])
  print()