def solution(operations):
    lst = []
    heap = []
    answer = []
    for operation in operations:
        lst.append(operation.split(' '))
    for op in lst:
        if op[0]=='I':
            heap.append(int(op[1]))
        if op[0]=='D' and op[1]=="1" and heap:
            heap.remove(max(heap))
        if op[0]=='D' and op[1]=="-1" and heap:
            heap.remove(min(heap))
    if heap:
        answer = [max(heap),min(heap)]
    else:
        answer = [0,0]
            
    return answer