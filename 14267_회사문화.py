import sys
input = sys.stdin.readline


def dp():
    N, M = map(int,input().split())
    lst = [0] + list(map(int,input().split()))
    result = [0] * (N+1)
    for _ in range(M):
        a,b = map(int,input().split())
        result[a] += b

    for i in range(2,N+1):
        result[i] += result[lst[i]]
        
    print(*result[1:])

dp()
