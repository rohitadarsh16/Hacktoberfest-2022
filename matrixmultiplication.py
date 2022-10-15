MAX = 100
r = int(input())
c = int(input())
mat = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    mat.append(a)

r1 = int(input())
c1 = int(input())
mat1 = []
for i in range(r1):
    a1 = []
    for j in range(c1):
        a1.append(int(input()))
    mat1.append(a1)

result = [[0 for i in range(MAX)]for j in range(MAX)]
for i in range(r):
    for j in range(c1):
        result[i][j] = 0
        for k in range(r1):
            result[i][j] += mat[i][k]*mat1[k][j]

for i in range(r):
    for j in range(c1):
        print(result[i][j],end = " ")
    print()
