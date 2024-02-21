nums = [int(i) for i in input().split()]
nums.sort()
visited = set()
dup = {x for x in nums if x in visited or (visited.add(x) or False)}
print(*dup)


a, c = [str(i) for i in input().split()], []
for i in a:
    if i not in c and a.count(i) > 1:
        c.append(i)
        print(i, end=' ')
