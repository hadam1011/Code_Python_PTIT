import itertools

from itertools import permutations
for i in range(int(input())):
    n = int(input())
    string = ""
    for j in range(1,n+1):
        string += str(j)
    string = list(permutations(string))[::-1]
    print(len(string))
    for value in string:
        print("".join(value),end=" ")
    print()