n, k = map(int, input().split())

numbers = [num for num in range(2, n+1)]
tmp_numbers = []
primes = []
erase_cnt = 0


while numbers:
    checking = numbers.pop(0)
    erase_cnt += 1
    if erase_cnt == k:
        print(checking)
        break
    primes.append(checking)

    if not numbers:
        break

    for num in numbers:
        if num % checking != 0:
            tmp_numbers.append(num)
        else:
            erase_cnt += 1
            if erase_cnt == k:
                print(num)
                numbers = []
                break
    numbers = tmp_numbers
    tmp_numbers = []