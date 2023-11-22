def count_rooms(n, m, map):
  rooms = []

  for i in range(n):
    for j in range(m):
      if map and 0 <= i < len(map) and 0 <= j < len(map[0]) and map[i][j] == '.':
        explore(i, j, rooms, map)

  return len(rooms)

def explore(i, j, rooms, map):
  if (i, j) not in rooms:
    rooms.append((i, j))

    for di in [-1, 0, 1]:
      for dj in [-1, 0, 1]:
        next_i = i + di
        next_j = j + dj
        if 0 <= next_i < n and 0 <= next_j < m and map[next_i][next_j] == '.':
          explore(next_i, next_j, rooms, map)


n = 5
m = 8
map = [
  ["#", "#", "#", "#", "#", "#"],
  ["#", ".", ".", "#", ".", "#"],
  ["#", "", "#", ".", ".", "#"],
  ["#", ".", ".", ".", ".", "#"],
  ["#", "#", "#", "#", "#", "#"]
]

print(count_rooms(n, m, map))
