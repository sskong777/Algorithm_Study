# [1620] 나는야 포켓몬 마스터 이다솜
"""
enumerate()을 사용하면 리스트로 받는데 for문을 돌다 보니까 시간초과 
그래서 반복문 안돌면서 값 체킹하려면 ->  dictionary를 사용해야 된다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_to_word = {}
word_to_num = {}

for i in range(1, N+1):
    word = input().strip()
    # dictionary를 만드는 과정 (key:value)
    num_to_word[i] = word
    word_to_num[word] = i


for _ in range(M):
    word = input().strip()
    if word.isdigit():  # 숫자라면,
        print(num_to_word[int(word)])  # 그 숫자에 해당하는 포켓몬의 이름을 출력
    else:  # 포켓몬의 이름이라면,
        print(word_to_num[word])  # 이름에 해당하는 숫자를 출력
