from itertools import combinations
T = int(input())

for test_case in range(1, T + 1):
	N = int(input())
	lst = list(map(int,input().split()))
	answer = [0]
	visited = [1]+[0]*sum(lst)
	for i in lst:
		for j in range(len(answer)):
			if visited[i+answer[j]] == 0:
				visited[i+answer[j]]=1
				answer.append(i+answer[j])

	print("#{} {}".format(test_case, len(answer)))
