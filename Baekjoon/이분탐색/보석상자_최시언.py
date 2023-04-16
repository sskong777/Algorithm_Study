def distribute_jewelry(jewelry, num_students):
    counts = {}
    for j in jewelry:
        if j in counts:
            counts[j] += 1
        else:
            counts[j] = 1
    
    max_count = (len(jewelry) // num_students)
    extra = len(jewelry) % num_students
    for j in counts:
        counts[j] //= max_count
        extra -= counts[j] % num_students
    
    j_list = list(counts.keys())
    j_list.sort()
    i = 0
    while extra > 0:
        counts[j_list[i]] += 1
        i = (i + 1) % len(j_list)
        extra -= 1
    
    result = 0
    for j in counts:
        result = max(result, counts[j])
    return result
