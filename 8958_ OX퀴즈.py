'''
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''

T = int(input())
for t in range(T):
    str = input()
    ans = 0
    temp = 0
    for i in str:
        if i == 'O':
            temp += 1
            ans += temp
        elif i =='X':
            temp = 0
    print(ans)