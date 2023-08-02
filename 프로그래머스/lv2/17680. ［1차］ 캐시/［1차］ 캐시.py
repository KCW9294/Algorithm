def solution(cacheSize, cities):
    cache = []
    answer = 0
    for city in cities:
        if city.lower() not in cache:
            answer += 5
            if len(cache) == cacheSize:
                if cacheSize != 0:
                    cache.pop(0)
                    cache.append(city.lower())
                else:
                    continue
            else:
                cache.append(city.lower())
                
        else:
            answer += 1
            cache.remove(city.lower())
            cache.append(city.lower())
        

    return answer