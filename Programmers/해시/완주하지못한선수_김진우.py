'''def solution(participant, completion):
    for i in completion:

        if i in participant:
            print(i)
            participant.remove(i)
            print(f' par: {participant}')

    answer = participant
    print(answer)
    return answer
'''
participant = ["leo", "kiki", "eden"]

completion = ["eden", "kiki"]



def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant)
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]

solution(participant,completion)