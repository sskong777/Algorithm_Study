
n =int(input())
sottuk = input()
count =0
for i in range(n//2):
    if sottuk[i] != sottuk[n-i-1]:
        count+=1
print(count)