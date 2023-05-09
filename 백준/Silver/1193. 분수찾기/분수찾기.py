N = int(input())
line = 0
end = 0

while(N>end):
    line+=1
    end+=line
diff = end-N

if line%2==0:
    s = line-diff
    b = diff+1
    print(f'{s}/{b}')
else:
    s = diff+1
    b = line-diff
    print(f'{s}/{b}')