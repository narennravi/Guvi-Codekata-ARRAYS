# Question:-
'''
Vishal is learning to skate on ice. He's a beginner, so his only mode of transportation is pushing off from a snow drift to the north, east, south or west and sliding until he lands in another snow drift.
He has noticed that in this way it's impossible to get from some snow drifts to some other by any sequence of moves. He now wants to heap up some additional snow drifts, so that he can get from any snow drift to any other one.
He asked you to find the minimal number of snow drifts that need to be created. We assume that Vishal can only heap up snow drifts at integer coordinates. The first line of input contains a single integer N the number of snow drifts.
Each of the following n lines contains two integers xi and yi the coordinates of the i-th snow drift. Note that the north direction coinсides with the direction of Oy axis, so the east direction coinсides with the direction of the Ox axis.
All snow drift's locations are distinct.
Input Size : 1 <= N,Xi,Yi <= 1000


Sample Testcase :
INPUT
2
2 1
1 2

OUTPUT
1
'''



# Solution:-
def dfs(node, graph, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)

def find_min_additional_snow_drifts(n, snow_drifts):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        x1, y1 = snow_drifts[i]
        for j in range(i + 1, n):
            x2, y2 = snow_drifts[j]
            if x1 == x2 or y1 == y2:
                graph[i].append(j)
                graph[j].append(i)

    visited = [False] * n
    connected_components = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, graph, visited)
            connected_components += 1

    return connected_components - 1

if __name__ == "__main__":
    n = int(input())
    snow_drifts = [tuple(map(int, input().split())) for _ in range(n)]

    min_additional_snow_drifts = find_min_additional_snow_drifts(n, snow_drifts)
    print(min_additional_snow_drifts)
