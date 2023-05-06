n = int(input())

for i in range(n):
    sentence = list(input().split())
    sentence.reverse()
    case = ' '.join(map(str, sentence))

    print(f"Case #{i+1}: {case}")