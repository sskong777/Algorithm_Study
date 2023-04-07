# [1484] 다이어트

# end**2 - start**2 = g
# 현재 - 과거
g = int(input())

# start < end
start, end = 1, 2
check = True


while start < end:
    diff = end**2 - start**2
    if diff < g:
        end += 1
    elif diff > g:
        start += 1
    else:
        print(end)
        end += 1
        check = False

if check == True:
    print(-1)
