N, M = map(int, input().split())
 
from collections import defaultdict
m = defaultdict(dict)
 
for i in range(M):
    u, v, k = map(int, input().split())
    m[u][v] = k
    m[v][u] = k
 
keys = set([1]) 
queue = [1] 
 
key_room = defaultdict(list)
 
while queue:
    cur_room = queue.pop()
    if cur_room in key_room:
        for t in key_room[cur_room]:
            if t in keys:
                continue
            queue.append(t)
            keys.add(t)
        key_room.pop(cur_room)
    for next_room in m[cur_room]:
        if next_room in keys:
            continue
        key = m[cur_room][next_room]
        if key in keys:
            keys.add(next_room)
            queue.append(next_room)
        else:
            key_room[key].append(next_room)
 
print(len(keys))