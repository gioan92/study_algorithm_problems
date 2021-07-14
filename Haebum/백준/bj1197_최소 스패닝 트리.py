import sys
# mst 크루스칼 풀이
# union-find를 이용하여 풀이
# 가중치를 기준으로 정렬하여 for문 돌면서 이어져있는지 확인

# 부모 찾기 함수
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

# 부모 연결 함수 (두개가 이어져 있다!)
def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    parent[x] = y

# m 정점의갯수 n 간선의 갯수
m,n = map(int,sys.stdin.readline().split())
parent = [i for i in range(m+1)]
lines = [0]*n
answer = 0
for j in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    lines[j] = line

lines.sort(key=lambda x:x[2])
for line in lines:
    if find(line[0]) == find(line[1]):
        pass
    else:
        union(line[0],line[1])
        answer += line[2]
