def tower_of_hanoi(n, S:list, D:list, B:list):
    if n>0:
        tower_of_hanoi(n-1, S, B, D)
        D.append(S.pop())
        tower_of_hanoi(n-1, B, D, S)



S = [1,2,3]
D = []
B = []

tower_of_hanoi(len(S), S, B, D)
