nanjeng_list = []
for _ in range(9):
    nanjeng_list.append(int(input()))


def main():
    for i, j in enumerate(nanjeng_list):
        for k, l in enumerate(nanjeng_list):
            if i != k:
                total = sum(nanjeng_list)
                total -= (j + l)
                if total == 100:
                    nanjeng_list.remove(j)
                    nanjeng_list.remove(l)
                    nanjeng_list.sort()
                    return nanjeng_list


answer_list = main()

for i in answer_list:
    print(i)
