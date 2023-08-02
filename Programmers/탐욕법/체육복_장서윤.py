import collections


def solution(n, lost, reserve):

    # 체육복을 도난 당한 학생이 여분을 가지고 있는 경우 리스트에서 제거함
    losts = list(collections.Counter(lost) - collections.Counter(reserve))
    reserves = list(collections.Counter(reserve) - collections.Counter(lost))

    answer = n - len(losts)

    losts.sort()
    reserves.sort()

    for l in losts:
        for r in reserves:
            if abs(l - r) == 1: # 여분을 가진 학생이 도난 당한 학생의 앞 뒤에 있는지 확인
                answer += 1
                reserves.remove(r) # 빌려준 학생은 빼줌
                break

    return answer

