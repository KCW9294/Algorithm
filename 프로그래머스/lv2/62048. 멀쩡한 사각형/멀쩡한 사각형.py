def solution(w,h):
    max = 0
    if w>=h:
        for i in range(1,h+1):
            if w%i==0 and h%i==0:
                if i>max:
                    max = i
    else:
        for i in range(1,w+1):
            if w%i==0 and h%i==0:
                if i>max:
                    max = i
    return w*h - (w+h-max)