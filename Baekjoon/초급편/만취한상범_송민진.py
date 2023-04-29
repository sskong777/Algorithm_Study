tc = int(input())

def change_status(arr, idx):
    if arr[idx] == False:
        arr[idx] = True
    else:
        arr[idx] = False

for _ in range(tc):
    n = int(input())
    rooms = [False] * n

    for tmp in range(n):
        for i in range(n):
            if (i+1) % (tmp+1) == 0:
                change_status(rooms, i)
    print(rooms.count(True))

