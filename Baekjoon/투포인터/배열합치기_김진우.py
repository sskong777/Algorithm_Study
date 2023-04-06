n , m = map(int, input().split())
li_a = list(map(int,input().split()))
li_b = list(map(int,input().split()))

# print(n,m,li_a,li_b)
li_sum = []
for i in li_a:
    li_sum.append(i)


for i in li_b:
    li_sum.append(i)

print(*sorted(li_sum))