import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    answer = []
    temp = []
    
    for op in operations:
        num = op.split(' ')
        if num[0] == "I":
            heapq.heappush(temp,int(num[1]))
            heapq.heappush(max_heap,(-int(num[1]),int(num[1])))
            heapq.heappush(min_heap,int(num[1]))
        else:
            if len(temp) == 0:
                pass
            elif num[1] == "1" and max_heap:
                max_num = heapq.heappop(max_heap)[1]
                min_heap.remove(max_num)
                temp.remove(max_num)
            elif num[1] == "-1" and min_heap:
                min_num = heapq.heappop(min_heap)
                max_heap.remove((-min_num,min_num))
                temp.remove(min_num)
                
    if len(temp) != 0:
        answer = [max_heap[0][1],min_heap[0]]
    else:
        answer = [0,0]
    
    return answer