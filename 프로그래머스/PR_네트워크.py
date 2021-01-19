def solution(n, computers):
    answer = 0
    bfs = []
    visited = [0 for x in range(n)]
		
	#방문 안 한 노드가 없을 때까지 실행
    while 0 in visited:
        x = visited.index(0)
        bfs.append(x)
        visited[x] = 1
        
		#큐 가장 앞 부분 원소 pop 한다음 연결 노드들 push
        while bfs:
            node = bfs.pop(0)
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    visited[i] = 1
        answer += 1
    return answer