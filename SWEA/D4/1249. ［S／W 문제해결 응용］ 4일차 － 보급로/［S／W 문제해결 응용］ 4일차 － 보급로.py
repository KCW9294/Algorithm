from collections import deque
T = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dij(queue):
	while queue:
		x,y = queue.popleft()
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]
			if 0<=nx<N and 0<=ny<N:
				if distance[nx][ny] > distance[x][y] + field[nx][ny]:
					distance[nx][ny] = distance[x][y] + field[nx][ny]
					queue.append((nx,ny))
	
for test_case in range(1, T + 1):
	N = int(input())
	field = [list(map(int, list(input()))) for _ in range(N)] 
	INF = float('inf')
	distance = [[ INF for _ in range(N)] for _ in range(N)]
	distance[0][0] = 0
	deq = deque()
	deq.append((0, 0))
	dij(deq)
	print('#{} {}'.format(test_case, distance[N-1][N-1]))
