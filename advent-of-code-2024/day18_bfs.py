from advent import parse, ints, heappop, heappush

blocks = { (x,y) for x, y in parse(18, ints)[:1024] }

def part1(goal):
    pq      = []
    visited = set()
    heappush(pq, (0, (0,0)))

    while pq:
        length, pos = heappop(pq)

        if pos == goal:
            return length
        elif pos in visited:
            continue

        visited.add(pos)
        x, y = pos

        for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
            nxt = (nx, ny) = x + dx, y + dy

            if 0 <= nx <= goal[0] and 0 <= ny <= goal[1] and nxt not in visited and nxt not in blocks:
                heappush(pq, (length + 1, nxt))

# ---------------------------------------------------------------------------------------------

assert part1((70,70)) == 344
