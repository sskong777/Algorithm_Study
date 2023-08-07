# def solution(name):
#     answer = 0

#     alphabets = [chr(x) for x in range(ord('A'), ord('Z')+1)]
#     for i in range(len(name)):
#         index = 0

#         # print(alphabets.index(name[i]))
#         if abs(alphabets.index(name[i]) - index) <= len(alphabets)//2:
#             answer += abs(alphabets.index(name[i]) - index)
#             index = alphabets.index(name[i])
#         else:
#             answer += len(alphabets) - abs(alphabets.index(name[i]) - index)
#             index = alphabets.index(name[i])

#         # 문자가 A이면 왼쪽
#         if index != 0 and i != len(name)-1:
#             answer += 1

#         # print(answer)

#     return answer


def solution(name):
    # 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer