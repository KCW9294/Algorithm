def solution(sizes):
    find_min = []
    find_max = []
    for i in range(len(sizes)):
        find_min.append(min(sizes[i]))
        find_max.append(max(sizes[i]))
    return max(find_min)*max(find_max)