def solution(array, commands):
    result = []
    for cut in commands:
        cut_array = array[cut[0]-1:cut[1]]
        cut_array.sort()
        result.append(cut_array[cut[2]-1])
    return result