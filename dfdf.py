a=int(input())

for i in range(a):
    for j in reversed(range(a)):
        if i<j:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(a):
        if i > j :
            print('*', end='')
        else :
            print(' ', end='')
    print()