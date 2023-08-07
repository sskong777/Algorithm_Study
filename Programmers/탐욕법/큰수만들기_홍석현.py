# 정답 풀이 - stack 사용
def solution(number, k):
    answer = []

    for i in number:
        print(answer)
        # k만큼 제거 될때까지, stack에 있는 마지막 값보다 i가 더 크다면 그 값을 제거하고 i를 추가
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1

        answer.append(i)

    # 이 부분 처리를 안하면 통과 못함
    # 굳이 인덱스로 왜 잘라야하는지 모르겠다
    return ''.join(answer[:len(answer) - k])

# 테스트케이스 통과, 시간 초과
# from itertools import permutations,combinations
# def solution(number, k):
#     answer = ''
#     number_list = list(number)
#     permu_number_list = combinations(number_list,len(number)-k)
#     for i in permu_number_list:
#         num = ''.join(i)
#         answer = max(answer,num)
#     return answer




