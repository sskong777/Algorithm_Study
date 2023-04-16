N = int(input())

arr = list()
for i in range(1, N+1):
    arr += str(i)

string = ''.join(arr)

print(string.index(str(N))+1)

