def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    people = [0, 0, 0, 0]

    for idx, ans in enumerate(answers):
        for person, pattern in enumerate(patterns, start=1):
            if ans == pattern[idx % len(pattern)]:
                people[person] += 1
                break

    max_score = max(people)
    result = [person for person, score in enumerate(people) if score == max_score]

    return result